from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions'

    """
        Return the last five published questions (not including those set to be
        published in the future).
    """
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now() #pub_date less-than or equals to ...
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    """
        Excludes any questions that aren't published yet.
    """
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Display the voting form again
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'No choice selected',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Use HttpResponseRedirect after post data as it stops data posting
        # twice if the browser's back button is hit
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
from django.http import HttpResponse, HttpResponseRedirect # Http404
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_questions':  latest_questions
    }
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


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
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from quickstart import views
# from django.core.urlresolvers import reverse_lazy

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)

urlpatterns = [
    # /polls/*
    url(r'^polls/', include('polls.urls')),
    # /admin/*
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # Capture anything that previously didn't match
    # url(r'^.*$', RedirectView.as_view(url=reverse_lazy('polls:index'), permanent=False)),
]

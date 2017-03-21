from django.conf.urls import url
from . import views

urlpatterns= [
    #/poll/
    url(r'^$', views.index, name='index'),
    #/poll/helpme
    url(r'^help/$', views.helpme, name='helpme'),
    #/detail_question
    url(r'^(?P<question_id>[0-9]+)/$', views.detail_question, name='detail_question'),
    #/poll/vote
    url(r'^vote/$', views.vote , name='vote'),
    #/poll/results
    url(r'^results/(?P<question_id>[0-9]+)/$', views.results , name='results'),
]

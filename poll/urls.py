from django.conf.urls import url
from . import views # titik artinya ngambil di folder yang sama

urlpatterns= [
    #/poll/
    url(r'^$', views.index, name='index'),
    #/poll/helpme
    url(r'^help/$', views.helpme, name='helpme'),
    #/detail_question
    url(r'^(?P<question_id>[0-9]+)/$', views.detail_question, name='detail_question'),
]

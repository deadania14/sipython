from django.conf.urls import url
from . import views # titik artinya ngambil di folder yang sama

urlpatterns= [
    #/poll/
    url(r'^$', views.index, name='index'),
    #/poll/helpme
    url(r'^help/$', views.helpme, name='helpme'),
]

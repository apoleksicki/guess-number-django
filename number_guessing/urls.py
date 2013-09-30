'''
Created on 30/09/2013

@author: Antek
'''
from django.conf.urls import patterns, url
from number_guessing import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^play/$', views.play, name='play'))

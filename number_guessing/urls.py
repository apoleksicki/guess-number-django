'''
Created on 30/09/2013

@author: Antek
'''
from django.conf.urls import patterns, url
from number_guessing import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^start_game/$', views.start_game, name='start_game'),
                       url(r'^play/$', views.play, name='play'),
                       url(r'^success/$', views.success, name='success'))

"""Defines URL patterns for learning_logs."""
#from django.conf.urls import url
from django.urls import path,re_path
from . import views
from django.contrib import messages
from django.contrib import auth

urlpatterns = [
   #Home Page
    path('',views.index,name='index'),

    #Show all topics
    re_path(r'^topics/$', views.topics, name='topics'),

    #Show a particular topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #New topic
    re_path(r'^new_topic/$',views.new_topic, name='new_topic'),
    path('new_topic2',views.new_topic2,name='new_topic2'),

    #To add entry to a topic
    re_path(r'^new_entry/(?P<topic_id>\d+)/$' ,views.new_entry, name='new_entry'),

    #To edit an entry of a topic
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$' ,views.edit_entry, name='edit_entry'),

    #To edit a topic
    re_path(r'^edit_topic/(?P<topic_id>\d+)/$' ,views.edit_topic, name='edit_topic'),

    #To delete a topic
    re_path(r'^delete_topic/(?P<topic_id>\d+)/$' ,views.delete_topic, name='delete_topic'),

    #To delete a entry
    re_path(r'^delete_entry/(?P<entry_id>\d+)/$' ,views.delete_entry, name='delete_entry'),
    
]

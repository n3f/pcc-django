"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
	# Topics page
	url(r'^topics/$', views.topics, name='topics'),
	# single topics
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	# new topic
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	# Add entry
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]
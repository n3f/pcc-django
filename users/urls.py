"""Defines url patterns for users."""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

app_name = 'users'
urlpatterns = [
    # Login page.
    url(r'^login/$',
        LoginView.as_view(template_name='users/login.html'),
        name='login'),
]

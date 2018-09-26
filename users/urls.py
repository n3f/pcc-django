"""Defines url patterns for users."""

from django.conf.urls import url
import django.contrib.auth.views as auth_views

app_name = 'users'
urlpatterns = [
    # Login page.
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(next_page='learning_logs:index'),
        name='logout'),
]

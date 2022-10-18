from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.login, name='login'),
    path("signup/", views.signup, name='signup'),
]

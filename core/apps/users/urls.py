# -*- encoding: utf-8 -*-


from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

app_name="users"
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]

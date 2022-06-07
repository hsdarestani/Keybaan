# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from apps.dashboard import views

urlpatterns = [

    path('', views.panel, name='panel'),


]

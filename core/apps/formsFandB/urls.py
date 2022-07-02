# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from .views import *

app_name = "formsFandB"
urlpatterns = [
    path('input', input, name='input'),
    path('output', output, name='output'),
]

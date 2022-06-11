# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from .views import *

app_name = "forms"
urlpatterns = [

    path('contract', contract, name='contract'),
    path('input', input, name='input'),
    path('output', output, name='output'),

]

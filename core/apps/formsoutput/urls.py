# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from .views import *

app_name = "formsoutput"
urlpatterns = [

    path('output', output, name='output'),

]

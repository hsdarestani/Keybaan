# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from .views import *

app_name = "home"
urlpatterns = [

    # The home page
    path('', index, name='index'),

]

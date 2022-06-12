# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from .views import *
app_name = "dashboard"
urlpatterns = [
    path('', panel, name='panel'),
    path('echarts', echarts, name='echarts'),
]

# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from .views import *

app_name = "home"
urlpatterns = [

    # The home page
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('services/', services, name='services'),
    path('FandB', FandB, name='FandB'),
    path('construction/', construction, name='construction'),
    path('advertisement/', advertisement, name='advertisement'),

]

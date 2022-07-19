# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from .views import *

app_name = "formsOOH"
urlpatterns = [
    path('contract', contract, name='contract'),
    path('econtract', econtract, name='econtract'),
    path('ocontract', ocontract, name='ocontract'),
    path('ocontractorpayment', ocontractorpayment, name='ocontractorpayment'),
]

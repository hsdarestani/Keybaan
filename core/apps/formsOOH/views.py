
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def contract(request):
    context = {'segment': 'contract'}

    html_template = loader.get_template('apps/formsOOH/templates/formsOOH/contract.html')
    return HttpResponse(html_template.render(context, request))


def econtract(request):
    context = {'segment': 'econtract'}

    html_template = loader.get_template('apps/formsOOH/templates/formsOOH/econtract.html')
    return HttpResponse(html_template.render(context, request))
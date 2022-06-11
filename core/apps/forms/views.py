
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



def input(request):
    context = {'segment': 'input'}

    html_template = loader.get_template('apps/forms/templates/forms/input.html')
    return HttpResponse(html_template.render(context, request))

def output(request):
    context = {'segment': 'output'}

    html_template = loader.get_template('apps/forms/templates/forms/output.html')
    return HttpResponse(html_template.render(context, request))

def contract(request):
    context = {'segment': 'contract'}

    html_template = loader.get_template('apps/forms/templates/forms/contract.html')
    return HttpResponse(html_template.render(context, request))

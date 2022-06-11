from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def panel(request):
    context = {'segment': 'panel'}

    html_template = loader.get_template('apps/dashboard/templates/dashboard/panel.html')
    return HttpResponse(html_template.render(context, request))

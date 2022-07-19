
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import ContactUsForm
from .models import ContactUs
from django.contrib import messages
from apps.blog.models import Article
from django.shortcuts import render, get_object_or_404

def index(request):
    articles = Article.objects.filter(status="p").order_by('-publish')

    context = {
        'segment': 'index',
        'articles' : articles
    }

    html_template = loader.get_template('apps/home/templates/home/index.html')
    return HttpResponse(html_template.render(context, request))


def about(request):
    context = {'segment': 'about'}

    html_template = loader.get_template('apps/home/templates/home/about.html')
    return HttpResponse(html_template.render(context, request))

def faq(request):
    context = {'segment': 'faq'}

    html_template = loader.get_template('apps/home/templates/home/faq.html')
    return HttpResponse(html_template.render(context, request))




def contact(request):
    context = {'segment': 'contact'}

    html_template = loader.get_template('apps/home/templates/home/contact.html')
    return HttpResponse(html_template.render(context, request))

def services(request):
    context = {'segment': 'services'}

    html_template = loader.get_template('apps/home/templates/home/services.html')
    return HttpResponse(html_template.render(context, request))

def packages(request):
    context = {'segment': 'services'}

    html_template = loader.get_template('apps/home/templates/home/packages.html')
    return HttpResponse(html_template.render(context, request))

def FandB(request):
    context = {'segment': 'FandB'}

    html_template = loader.get_template('apps/home/templates/home/industry-f&b.html')
    return HttpResponse(html_template.render(context, request))

def construction(request):
    context = {'segment': 'construction'}

    html_template = loader.get_template('apps/home/templates/home/industry-construction.html')
    return HttpResponse(html_template.render(context, request))

def advertisement(request):
    context = {'segment': 'advertisement'}

    html_template = loader.get_template('apps/home/templates/home/industry-advertisement.html')
    return HttpResponse(html_template.render(context, request))

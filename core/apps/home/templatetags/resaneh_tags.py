from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.forms import ContactUsForm
from apps.home.models import ContactUs
from django.contrib import messages
from django.shortcuts import render, get_object_or_404,redirect

register = template.Library()


@register.inclusion_tag("apps/home/templates/home/partial/contactform.html" , takes_context=True)
def contactform(context):
    request = context.get('request')
    form = ContactUsForm()
    if request.POST:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
    context ={
        "form" : form,
        }
    return {
        "form" : form,
    }

@register.inclusion_tag("apps/home/templates/home/partial/contactform2.html" , takes_context=True)
def contactform2(context):
    request = context.get('request')
    form2 = ContactUsForm()
    if request.POST:
        form2 = ContactUsForm(request.POST)
        if form2.is_valid():
            form2.save()
    context ={
        "form2" : form2,
        }
    return {
        "form2" : form2,
    }

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404,redirect
from .forms import *
from django.contrib import messages

def input(request):
    form = InputsForm()
    if 'InputsForm' in request.POST:
        form = InputsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            return redirect('formsFandB:input')
        else:
             print(form.errors.as_data())
    context={
        'form':form,
    }
    return render(request, 'apps/formsFandB/templates/formsFandB/input.html', context)

def output(request):
    form = OutputsForm()
    if 'OutputsForm' in request.POST:
        form = OutputsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            return redirect('formsFandB:output')
        else:
             print(form.errors.as_data())
    context={
        'form':form,
    }
    return render(request, 'apps/formsFandB/templates/formsFandB/output.html',context)

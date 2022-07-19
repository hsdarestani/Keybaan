from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404,redirect
from .forms import *
from django.contrib import messages
from .decorators import *
from apps.formsFandB.models import FAgents,Commodities,Inventories,MeasuringUnits,CommodityType

@login_required
@FandB_user
def input(request):
    form = InputsForm()
    form.fields["CommodityID"].queryset = Commodities.objects.filter(Company_id=request.user.profile.company_id)
    form.fields["ToInventoryID"].queryset = Inventories.objects.filter(Company_id=request.user.profile.company_id)

    if 'InputsForm' in request.POST:
        user = request.user.profile
        company = request.user.profile.company_id
        form = InputsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.EntryAgent = user
            obj.Company_id = company
            obj.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            return redirect('formsFandB:input')
        else:
             print(form.errors.as_data())
    context={
        'form':form,
    }
    return render(request, 'apps/formsFandB/templates/formsFandB/input.html', context)

@login_required
@FandB_user
def output(request):
    form = OutputsForm()
    form.fields["DeliveryAgent"].queryset = FAgents.objects.filter(Company_id=request.user.profile.company_id)
    form.fields["CommodityID"].queryset = Commodities.objects.filter(Company_id=request.user.profile.company_id)
    form.fields["FromInventoryID"].queryset = Inventories.objects.filter(Company_id=request.user.profile.company_id)

    if 'OutputsForm' in request.POST:
        user = request.user.profile
        company = request.user.profile.company_id
        form = OutputsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.EntryAgent = user
            obj.Company_id = company
            obj.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            return redirect('formsFandB:output')
        else:
             print(form.errors.as_data())
    context={
        'form':form,
    }
    return render(request, 'apps/formsFandB/templates/formsFandB/output.html',context)


def load_units(request):
    CommodityID = request.GET.get('CommodityID')
    aa = Commodities.objects.get(id=CommodityID)
    bb = aa.CommodityTypeID
    cc = bb.MeasuringUnitID
    # print(Commodities.objects.filter(id=CommodityID))
    # MeasuringUnit = Commodities.CommodityType.objects.filter(id=CommodityID)
    return render(request, 'apps/formsFandB/templates/formsFandB/units.html', {'MeasuringUnit': cc})

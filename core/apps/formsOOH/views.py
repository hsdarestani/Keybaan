from django.shortcuts import render, get_object_or_404,redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import *
from django.contrib import messages

def contract(request):
    form1 = ContractsForm()
    form2 = ContractDetailsPerBoardForm()
    form3 = InstallmentForm()
    form4 = CustomersForm()


    if 'AddCustomer' in request.POST:
        form4 = CustomersForm(request.POST)
        if (form4.is_valid()):
            form4.save()
            return redirect('formsOOH:contract')
    if 'ContractNumber' in request.POST:
        form1 = ContractsForm(request.POST)
        form2 = ContractDetailsPerBoardForm(request.POST)
        form3 = InstallmentForm(request.POST)
        if all([form1.is_valid(),form2.is_valid(),form3.is_valid()]):
            form1.save()
            form2.save()
            form3.save()
            return redirect('formsOOH:contract')
        else:
             print(form1.errors.as_data())
             print(form2.errors.as_data())
             print(form3.errors.as_data())
             messages.info(request, "نام‌کاربری یا رمز عبور اشتباه است!")
    # print(len(request.POST), "asdas")
    # if(len(request.POST) == 0):
    #     form4 = CustomersForm(request.POST)
    #     print("asdas")
    #     # form4.save()
    #     if (form4.is_valid()):
    #         form4.save()
    #
    # if all([form1.is_valid(),form2.is_valid(),form3.is_valid()]):
    #     form1.save()
    #     obj = form2.save()
    #     obj.DailyPrice = (obj.ContractPrice*(obj.ContractFinish-obj.ContractStart+1))
    #     obj.save()
    #     form3.save()
    #     messages.success(request,'پیام شما با موفقیت ارسال گردید.')
    context={
        'form1':form1,
        'form2':form2,
        'form3':form3,
        'form4':form4,
    }
    return render(request, 'apps/formsOOH/templates/formsOOH/contract.html', context)

def econtract(request):

    form = eContractsForm()

    if 'eContracts' in request.POST:
        form = eContractsForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('formsOOH:econtract')
    context={
        'form':form,
    }
    return render(request, 'apps/formsOOH/templates/formsOOH/econtract.html', context)

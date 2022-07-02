from django.shortcuts import render, get_object_or_404,redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import *
from django.contrib import messages
from .decorators import *
from apps.formsOOH.models import Customers,Boards,Agents,ContractDetailsPerBoard, Installment,Contracts
from django.forms import formset_factory

@login_required
@OOH_user
def contract(request):
    form1 = ContractsForm()
    # form3 = modelformset_factory(Installment,form=InstallmentForm)
    # qs = objb.Installment_set.all()
    # formset3 = form3(request.POST)
    form2 = ContractDetailsPerBoardForm()
    form3 = InstallmentForm()
    form2set = formset_factory(ContractDetailsPerBoardForm)
    form3set = formset_factory(InstallmentForm)

    formset2 = form2set(request.POST or None,prefix='formset2')
    formset = form3set(request.POST or None,prefix='formset3')
    form4 = CustomersForm()
    form1.fields["CustomerID"].queryset = Customers.objects.filter(Company_id=request.user.profile.company_id)
    form2.fields["BoardID"].queryset = Boards.objects.filter(Company_id=request.user.profile.company_id)
    form2.fields["AgentNameID"].queryset = Agents.objects.filter(Company_id=request.user.profile.company_id)

    if 'AddCustomer' in request.POST:
        user = request.user.profile
        company = request.user.profile.company_id
        form4 = CustomersForm(request.POST)
        print(request.user.profile.company_id)
        if (form4.is_valid()):
            obj = form4.save(commit=False)
            obj.EntryAgent = user
            obj.Company_id = company
            obj.save()
            return redirect('formsOOH:contract')
    if 'ContractNumber' in request.POST:
        user = request.user.profile
        company = request.user.profile.company_id
        form1 = ContractsForm(request.POST)
        form2 = ContractDetailsPerBoardForm(request.POST)
        form3 = InstallmentForm(request.POST)
        if all([form1.is_valid(),formset2.is_valid(),formset.is_valid()]):
            obj = form1.save(commit=False)
            obj.EntryAgent = user
            obj.Company_id = company
            obj.save()
            conb = Contracts.objects.get(ContractNumber = obj.ContractNumber) # []
            # for formx2 in formset2:
            # obj2 = form2.save(commit=False)
            # obj2.EntryAgent = user
            # obj2.Company_id = company
            # obj2.save()
            print (conb)
            for form2 in formset2:
                obj2 = form2.save(commit=False)
                # for ins in formset3:
                #     ins.EntryAgent = user
                #     ins.Company_id = company
                #     ins.save()
                obj2.ContractID = conb
                obj2.EntryAgent = user
                obj2.Company_id = company
                obj2.save()
            for form in formset:
                obj3 = form.save(commit=False)
                # for ins in formset3:
                #     ins.EntryAgent = user
                #     ins.Company_id = company
                #     ins.save()
                obj3.ContractID = conb
                obj3.EntryAgent = user
                obj3.Company_id = company
                obj3.save()
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
        'formset2' : formset2,
        'form3':form3,
        'formset':formset,
        'form4':form4,
    }
    return render(request, 'apps/formsOOH/templates/formsOOH/contract.html', context)

@login_required
@OOH_user
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

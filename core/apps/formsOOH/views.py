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
from extensions import jalali
import datetime


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
    form1.fields["AgentNameID"].queryset = Agents.objects.filter(Company_id=request.user.profile.company_id)
    mamadBoards = Boards.objects.filter(Company_id=request.user.profile.company_id)

    if 'AddCustomer' in request.POST:
        user = request.user.profile
        company = request.user.profile.company_id
        form4 = CustomersForm(request.POST)
        print(request.user.profile.company_id)
        if (form4.is_valid()):
            obj = form4.save(commit=False)
            try:
                get_object_or_404(Customers,CustomerName = obj.CustomerName)
                cuscheck = 1
            except:
                cuscheck = 0
            if (cuscheck):
                messages.info(request, "این نام مشتری قبلا ثبت شده است")
            else:
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
            obj.ContractConfirmDate = jalali.Persian(str(obj.ContractConfirmDateJalali)).gregorian_string()
            try:
                conNcheck = get_object_or_404(Contracts,ContractNumber = obj.ContractNumber)
            except:
                conNcheck = 0
            if (conNcheck):
                 messages.info(request, "این شماره قرارداد قبلا ثبت شده است")
            elif (int(obj.PrePayment) > int(obj.ContractPrice)):
                 messages.info(request, "مبلغ پیش پرداخت، بیشتر از مبلغ کل قرارداد وارد شده است")
            else:
                obj.EntryAgent = user
                obj.Company_id = company
                obj.save()
                conb = Contracts.objects.get(ContractNumber = obj.ContractNumber)
                for form2 in formset2:
                    obj2 = form2.save(commit=False)
                    obj2.AgentNameID = obj.AgentNameID
                    obj2.ContractStart = jalali.Persian(str(obj2.JalaliStart)).gregorian_string()
                    obj2.ContractFinish = jalali.Persian(str(obj2.JalaliFinish)).gregorian_string()
                    try:
                        SameBoards = ContractDetailsPerBoard.objects.all(BoardID = obj2.BoardID)
                        for board in SameBoards:
                            if ((board.ContractStart > obj2.ContractStart and board.ContractFinish < obj2.ContractFinish) or (board.ContractStart < obj2.ContractStart and  board.ContractFinish > obj2.ContractFinish) or (board.ContractFinish > obj2.ContractStart and  board.ContractFinish < obj2.ContractFinish) or (board.ContractStart > obj2.ContractStart and  board.ContractStart < obj2.ContractFinish)):
                                SameBoardscheck = 1
                            else:
                                SameBoardscheck = 0
                    except:
                        SameBoardscheck = 0
                    if (SameBoardscheck):
                        messages.info(request, "این تابلو در بازه ثبت شده در قرارداد دیگری در اکران است!")
                    elif (obj2.ContractStart > obj2.ContractFinish):
                        messages.info(request, "تاریخ شروع اکران نباید زودتر از تاریخ پایان اکران باشد")
                    else:
                        starbrd = datetime.datetime.strptime(obj2.ContractStart, '%Y-%m-%d')
                        fnshbrd = datetime.datetime.strptime(obj2.ContractFinish, '%Y-%m-%d')
                        delta = fnshbrd - starbrd
                        obj2.DailyPrice = int(obj2.BoardContractPrice) /(delta.days +1)
                        obj2.ContractID = conb
                        obj2.EntryAgent = user
                        obj2.Company_id = company
                        obj2.save()
                insnum = 1
                inssum = 0
                for form in formset:
                     obj3 = form.save(commit=False)
                     try:
                         SameIns = Installments.objects.all(ContractID = obj3.ContractID)
                         for ins in SameIns:
                             inssum += ins.Installment
                     except:
                         SameBoardscheck = 0
                     obj3.PaymentDate = jalali.Persian(str(obj3.PaymentDateJalali)).gregorian_string()
                     obj3.ContractID = conb
                     obj3.EntryAgent = user
                     obj3.Company_id = company
                     obj3.save()
                     insnum += 1
                # if (inssum != int(obj.ContractPrice)):
                #     messages.info(request, "مجموع اقساط با مبلغ کل قرارداد برابر نشده است")
                return redirect('formsOOH:contract')
    context={
        'form1':form1,
        'mamadBoards':mamadBoards,
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

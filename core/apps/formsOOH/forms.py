from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ('CustomerName',)

    def __init__(self, *args, **kwargs):
        super(CustomersForm, self).__init__(*args, **kwargs)
        self.fields['CustomerName'].widget.attrs['class'] = 'kbforms'

class OCustomersForm(ModelForm):
    class Meta:
        model = OCustomers
        fields = ('CustomerName',)

    def __init__(self, *args, **kwargs):
        super(OCustomersForm, self).__init__(*args, **kwargs)
        self.fields['CustomerName'].widget.attrs['placeholder'] = 'نام مشتری'
        self.fields['CustomerName'].widget.attrs['class'] = 'kbforms'

class OContractorForm(ModelForm):
    class Meta:
        model = OContractor
        fields = ('Contractor','ContractorType',)

    def __init__(self, *args, **kwargs):
        super(OContractorForm, self).__init__(*args, **kwargs)
        self.fields['Contractor'].widget.attrs['placeholder'] = 'نام پیمانکار'
        self.fields['ContractorType'].widget.attrs['placeholder'] = 'نوع پیمانکار'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'

class OContractsForm(ModelForm):
    class Meta:
        model = OContracts
        fields = ('ContractNumber','CustomerID','ContractConfirmDateJalali',)
    def __init__(self, *args, **kwargs):
        super(OContractsForm, self).__init__(*args, **kwargs)
        self.fields['ContractNumber'].widget.attrs['placeholder'] = 'شماره قرارداد'
        self.fields['CustomerID'].widget.attrs['placeholder'] = 'نام مشتری'
        self.fields['ContractConfirmDateJalali'].widget.attrs['placeholder'] = 'تاریخ ثبت قرارداد'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'

        self.fields['ContractConfirmDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['CustomerID'].widget.attrs['class'] = 'searchable CsSelc'
        self.fields['ContractConfirmDateJalali'].widget.attrs['id'] = 'ContractConfirmDateJalali'

class ContractsForm(ModelForm):
    class Meta:
        model = Contracts
        fields = ('ContractNumber','AgentNameID' ,'CustomerID','PrePayment','ContractPrice','ContractConfirmDateJalali','IsExpanded','ValueAddedTax',)
    def __init__(self, *args, **kwargs):
        super(ContractsForm, self).__init__(*args, **kwargs)
        self.fields['ContractNumber'].widget.attrs['placeholder'] = 'شماره قرارداد'
        self.fields['CustomerID'].widget.attrs['placeholder'] = 'نام مشتری'
        self.fields['PrePayment'].widget.attrs['placeholder'] = 'پیش پرداخت (ریال)'
        self.fields['ContractPrice'].widget.attrs['placeholder'] = 'مبلغ کل قرارداد (ریال)'
        self.fields['ContractConfirmDateJalali'].widget.attrs['placeholder'] = 'تاریخ ثبت قرارداد'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'

        self.fields['ContractConfirmDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['CustomerID'].widget.attrs['class'] = 'searchable CsSelc'
        self.fields['AgentNameID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['IsExpanded'].widget.attrs['class'] = ''
        self.fields['ValueAddedTax'].widget.attrs['class'] = ''
        self.fields['ContractConfirmDateJalali'].widget.attrs['id'] = 'ContractConfirmDateJalali'

class eContractsForm(ModelForm):
    class Meta:
        model = Contracts
        fields = ('ContractNumber','IsCancelled','CancelingDateJalali',)
    def __init__(self, *args, **kwargs):
        super(eContractsForm, self).__init__(*args, **kwargs)
        self.fields['ContractNumber'].widget.attrs['placeholder'] = 'شماره قرارداد'
        self.fields['CancelingDateJalali'].widget.attrs['placeholder'] = 'تاریخ فسخ قرارداد'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'

        self.fields['CancelingDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['ContractNumber'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['IsCancelled'].widget.attrs['class'] = ''
        self.fields['CancelingDateJalali'].widget.attrs['id'] = 'CancelingDateJalali'

class OContractDetailsPerBoardForm(ModelForm):
    class Meta:
        model = OContractDetailsPerBoard
        fields = ('BoardID',)

    def __init__(self, *args, **kwargs):
        super(OContractDetailsPerBoardForm, self).__init__(*args, **kwargs)
        self.fields['BoardID'].widget.attrs['class'] = 'searchable kbforms'

class OOperationForm(ModelForm):
    class Meta:
        model = OOperation
        fields = ('OperationTypeID','ContractorID','OperationDateJalali','OperationFee','OperationTariff')

    def __init__(self, *args, **kwargs):
        super(OOperationForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'
        self.fields['OperationDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['OperationTypeID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['ContractorID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['OperationDateJalali'].widget.attrs['id'] = 'OperationDateJalali'


class OContractorPaymentForm(ModelForm):
    class Meta:
        model = OContractorPayment
        fields = ('PaymentFee','ContractorID','PaymentDateJalali')

    def __init__(self, *args, **kwargs):
        super(OContractorPaymentForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'
        self.fields['PaymentDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['ContractorID'].widget.attrs['class'] = 'searchable kbforms'        
        self.fields['PaymentDateJalali'].widget.attrs['id'] = 'PaymentDateJalali'


class ContractDetailsPerBoardForm(ModelForm):
    class Meta:
        model = ContractDetailsPerBoard
        fields = ('ContractID','BoardID','DailyPrice','BoardContractPrice','JalaliStart','JalaliFinish','AgentNameID',)

    def __init__(self, *args, **kwargs):
        super(ContractDetailsPerBoardForm, self).__init__(*args, **kwargs)
        self.fields['ContractID'].widget.attrs['placeholder'] = 'شماره قرارداد'
        self.fields['BoardID'].widget.attrs['placeholder'] = 'کد تابلو'
        self.fields['BoardContractPrice'].widget.attrs['placeholder'] = 'مبلغ قرارداد تابلو (ریال)'
        self.fields['JalaliStart'].widget.attrs['placeholder'] = 'شروع اکران'
        self.fields['JalaliFinish'].widget.attrs['placeholder'] = 'پایان اکران'
        self.fields['AgentNameID'].widget.attrs['placeholder'] = 'مسئول فروش'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'
        self.fields['JalaliStart'].widget.attrs['readonly'] = 'readonly'
        self.fields['JalaliFinish'].widget.attrs['readonly'] = 'readonly'
        self.fields['JalaliStart'].widget.attrs['class'] = 'kbforms JalaliStart'
        self.fields['JalaliFinish'].widget.attrs['class'] = 'kbforms JalaliFinish'
        self.fields['AgentNameID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['BoardID'].widget.attrs['class'] = 'kbforms'
        # self.fields['JalaliStart'].widget.attrs['id'] = 'JalaliStart'
        # self.fields['JalaliFinish'].widget.attrs['id'] = 'JalaliFinish'

class InstallmentForm(ModelForm):
    class Meta:
        model = Installment
        fields = ('ContractID','Installment','InstallmentNumber','PaymentDate','PaymentDateJalali',)
    def __init__(self, *args, **kwargs):
        super(InstallmentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'
        self.fields['Installment'].widget.attrs['placeholder'] = 'مبلغ قسط (ریال)'
        self.fields['InstallmentNumber'].widget.attrs['placeholder'] = 'نوبت قسط'
        self.fields['PaymentDateJalali'].widget.attrs['placeholder'] = 'تاریخ پرداخت'
        # self.fields['PaymentDateJalali'].widget.attrs['id'] = 'PaymentDateJalali'
        self.fields['PaymentDateJalali'].widget.attrs['class'] = 'kbforms PaymentDateJalali'
        self.fields['PaymentDateJalali'].widget.attrs['readonly'] = 'readonly'

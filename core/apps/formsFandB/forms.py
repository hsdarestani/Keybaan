from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field


class InputsForm(ModelForm):
    class Meta:
        model = Inputs
        fields = ('TransfereeAgent','ProcurementID','ToInventoryID','TransferedDateJalali','TransferedQuantity',)
    def __init__(self, *args, **kwargs):
        super(InputsForm, self).__init__(*args, **kwargs)
        self.fields['ProcurementID'].widget.attrs['placeholder'] = 'قلم کالا'
        self.fields['TransferedDateJalali'].widget.attrs['placeholder'] = 'تاریخ ورود'
        self.fields['TransferedQuantity'].widget.attrs['placeholder'] = 'مقدار'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'

        self.fields['TransferedDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['ProcurementID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['TransferedDateJalali'].widget.attrs['id'] = 'TransferedDateJalali'


class OutputsForm(ModelForm):
    class Meta:
        model = Outputs
        fields = ('DeliveryAgent','ProcurementID','FromInventoryID','TransferedDateJalali','TransferedQuantity',)

    def __init__(self, *args, **kwargs):
        super(OutputsForm, self).__init__(*args, **kwargs)
        self.fields['ProcurementID'].widget.attrs['placeholder'] = 'قلم کالا'
        self.fields['TransferedDateJalali'].widget.attrs['placeholder'] = 'تاریخ خروج'
        self.fields['TransferedQuantity'].widget.attrs['placeholder'] = 'مقدار'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'

        self.fields['TransferedDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['ProcurementID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['TransferedDateJalali'].widget.attrs['id'] = 'TransferedDateJalali'

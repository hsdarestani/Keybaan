from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field


class InputsForm(ModelForm):
    class Meta:
        model = Inputs
        fields = ('TransfereeAgent','CommodityID','ToInventoryID','TransferedDateJalali','TransferedQuantity',)
    def __init__(self, *args, **kwargs):
        super(InputsForm, self).__init__(*args, **kwargs)
        self.fields['CommodityID'].widget.attrs['placeholder'] = 'قلم کالا'
        self.fields['TransferedDateJalali'].widget.attrs['placeholder'] = 'تاریخ ورود'
        self.fields['TransferedQuantity'].widget.attrs['placeholder'] = 'مقدار'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'

        self.fields['TransferedDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['TransferedQuantity'].widget.attrs['class'] = 'w40'
        self.fields['CommodityID'].widget.attrs['class'] = ' kbforms'
        self.fields['CommodityID'].widget.attrs['data-cities-url'] = 'ajax_load_units'
        self.fields['ToInventoryID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['TransferedDateJalali'].widget.attrs['id'] = 'TransferedDateJalali'


class OutputsForm(ModelForm):
    class Meta:
        model = Outputs
        fields = ('DeliveryAgent','CommodityID','FromInventoryID','TransferedDateJalali','TransferedQuantity',)

    def __init__(self, *args, **kwargs):
        super(OutputsForm, self).__init__(*args, **kwargs)
        self.fields['CommodityID'].widget.attrs['placeholder'] = 'قلم کالا'
        self.fields['TransferedDateJalali'].widget.attrs['placeholder'] = 'تاریخ خروج'
        self.fields['TransferedQuantity'].widget.attrs['placeholder'] = 'مقدار'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'kbforms'

        self.fields['TransferedDateJalali'].widget.attrs['readonly'] = 'readonly'
        self.fields['CommodityID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['TransferedQuantity'].widget.attrs['class'] = 'w40'
        self.fields['DeliveryAgent'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['FromInventoryID'].widget.attrs['class'] = 'searchable kbforms'
        self.fields['TransferedDateJalali'].widget.attrs['id'] = 'TransferedDateJalali'

from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

class ticketform(ModelForm):
        class Meta:
            model = Ticket
            fields = ['title','assignee','description']

        def __init__(self, *args, **kwargs):
            super(ticketform, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'kbforms'
                
            self.fields['description'].widget.attrs.update({
                'rows': '5'})

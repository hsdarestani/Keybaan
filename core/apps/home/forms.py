from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import ContactUs
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

class ContactUsForm(ModelForm):
        class Meta:
            model = ContactUs
            fields = ['csname','emailaddress','description']

        def __init__(self, *args, **kwargs):
            super(ContactUsForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'contactus'

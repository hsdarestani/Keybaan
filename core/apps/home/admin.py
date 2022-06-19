from django.contrib import admin
from .models import ContactUs
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('csname','emailaddress')
    search_fields = ('csname','emailaddress','description')
admin.site.register(ContactUs, ContactUsAdmin)

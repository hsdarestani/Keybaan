from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Company, Position, Industry
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company','status', 'position',)
    ordering = ['user', 'company']
    list_filter = ( 'position','status')
    search_fields = ('company','user',)

admin.site.register(Profile,ProfileAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ['name', ]
    search_fields = ('name',)

admin.site.register(Company,CompanyAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('position',)
    search_fields = ('position',)

admin.site.register(Position,PositionAdmin)

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('Industry',)
    search_fields = ('Industry',)

admin.site.register(Industry,IndustryAdmin)

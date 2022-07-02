
from django.contrib.auth.models import AbstractUser, BaseUserManager,User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.urls import reverse
from extensions.utils import jalali_converter
from django.core.validators import RegexValidator

# Create your models here.


class Position(models.Model):
    position = models.CharField(max_length=40, null=True, verbose_name="رده", blank=True)

    class Meta:
        verbose_name = "رده"
        verbose_name_plural = "رده‌ها"

    def __str__(self):
        return str(self.position)

class Industry(models.Model):
    Industry = models.CharField(max_length=40, null=True, verbose_name="صنعت", blank=True)
    class Meta:
        verbose_name = "صنعت"
        verbose_name_plural = "صنایع"

    def __str__(self):
        return str(self.Industry)

class Company(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name="نام",  blank=True)
    IndustrySel = models.ForeignKey(Industry, default=None, null=True, verbose_name="صنعت", on_delete=models.CASCADE, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, verbose_name="تاریخ ایجاد",  blank=True)

    class Meta:
        verbose_name = "شرکت"
        verbose_name_plural = "شرکت‌ها"

    def __str__(self):
        return str(self.name)

# Model
class Profile(models.Model):

    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE, verbose_name="کاربر", related_name="profile")
    firstname = models.CharField(max_length=200, null=True, verbose_name="نام")
    lastname = models.CharField(max_length=200, null=True, verbose_name="نام‌خانوادگی")
    position = models.ForeignKey(Position, default=None, null=True, verbose_name="رده", on_delete=models.CASCADE, blank=True)
    IndustrySel = models.ForeignKey(Industry, default=None, null=True, verbose_name="صنعت", on_delete=models.CASCADE, blank=True)   
    company = models.ForeignKey(Company, default=None, null=True, verbose_name="شرکت", on_delete=models.CASCADE, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, verbose_name="تاریخ ایجاد",  blank=True)
    sphone = models.CharField(max_length=200, null=True, verbose_name="تلفن ثابت", blank=True)
    mphone = models.CharField(max_length=200, null=True, verbose_name="تلفن همراه", blank=True)
    status = models.BooleanField(default=False, verbose_name="وضعیت حساب")


    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب‌های کاربری"

    def __str__(self):
        return str(self.user)

    def jdate_created(self):
        return jalali_converter(self.date_created)
    jdate_created.short_description = "تاریخ عضویت"
    # def get_absolute_url(self):
    #     return reverse('account:login_register')

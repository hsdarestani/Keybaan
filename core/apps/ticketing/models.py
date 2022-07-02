from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from extensions.utils import jalali_converter
from apps.useraccount.models import Profile
# Create your models here.
class TicketStatus(models.TextChoices):
 TO_DO = 'جدید'
 IN_PROGRESS = 'در حال بررسی'
 IN_REVIEW = 'نیازمند پاسخ مشتری'
 DONE = 'تکمیل'

class Ticket(models.Model):
     created_by = models.OneToOneField(User, related_name="سازنده",null=True, blank = True,on_delete=models.CASCADE, verbose_name="سازنده تیکت")
     title = models.CharField(max_length=100, verbose_name="عنوان")
     assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE, verbose_name="بخش")
     status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
     description = models.TextField( verbose_name="متن تیکت")
     created_at = models.DateTimeField('ایجاد شده در', auto_now_add=True)
     updated_at = models.DateTimeField('به روز شده در', auto_now=True)

     class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت‌ها"

     def __str__(self):
        return str(self.title)

     def jEntryDate(self):
         return jalali_converter(self.created_at)
     jEntryDate.short_description = "تاریخ ثبت رکورد"
     def jUpdateDate(self):
         return jalali_converter(self.updated_at)
     jUpdateDate.short_description = "تاریخ به روز رسانی"

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TicketStatus(models.TextChoices):
 TO_DO = 'جدید'
 IN_PROGRESS = 'در حال بررسی'
 IN_REVIEW = 'نیازمند پاسخ مشتری'
 DONE = 'تکمیل'

class Ticket(models.Model):
 title = models.CharField(max_length=100)
 assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
 status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
 description = models.TextField()
 created_at = models.DateTimeField('ایجاد شده در', auto_now_add=True)
 updated_at = models.DateTimeField('به روز شده در', auto_now=True)

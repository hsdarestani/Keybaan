from django.db import models
# Create your models here.
class ContactUs(models.Model):
    csname = models.CharField(max_length=200, null=True, verbose_name="نام و نام خانوادگی")
    emailaddress = models.CharField(max_length=200, null=True, verbose_name="آدرس ایمیل")
    description = models.TextField(verbose_name="توضیحات",blank=True)

    class Meta:
        verbose_name = "فرم ارتباط با ما"
        verbose_name_plural = "فرم‌های ارتباط با ما"

    def __str__(self):
        return self.csname

# Generated by Django 4.0.5 on 2022-06-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('جدید', 'To Do'), ('در حال بررسی', 'In Progress'), ('نیازمند پاسخ مشتری', 'In Review'), ('تکمیل', 'Done')], default='جدید', max_length=25),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='به روز شده در'),
        ),
    ]
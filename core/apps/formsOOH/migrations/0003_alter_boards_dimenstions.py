# Generated by Django 4.0.5 on 2022-06-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsOOH', '0002_agentpaymentmethods_agents_agentmail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='Dimenstions',
            field=models.CharField(max_length=200, null=True, verbose_name='ابعاد'),
        ),
    ]

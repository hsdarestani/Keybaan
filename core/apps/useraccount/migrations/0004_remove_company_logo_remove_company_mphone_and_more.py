# Generated by Django 4.0.5 on 2022-06-30 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0003_alter_industry_options_alter_position_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='company',
            name='mphone',
        ),
        migrations.RemoveField(
            model_name='company',
            name='sphone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pic',
        ),
        migrations.AddField(
            model_name='company',
            name='IndustrySel',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='useraccount.industry', verbose_name='صنعت'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='Industry',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='صنعت'),
        ),
        migrations.AlterField(
            model_name='position',
            name='position',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='رده'),
        ),
    ]

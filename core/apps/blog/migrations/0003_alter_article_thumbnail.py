# Generated by Django 4.0.5 on 2022-07-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(upload_to='media/blogimages', verbose_name='تصویر'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-07-09 06:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آدرس آی\u200cپی')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته\u200cبندی')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.category', verbose_name='زیرشاخه')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='تیتر خبر')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس')),
                ('minidescription', models.CharField(max_length=500, verbose_name='خلاصه')),
                ('description', models.TextField(verbose_name='متن')),
                ('thumbnail', models.ImageField(upload_to='media/blogimages', verbose_name='تصویر')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='useraccount.profile', verbose_name='نویسنده')),
                ('category', models.ManyToManyField(related_name='articles', to='blog.category', verbose_name='دسته\u200cبندی')),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'خبرها',
            },
        ),
    ]

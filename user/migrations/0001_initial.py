# Generated by Django 4.2.7 on 2023-12-02 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=30, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=30, verbose_name='Second Name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number_pnone', models.IntegerField(max_length=10, unique=True)),
                ('date_registration', models.DateField(verbose_name=datetime.datetime(2023, 12, 2, 12, 24, 11, 159588))),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1, verbose_name='Gender')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-02 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_registration',
            field=models.DateField(verbose_name=datetime.datetime(2023, 12, 2, 12, 24, 55, 169414)),
        ),
    ]
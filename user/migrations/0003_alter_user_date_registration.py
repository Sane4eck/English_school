# Generated by Django 4.2.7 on 2023-12-02 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_date_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_registration',
            field=models.DateField(verbose_name=datetime.datetime(2023, 12, 2, 12, 25, 51, 948085)),
        ),
    ]

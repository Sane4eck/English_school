# Generated by Django 4.2.7 on 2023-12-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_teacher_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='language',
            field=models.CharField(blank=True, choices=[('French', 'French'), ('Ukrainian', 'Ukrainian'), ('Polish', 'Polish'), ('English', 'English'), ('German', 'German')], max_length=15, verbose_name='Teaching Language'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
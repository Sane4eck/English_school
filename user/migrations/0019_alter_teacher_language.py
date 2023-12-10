# Generated by Django 4.2.7 on 2023-12-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_teacher_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='language',
            field=models.CharField(blank=True, choices=[('German', 'German'), ('Ukrainian', 'Ukrainian'), ('English', 'English'), ('French', 'French'), ('Polish', 'Polish')], max_length=15, verbose_name='Teaching Language'),
        ),
    ]

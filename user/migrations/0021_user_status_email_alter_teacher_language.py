# Generated by Django 5.0 on 2023-12-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_alter_teacher_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status_email',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending', max_length=8, verbose_name='Status_email'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='language',
            field=models.CharField(blank=True, choices=[('Ukrainian', 'Ukrainian'), ('German', 'German'), ('French', 'French'), ('Polish', 'Polish'), ('English', 'English')], max_length=15, verbose_name='Teaching Language'),
        ),
    ]

# Generated by Django 4.2.6 on 2024-07-29 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]

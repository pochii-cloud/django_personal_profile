# Generated by Django 4.0.1 on 2022-01-30 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Feedback',
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'messages'},
        ),
    ]

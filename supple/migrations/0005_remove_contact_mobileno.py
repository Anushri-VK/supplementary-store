# Generated by Django 3.0.6 on 2020-05-27 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supple', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='mobileno',
        ),
    ]

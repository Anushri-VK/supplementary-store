# Generated by Django 3.0.6 on 2020-05-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supple', '0002_auto_20200526_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='address',
            field=models.CharField(default='null', max_length=20),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supple', '0005_remove_contact_mobileno'),
    ]

    operations = [
        migrations.CreateModel(
            name='ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(default='null', max_length=200)),
                ('message', models.CharField(default='null', max_length=2000)),
            ],
        ),
    ]

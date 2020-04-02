# Generated by Django 3.0.4 on 2020-03-27 15:11

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateTimeField(default=None),
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20200403_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug_hash',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=10),
        ),
    ]
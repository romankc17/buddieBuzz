# Generated by Django 3.0.4 on 2020-04-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200402_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(max_length=500),
        ),
    ]

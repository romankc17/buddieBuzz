# Generated by Django 3.0.4 on 2020-03-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200329_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='_profile_followers_+', to='account.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='_profile_followings_+', to='account.Profile'),
        ),
    ]

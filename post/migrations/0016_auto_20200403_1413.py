# Generated by Django 3.0.4 on 2020-04-03 08:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0015_auto_20200403_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='likes',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
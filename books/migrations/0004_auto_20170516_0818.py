# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 08:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_auto_20170515_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='books',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='users',
        ),
        migrations.AddField(
            model_name='books',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]

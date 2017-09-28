# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muss', '0007_auto_20170926_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='public_forum',
            field=models.BooleanField(default=False, help_text="If the forum is public and don't to register to the forum", verbose_name='Public'),
        ),
    ]
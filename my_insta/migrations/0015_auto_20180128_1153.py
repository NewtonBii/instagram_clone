# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-28 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_insta', '0014_auto_20180128_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='image',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20160316_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_copies',
            old_name='Book_id',
            new_name='Book',
        ),
    ]
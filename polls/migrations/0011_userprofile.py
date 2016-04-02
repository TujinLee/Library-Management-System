# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 15:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0010_auto_20160316_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('mobile', models.CharField(max_length=15)),
                ('Ssn', models.CharField(max_length=60)),
                ('Address', models.CharField(max_length=60)),
                ('Card_no', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0022_auto_20140914_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='id',
        ),
        migrations.AlterField(
            model_name='news',
            name='home_news',
            field=models.CharField(max_length=200, primary_key=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='inner_news',
            field=models.TextField(max_length=200, serialize=False, primary_key=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0024_auto_20140914_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='home_news',
            field=models.CharField(max_length=200, primary_key=True),
        ),
    ]

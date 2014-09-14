# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0020_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='home_news',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='inner_news',
            field=models.TextField(max_length=200),
        ),
    ]

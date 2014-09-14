# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0005_auto_20140913_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='is_term',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0007_auto_20140913_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='term_grades',
            field=models.TextField(default=True, max_length=200),
            preserve_default=True,
        ),
    ]

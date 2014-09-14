# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0006_grades_is_term'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='manufacter',
        ),
        migrations.DeleteModel(
            name='Grades',
        ),
        migrations.AddField(
            model_name='student',
            name='grades',
            field=models.TextField(default=True, max_length=1000),
            preserve_default=True,
        ),
    ]

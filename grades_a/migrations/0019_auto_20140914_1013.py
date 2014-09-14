# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0018_auto_20140914_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='alg_grades',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='alg_term_grades',
            field=models.TextField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='geom_grades',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='geom_term_grades',
            field=models.TextField(max_length=200, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0010_int_grades'),
    ]

    operations = [
        migrations.AddField(
            model_name='int_grades',
            name='geom_term',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='int_grades',
            name='student',
            field=models.OneToOneField(to='grades_a.student'),
        ),
    ]

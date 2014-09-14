# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0008_student_term_grades'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='grades',
            new_name='alg_grades',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='term_grades',
            new_name='alg_term_grades',
        ),
        migrations.AddField(
            model_name='student',
            name='geom_grades',
            field=models.TextField(default=True, max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='geom_term_grades',
            field=models.TextField(default=True, max_length=200),
            preserve_default=True,
        ),
    ]

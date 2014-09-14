# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0011_auto_20140914_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='int_grades',
            name='student',
            field=models.ForeignKey(to='grades_a.student'),
        ),
    ]

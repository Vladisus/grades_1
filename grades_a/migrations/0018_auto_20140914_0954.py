# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0017_auto_20140914_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latest_work',
            name='name',
        ),
        migrations.DeleteModel(
            name='latest_work',
        ),
        migrations.AddField(
            model_name='student',
            name='latest_grade',
            field=models.CharField(default=b'---', max_length=20),
            preserve_default=True,
        ),
    ]

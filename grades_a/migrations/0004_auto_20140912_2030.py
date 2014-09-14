# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0003_auto_20140912_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='name',
        ),
        migrations.AddField(
            model_name='car',
            name='grade',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]

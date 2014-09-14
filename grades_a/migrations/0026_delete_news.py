# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0025_auto_20140914_1054'),
    ]

    operations = [
        migrations.DeleteModel(
            name='news',
        ),
    ]

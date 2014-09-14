# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0027_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='new',
            field=models.TextField(max_length=200),
        ),
    ]

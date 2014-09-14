# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0019_auto_20140914_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_news', models.TextField()),
                ('inner_news', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

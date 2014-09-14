# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0016_auto_20140914_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lates_work',
            name='name',
        ),
        migrations.DeleteModel(
            name='lates_work',
        ),
        migrations.CreateModel(
            name='latest_work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latest_grade', models.CharField(default=b'---', max_length=25)),
                ('name', models.OneToOneField(to='grades_a.student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

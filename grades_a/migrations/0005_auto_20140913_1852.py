# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0004_auto_20140912_2030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manufacter',
            new_name='Student',
        ),
        migrations.RemoveField(
            model_name='car',
            name='manufacter',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.IntegerField(default=0)),
                ('manufacter', models.ForeignKey(to='grades_a.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

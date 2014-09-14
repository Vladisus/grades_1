# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0002_auto_20140912_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='student',
        ),
        migrations.DeleteModel(
            name='Grades',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='car',
            name='manufacter',
            field=models.ForeignKey(to='grades_a.Manufacter'),
            preserve_default=True,
        ),
    ]

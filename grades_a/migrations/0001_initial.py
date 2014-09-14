# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_field', models.TextField(max_length=100)),
                ('grades', models.TextField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

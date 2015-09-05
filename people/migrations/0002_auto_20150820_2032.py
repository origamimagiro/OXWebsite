# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='major',
            field=models.CharField(default='undecided', blank=True, max_length=20),
        ),
    ]

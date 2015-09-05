# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20150825_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='class_year',
            field=models.IntegerField(blank=True, default=1920),
            preserve_default=False,
        ),
    ]

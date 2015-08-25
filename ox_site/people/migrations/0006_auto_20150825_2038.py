# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20150825_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='class_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='brother',
            name='image',
            field=models.ImageField(default='/media//coatarms.jpg', upload_to=''),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20150820_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='brother',
            name='image',
            field=models.ImageField(default='images/coatarms.jpg', upload_to='images/brothers'),
        ),
    ]

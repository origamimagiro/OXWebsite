# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20150825_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='image',
            field=models.ImageField(default='/media//coatarms.jpg', upload_to='/Users/henryaspegren/Documents/Projects/OXWebsite/ox_site/media/'),
        ),
    ]

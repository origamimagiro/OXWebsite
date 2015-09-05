# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_brother_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='image',
            field=models.ImageField(upload_to='/media/', default='/media//coatarms.jpg'),
        ),
    ]

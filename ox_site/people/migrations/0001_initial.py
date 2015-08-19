# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brother',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_year', models.IntegerField(blank=True)),
                ('major', models.CommaSeparatedIntegerField(blank=True, null=True, max_length=20)),
                ('hometown', models.CharField(blank=True, max_length=100)),
                ('about', models.CharField(blank=True, max_length=500)),
                ('campus_involvement', models.CharField(blank=True, max_length=500)),
                ('is_alum', models.BooleanField(default=False)),
                ('big_brother', models.ManyToManyField(blank=True, related_name='big_brother_rel_+', to='people.Brother')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

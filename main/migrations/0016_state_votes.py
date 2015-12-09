# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20151106_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='votes',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20151106_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
        ),
    ]

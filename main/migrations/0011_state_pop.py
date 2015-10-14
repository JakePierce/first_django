# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_city_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='pop',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]

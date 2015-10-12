# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151007_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151106_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='downvotes_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='state',
            name='upvotes_count',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

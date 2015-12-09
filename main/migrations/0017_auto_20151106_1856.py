# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_state_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='downvotes_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='upvotes_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]

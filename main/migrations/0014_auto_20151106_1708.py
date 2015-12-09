# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_auto_20151012_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=255, null=True, blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='downvotes',
            field=models.ManyToManyField(related_name='down_votes', to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='state',
            name='upvotes',
            field=models.ManyToManyField(related_name='up_votes', to='main.UserProfile'),
        ),
    ]

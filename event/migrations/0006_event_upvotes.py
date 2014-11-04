# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='upvotes',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
    ]

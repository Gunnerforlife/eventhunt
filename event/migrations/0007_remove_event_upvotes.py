# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_event_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='upvotes',
        ),
    ]

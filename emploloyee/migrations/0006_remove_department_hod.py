# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emploloyee', '0005_auto_20151112_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='hod',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emploloyee', '0002_auto_20151111_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeleave',
            name='employee',
        ),
        migrations.DeleteModel(
            name='EmployeeLeave',
        ),
    ]

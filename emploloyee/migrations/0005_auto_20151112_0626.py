# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emploloyee', '0004_auto_20151112_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(verbose_name='Joined On', auto_now_add=True, null=True),
        ),
    ]

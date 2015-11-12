# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emploloyee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='hod',
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='employee',
            field=models.ForeignKey(to='emploloyee.Employee'),
        ),
    ]

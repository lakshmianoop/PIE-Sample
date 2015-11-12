# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('emploloyee', '0003_auto_20151111_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='hod',
            field=models.ForeignKey(null=True, to='emploloyee.Employee', related_name='hods', help_text='Head of the Department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Joined On'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, to='emploloyee.Employee', help_text='Manager'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]

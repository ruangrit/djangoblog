# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogengin', '0004_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='id',
        ),
        migrations.AddField(
            model_name='catagory',
            name='cid',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]

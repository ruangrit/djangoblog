# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogengin', '0005_auto_20140918_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cid',
            field=models.ForeignKey(default=1, to='blogengin.Catagory'),
            preserve_default=False,
        ),
    ]

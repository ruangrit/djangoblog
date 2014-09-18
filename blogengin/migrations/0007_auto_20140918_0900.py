# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogengin', '0006_post_cid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
    ]

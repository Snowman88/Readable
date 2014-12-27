# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141223_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['pk']},
        ),
    ]

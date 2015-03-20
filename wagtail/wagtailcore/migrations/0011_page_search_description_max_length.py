# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='search_description',
            field=models.CharField(blank=True, max_length=2000)
        ),
    ]

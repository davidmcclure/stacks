# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 21:22
from __future__ import unicode_literals

import corpus.fields.metadata
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0004_add_author_first_last_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='author_name_first',
            field=corpus.fields.metadata.MetadataField(null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='author_name_full',
            field=corpus.fields.metadata.MetadataField(null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='author_name_last',
            field=corpus.fields.metadata.MetadataField(null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='plain_text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=corpus.fields.metadata.MetadataField(),
        ),
    ]
# Generated by Django 5.0.8 on 2024-08-20 10:18

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='library_boo_search__4f5e04_gin'),
        ),
    ]

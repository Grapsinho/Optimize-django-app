# Generated by Django 5.0.8 on 2024-08-20 09:59

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('average_rating', models.FloatField()),
                ('isbn', models.CharField(max_length=13)),
                ('isbn13', models.CharField(max_length=13)),
                ('language_code', models.CharField(max_length=10)),
                ('num_pages', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('text_reviews_count', models.IntegerField()),
                ('publisher', models.CharField(max_length=255)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
            ],
            options={
                'indexes': [django.contrib.postgres.indexes.GinIndex(fields=['title'], name='GinIndexForTitle', opclasses=['gin_trgm_ops']), django.contrib.postgres.indexes.GinIndex(fields=['authors'], name='GinIndexForAuthors', opclasses=['gin_trgm_ops'])],
            },
        ),
    ]

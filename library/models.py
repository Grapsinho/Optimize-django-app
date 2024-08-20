from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    authors = models.CharField(max_length=255)
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=13)
    isbn13 = models.CharField(max_length=13)
    language_code = models.CharField(max_length=10)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publisher = models.CharField(max_length=255)
    search_vector = SearchVectorField(null=True)


    class Meta:
        indexes = [
            GinIndex(name='GinIndexForTitle', fields=['title'], opclasses=['gin_trgm_ops']),
            GinIndex(name='GinIndexForAuthors', fields=['authors'], opclasses=['gin_trgm_ops']),
            GinIndex(fields=['search_vector']),
        ]

    def __str__(self):
        return self.title

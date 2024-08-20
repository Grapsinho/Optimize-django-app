from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector
from library.models import Book

@receiver(post_save, sender=Book)
def update_search_vector(sender, instance, **kwargs):
    instance.search_vector = SearchVector('title', 'authors')
    instance.save(update_fields=['search_vector'])

from django.core.management.base import BaseCommand
from library.models import Book
from django.contrib.postgres.search import SearchVector

class Command(BaseCommand):
    help = 'Update search vector fields for all books in batches.'

    def handle(self, *args, **kwargs):
        batch_size = 500
        total_records = Book.objects.count()

        for start in range(0, total_records, batch_size):
            end = start + batch_size
            books = Book.objects.all()[start:end]
            for book in books:
                book.search_vector = SearchVector('title', 'authors')
                book.save(update_fields=['search_vector'])
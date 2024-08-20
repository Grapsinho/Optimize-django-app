from django.core.cache import cache
from library.models import Book
import json


def get_paginated_books(page_number, page_size):
    cache_key = f'paginated_books_page_{page_number}'
    cached_books = cache.get(cache_key)
    
    if not cached_books:
        start = (page_number - 1) * page_size
        end = start + page_size
        
        # Fetch book objects and serialize them
        books_query = Book.objects.all()[start:end]
        cached_books = [
            {
                'id': book.id,
                'title': book.title,
                'author': book.authors,  # Adjust this as per your model fields
                'average_rating': book.average_rating,
            }
            for book in books_query
        ]
        
        # Store serialized book data in Redis
        cache.set(cache_key, json.dumps(cached_books), timeout=300)  # Cache for 5 minutes
    else:
        # Deserialize the cached data
        cached_books = json.loads(cached_books)

    # Convert the cached data back to a list of book-like objects
    return cached_books
from rest_framework import generics
from library.models import Book
from .serializers import BookSerializer

from django.contrib.postgres.search import SearchQuery

from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500

# just a api that get's me all the book object
class BookView(generics.ListAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

# and this is for searching
class BookSearchView(generics.ListAPIView):
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            search_query = SearchQuery(query)
            queryset = Book.objects.filter(
                title__search=search_query
            ).order_by('-id').only('title', 'authors')
            return queryset
        return Book.objects.none()


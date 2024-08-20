from typing import Any

from .models import Book
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class Home(TemplateView):
    template_name = 'library/home.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        # i = 1

        # Book.objects.create(
        #     title=f"Book {i}23222",
        #     authors=f"Author {i}22231",
        #     average_rating=round(2.0 + i * 0.01, 2),
        #     isbn=f"{10 + i:010d}",
        #     isbn13=f"9743534",
        #     language_code="eng",
        #     num_pages=200 + i % 100,
        #     ratings_count=i % 50,
        #     text_reviews_count=i % 20,
        #     publisher="Test Publisher"
        # )

        context['books'] = Book.objects.get(id=1)
        return context
    
from django.shortcuts import get_object_or_404
    
class OtherPage(DetailView):
    model = Book
    template_name = 'library/other.html'
    context_object_name = 'item'

    def get_object(self, queryset=None):
        item_id = self.kwargs.get('id')
        return get_object_or_404(Book, id=item_id)
    

from django.core.cache import cache
from django.utils.decorators import method_decorator

from django.contrib.postgres.search import SearchQuery

class SomeOtherPage(ListView):
    model = Book
    template_name = 'library/some_other.html'
    context_object_name = 'items'
    paginate_by = 30

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        cache_key = f'books_cache_{query}'
        cached_queryset = cache.get(cache_key)

        if cached_queryset is None:
            queryset = Book.objects.only('title', 'authors', 'id', 'publisher').order_by('-average_rating')
            if query:
                search_query = SearchQuery(query)
                queryset = queryset.filter(title__search=search_query)

            cache.set(cache_key, list(queryset), timeout=300)
        else:
            queryset = cached_queryset

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page = context['page_obj']
        index = page.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 2 if index >= 2 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        context['page_range'] = paginator.page_range[start_index:end_index]

        context['search_term'] = self.request.GET.get('search', '')

        return context

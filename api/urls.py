from django.urls import path
from .views import BookSearchView, BookView

urlpatterns = [
    path('books/', BookView.as_view(), name='book'),
    path('books/search/', BookSearchView.as_view(), name='book_search'),
]
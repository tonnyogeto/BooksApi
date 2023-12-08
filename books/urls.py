from django.urls import path
from .views import create_book, get_books

urlpatterns = [
    path('get-books/', get_books),
    path('create-book/', create_book),
]

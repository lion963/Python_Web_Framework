from django.urls import path

from django_rest.books_api.views import ListBooksView, DetailBookView

urlpatterns = [
    path('books', ListBooksView.as_view(), name='list books'),
    path('books/<int:pk>', DetailBookView.as_view(), name='detail book')
]
from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/list/', views.books_list, name='books_list'),
    path('books/register/', views.books_register, name='books_register'),
    path('authors/list/', views.authors_list, name='authors_list'),
    path('<int:id>/books/', views.author_books, name='author_books'),
]
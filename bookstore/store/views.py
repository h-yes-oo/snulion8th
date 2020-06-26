from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from .models import Author, Book

# Create your views here.
def index(request):
    return render(request, 'store/index.html')


def books_list(request):
    books = Book.objects.all()
    return render(request, 'store/book-list.html', {'books': books})


def books_register(request):
    if request.method == 'POST':
        title = request.POST['title']
        published_year = request.POST['published_year']
        stock = request.POST['stock']

        try:
            author = Author.objects.get(name = request.POST['author'])
        except Author.DoesNotExist:
            author = Author.objects.create(name = request.POST['author'])
        Book.objects.create(title = title, author = author, published_year = published_year, stock = stock)
        return redirect('/store/')
    
    return render(request, 'store/book-register.html')


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'store/authors-list.html', {'authors': authors})


def author_books(request, id):
    books = Book.objects.filter(author = id)
    return render(request, 'store/author-books.html', {'books': books})
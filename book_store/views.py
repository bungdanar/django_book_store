from django.shortcuts import render
from django.http import HttpRequest, Http404

from .models import Book


def index(request: HttpRequest):
    books = Book.objects.all()
    return render(request, "book_store/index.html", {
        "books": books
    })


def book_detail(request: HttpRequest, id: int):
    try:
        book: Book = Book.objects.get(pk=id)
        return render(request, "book_store/book_detail.html", {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestselling": book.is_bestselling
        })
    except:
        raise Http404()

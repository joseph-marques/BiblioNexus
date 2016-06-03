from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from data.models import Book
# Create your views here.
def index(request):
    get_books = Book.objects.order_by("title")
    context = {
        'books_to_display': get_books,
    }
    return render(request, 'browse/index.html', context)

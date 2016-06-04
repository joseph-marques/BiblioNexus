from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from data.models import Book

def index(request, book_id):
    book=get_object_or_404(Book, pk=book_id)
    return render(request, 'read/index.html', {'book': book})

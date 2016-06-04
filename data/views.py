from django.shortcuts import render
from .models import Series, Book, Author
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("data shit")

#literally copied off of starting tutorial.  trying to get list of books by title show
def sort_by_book(request):
    book_list = Book.objects.filter(Book.title)
    context = {'book':Book.title}
    return render(request, 'data/sort_by_book.html',context)
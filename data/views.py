from django.shortcuts import render, get_object_or_404
from .models import Series, Book, Author
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def add(request):
    return render(request, 'data/add.html')


def edit(request, book_id):
    book=get_object_or_404(Book, pk=book_id)
    return render(request, 'data/edit.html', {'book': book})



#literally copied off of starting tutorial.  trying to get list of books by title show
#def sort_by_book(request):
#    book_list = Book.objects.filter(Book.title)
#    template = loader.get_template('templates/data/index.html')
#    context = {'book': Book.title}
#    return render(request, 'data/sort_by_book.html', context)

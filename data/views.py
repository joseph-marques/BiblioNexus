from django.shortcuts import render, get_object_or_404
from .models import Series, Book, Author, BookForm
from django.http import HttpResponse
from django.template import loader
from django.forms import modelformset_factory


# Create your views here.
def add(request):
    BookFormSet = modelformset_factory(Book, fields=('authors', 'title', 'series', 'seriesSpot', 'publish_date'))
    if request.method == 'POST':
        formset = BookFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render(request, 'data/edit.html', {'formset': formset})
            # do something.
    else:
        #formset = BookFormSet(queryset=Book.objects.none())
        formset = BookForm()
        return render(request, 'data/add.html', {'formset': formset})




def edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'data/edit.html', {'book': book})



#literally copied off of starting tutorial.  trying to get list of books by title show
#def sort_by_book(request):
#    book_list = Book.objects.filter(Book.title)
#    template = loader.get_template('templates/data/index.html')
#    context = {'book': Book.title}
#    return render(request, 'data/sort_by_book.html', context)

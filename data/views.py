from django.forms import TextInput
from django.shortcuts import render, get_object_or_404, redirect
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
            next = request.GET.get('from', None)
            if next:
                return redirect(next)
        return HttpResponse("<H1>INVALID</H1><br/><FORM><INPUT Type='button' VALUE='Back' onClick='history.go(-1);return true;'></FORM>")
            # do something.
    else:
        #formset = BookFormSet(queryset=Book.objects.none())
        formset = BookForm()
    return render(request, 'data/add.html', {'formset': formset})

def author(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name',), widgets={'name': TextInput(attrs={'class': 'form-control com-md-10',  'required' : True}),})
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            next = request.GET.get('from', None)
            if next:
                return redirect(next)
        return HttpResponse("<H1>INVALID</H1><br/><FORM><INPUT Type='button' VALUE='Back' onClick='history.go(-1);return true;'></FORM>")
    else:
        formset = AuthorFormSet(queryset=Author.objects.none())
    return render(request, 'data/author.html', {'formset': formset})

def series(request):
    SeriesFormSet = modelformset_factory(Series, fields=('title',), widgets={'title': TextInput(attrs={'class': 'form-control com-md-10',  'required' : True}),})
    if request.method == 'POST':
        formset = SeriesFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            next = request.GET.get('from', None)
            if next:
                return redirect(next)
        return HttpResponse("<H1>INVALID</H1><br/><FORM><INPUT Type='button' VALUE='Back' onClick='history.go(-1);return true;'></FORM>")
    else:
        formset = SeriesFormSet(queryset=Series.objects.none())
    return render(request, 'data/Series.html', {'formset': formset})


def edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'data/edit.html', {'book': book})



#literally copied off of starting tutorial.  trying to get list of books by title show
#def sort_by_book(request):
#    book_list = Book.objects.filter(Book.title)
#    template = loader.get_template('templates/data/index.html')
#    context = {'book': Book.title}
#    return render(request, 'data/sort_by_book.html', context)

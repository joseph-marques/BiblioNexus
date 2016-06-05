from django.forms import TextInput, SelectMultiple
from django.shortcuts import render, get_object_or_404, redirect
from .models import Series, Book, Author, BookForm, f
from django.http import HttpResponse
from django.template import loader
from django.forms import modelformset_factory
from django import forms
from django.core.files import File



# Create your views here.
def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            next = request.GET.get('from', None)
            if next:
                return redirect(next)
            else:
                return redirect("/")
        return HttpResponse("<H1>INVALID DATA, PLEASE TRY AGAIN.</H1><br/><FORM><INPUT Type='button' VALUE='Back' onClick='history.go(-1);return true;'></FORM>")
    else:
        form = BookForm()
    return render(request, 'data/add.html', {'formset': form, })

def author(request):
    authorFormSet = modelformset_factory(Author, fields=('name',), widgets={'name': TextInput(attrs={'class': 'form-control com-md-10',  'required' : True}),})
    if request.method == 'POST':
        formset = authorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            next = request.GET.get('from', None)
            if next:
                return redirect(next)
            else:
                return redirect("/")
        return HttpResponse("<H1>INVALID DATA, PLEASE TRY AGAIN.</H1><br/><FORM><INPUT Type='button' VALUE='Back' onClick='history.go(-1);return true;'></FORM>")
    else:
        formset = authorFormSet(queryset=Author.objects.none())
    return render(request, 'data/author.html', {'formset': formset})

def series(request):
    seriesFormSet = modelformset_factory(Series, fields=('title', 'authors',), widgets={'title': TextInput(attrs={'class': 'form-control com-md-10',  'required': True}), 'authors': SelectMultiple(attrs={'class': 'form-control col-md-10'}), })
    if request.method == 'POST':
        formset = seriesFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            next = request.GET.get('from', None)
            if next:
                return redirect(next)
            else:
                return redirect("/")
        return HttpResponse("<H1>INVALID DATA, PLEASE TRY AGAIN.</H1><br/><FORM><INPUT Type='button' VALUE='Back' onClick='history.go(-1);return true;'></FORM>")
    else:
        formset = seriesFormSet(queryset=Series.objects.none())
    return render(request, 'data/series.html', {'formset': formset})


def edit(request, book_id):
    if request.method == 'POST':
        data=get_object_or_404(Book, id=book_id)
        form = BookForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            obj = form.save()
            next = request.GET.get('from', None)
            if next:
                return redirect(next)
            else:
                return redirect("/")
        return HttpResponse("<H1>INVALID DATA, PLEASE TRY AGAIN.</H1><br/><FORM><INPUT Type='button' VALUE='Back' onClick='history.go(-1);return true;'></FORM>")
    else:
        data=get_object_or_404(Book, id=book_id)
        form=BookForm(instance=data)

    return render(request, 'data/add.html', {'formset': form, })



#literally copied off of starting tutorial.  trying to get list of books by title show
#def sort_by_book(request):
#    book_list = Book.objects.filter(Book.title)
#    template = loader.get_template('templates/data/index.html')
#    context = {'book': Book.title}
#    return render(request, 'data/sort_by_book.html', context)

from django.forms import *
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128, unique=True) #The name of the author

    def __str__(self):
        return self.name

class Series(models.Model):
    title = models.CharField(max_length=512, unique=True) #the title of the series
    authors = models.ManyToManyField(Author) #the authors that participated in the making of the series

    def __str__(self):
        return self.title + " by "+" and ".join(str(x) for x in self.authors.all())


class Book(models.Model):
    title = models.CharField(max_length=512) #the title of the book
    authors = models.ManyToManyField(Author) #describes the author (or authors) of the book
    series = models.ForeignKey(Series, null=True, blank=True) #describes what series the book is in, if at all.  will be null if not there
    seriesSpot = models.IntegerField(default=0) #describes which book in the series this is, if 0, no series
    publish_date = models.DateField() #states the date that the book was published


    def __str__(self):
        return self.title + " by "+" and ".join(str(x) for x in self.authors.all())

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['authors', 'title', 'series', 'seriesSpot', 'publish_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control col-md-10'}),
            'publish_date': TextInput(attrs={'class': 'form-control com-md-10',  'required' : False}),
            'authors': SelectMultiple(attrs={'class': 'form-control col-md-10'}),
            'series': Select(attrs={'class': 'form-control col-md-10'}),
            'seriesSpot': TextInput(attrs={'class': 'form-control col-md-10'}),
        }

class Shelf(modles.Model):
    title = models.CharField(max_length=512)
    books = moels.ManyToManyField(Book)
    creation_date = models.DateField()
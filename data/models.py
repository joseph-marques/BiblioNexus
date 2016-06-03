from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128) #The name of the author


class Series(models.Model):
    title = models.CharField(max_length=512) #the title of the series
    authors = models.ManyToManyField(Author) #the authors that participated in the making of the series
    books = [] #the list of books that are in the series
    def AddBook(Book(x)): #a method to get books into the series list
        books.append(x)


class Book(models.Model):
    title = models.CharField(max_length=512) #the title of the book
    authors = models.ManyToManyField(Author) #describes the author (or authors) of the book
    series = models.ForeignKey(Series) #describes what series the book is in, if at all.  will be null if not there
    seriesSpot = models.IntegerField() #describes which book in the series this is, if 0, no series
    publish_date = models.DateField() #states the date that the book was published


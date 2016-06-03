from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)


class Series(models.Model):
    title = models.CharField(max_length=512)
    authors = models.ManyToManyField(Author)
    books = []
    def AddBook(Book(x)):
        books.append(x)


class Book(models.Model):
    title = models.CharField(max_length=512)
    authors = models.ManyToManyField(Author)
    series = models.ForeignKey(Series)
    seriesSpot = models.IntegerField()
    publish_date = models.DateField()


from django.contrib import admin

# Register your models here.
from .models import Author, Book, Series

admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Book)
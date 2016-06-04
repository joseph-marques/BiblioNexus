from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.add, name='add'),
    url(r'^(?P<book_id>[0-9]+)', views.edit, name='edit'),
]
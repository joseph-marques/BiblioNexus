from django.conf.urls import url

from . import views
app_name='data'
urlpatterns = [
    url(r'^$', views.add, name='add'),
    url(r'^(?P<book_id>[0-9]+)', views.edit, name='edit'),
]
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', homepage, name='homepage' ),
    url(r'^new_book/$', add_book, name='add_book'),
    url(r'^new_category/$', add_category, name='add_category'),
    url(r'^book/(?P<id>\d+)/$', book_detail_view, name='book_detail'),
    url(r'^search/$', search_by_title, name='search')
]
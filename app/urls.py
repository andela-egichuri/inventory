from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', homepage, name='homepage' ),
    url(r'^new_book/$', add_book, name='add_book'),
    url(r'^new_category/$', add_category, name='add_category')

]
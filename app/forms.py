from django.forms import ModelForm
from .models import *


class BookForm(ModelForm):
    """ Define form fields for Book books"""
    class Meta:
        model = Book
        fields = ['title', 'description', 'category']


class CategoryForm(ModelForm):
    """ Define form fields for the Categories"""

    class Meta(ModelForm):
        model = Category
        fields = ('name', )
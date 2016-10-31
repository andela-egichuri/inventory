from django.forms import ModelForm, Textarea, TextInput, Select
from .models import *  
        
class BookForm(ModelForm):
    """ Define form fields for Book books"""

    class Meta:
        model = Book
        fields = ['title', 'description', 'category']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
        }


class CategoryForm(ModelForm):
    """ Define form fields for the Categories"""

    class Meta(ModelForm):
        model = Category
        fields = ('name', )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'})
        }
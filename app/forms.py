from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import *  
        
class BookForm(ModelForm):
    """ Define form fields for Book books"""
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'

    class Meta:
        model = Book
        fields = ['title', 'description', 'category']


class CategoryForm(ModelForm):
    """ Define form fields for the Categories"""

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'

    class Meta(ModelForm):
        model = Category
        fields = ('name', )
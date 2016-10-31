from django.shortcuts import render
from .forms import BookForm, CategoryForm
from .models import *

def homepage(request):
    """ Function based view for the home page

    User can add book from front end
    """
    content = {}
    content['all_books'] = Book.objects.all()
    return render(request, 'index.html', content)


def add_book(request):
    """ View to render form page"""
    content = {}
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
    content['new_book_form'] = form
    return render(request, 'new_book.html', content)


def add_category(request):
    """ View to render form page"""
    content = {}
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save()
    content['new_category_form'] = form
    return render(request, 'new_category.html', content)

def book_detail_view(request, id):
    """ Book details view """
    current_book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'current_book': current_book})

def search_by_title(request):
    content = {}
    if request.method == 'POST':
        search_results = Book.objects.filter(title__icontains=request.POST.get('search_term')) 
        if search_results:
            content['search_results'] = search_results
    return render(request, 'search_results.html', content)
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    """ Books Category"""
    name = models.CharField(max_length=120)
        
class Book(models.Model):
    """ Book Model.
            Defines fields for the books
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'name', 'author', 'language', 'ano', 'publishing_house', 'category', 'comments']

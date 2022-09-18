from django import forms
from .models import Book
from django.conf import settings

class BookForm(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Book
        fields = ['name', 'pages']
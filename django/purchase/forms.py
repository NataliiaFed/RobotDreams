from django import forms
from .models import Purchase
from user.models import User
from book.models import Book


class PurchaseForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    book = forms.ModelChoiceField(queryset=Book.objects.all())

    class Meta:
        model = Purchase
        fields = ('user', 'book', )
from django import forms
from .models import Book, PublishingHouse


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    publish_house = forms.ModelChoiceField(queryset=PublishingHouse.objects.all())

    class Meta:
            model = Book
            fields = ('title', 'author', 'year', 'price', 'publish_house', )
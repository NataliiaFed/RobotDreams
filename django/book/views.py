from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
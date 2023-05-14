from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Book
from .forms import BookForm
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from rest_framework import filters

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['title', 'author',]
    ordering_fields = ['id']
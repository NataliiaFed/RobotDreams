from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def my_view(response):
    res = Book.objects.all().values()
    return HttpResponse(res)
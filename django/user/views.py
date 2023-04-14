from django.shortcuts import render
from django.http import HttpResponse

def my_view(response):
    return HttpResponse('Hello, users!')
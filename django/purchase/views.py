from django.shortcuts import render
from django.http import HttpResponse
from .models import Purchase

def my_view(response):
    res = Purchase.objects.all().order_by('-date').values()
    return HttpResponse(res)
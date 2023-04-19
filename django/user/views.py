from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def my_view(response):
    res = User.objects.all().values()
    return HttpResponse(res)
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import User
from .forms import UserForm

class UserListView(ListView):
    model = User

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
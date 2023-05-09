from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import User
from .forms import UserForm
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class UserListView(ListView):
    model = User

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    model = User
    form_class = UserForm

class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['first_name', 'last_name',]
    ordering_fields = ['id']

    pagination_class = CustomPaginator
    max_page_size = 10
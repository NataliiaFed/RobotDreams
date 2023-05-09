from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Purchase
from .forms import PurchaseForm
from rest_framework.viewsets import ModelViewSet
from .serializers import PurchaseSerializer
from rest_framework import filters

class PurchaseListView(ListView):
    model = Purchase

class PurchaseDetailView(DetailView):
    model = Purchase

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['user', 'book',]
    ordering_fields = ['id']
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Purchase
from .forms import PurchaseForm

class PurchaseListView(ListView):
    model = Purchase

class PurchaseDetailView(DetailView):
    model = Purchase

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
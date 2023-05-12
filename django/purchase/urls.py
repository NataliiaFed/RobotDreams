from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView

urlpatterns = [
    path('list', PurchaseListView.as_view(), name='purchase-list'),
    path('detail/<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('create', PurchaseCreateView.as_view(), name='purchase-create'),
]
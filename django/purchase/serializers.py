from rest_framework import serializers
from .models import Purchase
from user.serializers import UserSerializer
from book.serializers import BookSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    user = UserSerializer
    book = BookSerializer(many=True)
    date = serializers.ReadOnlyField()

    class Meta:
        model = Purchase
        fields = '__all__'
from django.contrib import admin
from .models import Book, PublishingHouse

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass
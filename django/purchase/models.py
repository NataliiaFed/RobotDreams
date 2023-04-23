from django.db import models
from user.models import User
from book.models import Book


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase'
        
    def __str__(self):
        return f"{self.id}: {self.user.first_name} {self.user.last_name} - {self.book.title}"
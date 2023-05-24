from django.db import models
from django.urls import reverse

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name} ({self.age})"

    def get_absolute_url(self):
        return reverse('user-detail', args=[self.id])
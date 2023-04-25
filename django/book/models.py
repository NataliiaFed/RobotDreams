from django.db import models


class PublishingHouse(models.Model):
    name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(default=5)

    class Meta:
        db_table = 'publishing_house'

    def __str__(self):
        return f"{self.id}: {self.name} ({self.rating})"


class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255)
    year = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    publish_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')
    
    def __str__(self):
        return f'{self.id}: "{self.title}" {self.author} {self.year} {self.publish_house.name} - {self.price}'
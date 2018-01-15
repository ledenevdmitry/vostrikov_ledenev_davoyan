from django.db import models
from django.utils import timezone

class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=30)
    #вес в граммах
    weight = models.IntegerField(max_length=5)
    published_date = models.DateTimeField(default=timezone.now())
    id = models.IntegerField(primary_key=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

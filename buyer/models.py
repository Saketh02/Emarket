from django.db import models
from seller.models import product

# Create your models here.
class cart(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

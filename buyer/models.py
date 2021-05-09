from django.db import models
from seller.models import product


# Create your models here.
class cart(models.Model):
    customer = models.ForeignKey('account.account', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField()

class cartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)

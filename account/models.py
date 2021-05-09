from django.db import models

# Create your models here.
from django.db import models
from buyer.models import cart


# Create your models here.
class account(models.Model):
    user_name = models.CharField(max_length=100)
    mobileNumber = models.CharField(
        max_length=20,
        default=None,
        unique=True,
    )
    isActive = models.BooleanField(default=True)
    isCustomer = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)
    address = models.CharField(max_length=300)


class session(models.Model):
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(blank=True, null=True)
    isExpired = models.BooleanField(default=False)
    authToken = models.CharField(max_length=100, unique=True)


class order(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    order_total = models.FloatField()

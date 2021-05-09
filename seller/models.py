from django.db import models

# Create your models here.
class store(models.Model):
    store_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    seller = models.ForeignKey("account.account", on_delete=models.CASCADE)
    link = models.CharField(max_length=400, default="")


class category(models.Model):
    category_name = models.CharField(max_length=100)
    store = models.ForeignKey(store, on_delete=models.CASCADE)


class product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    MRP = models.FloatField()
    selling_price = models.FloatField()
    image = models.BinaryField(blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

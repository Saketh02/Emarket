from django.contrib import admin
from .models import store,category,product
# Register your models here.
admin.site.register(store)
admin.site.register(category)
admin.site.register(product)
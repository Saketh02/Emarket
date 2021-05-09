from django.contrib import admin
from .models import account, session, order

# Register your models here.
admin.site.register(account)
admin.site.register(session)
admin.site.register(order)
from django.urls import path
from seller import views
urlpatterns = [
    path('check/',views.check,name='seller-check')
]

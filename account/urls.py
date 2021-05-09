from django.urls import path
from account import views
from account import apis

urlpatterns = [
    path("", views.check, name="homepage"),
    
]

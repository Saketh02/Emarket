from django.urls import path
from buyer import views
urlpatterns = [
    path('check/',views.check,name='check')
]

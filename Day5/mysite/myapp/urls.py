from .views import greet
from django.urls import path

urlpatterns = [
    path('',greet)
]
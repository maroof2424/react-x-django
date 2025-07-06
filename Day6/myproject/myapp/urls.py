from django.urls import path
from .views  import orm_view

urlpatterns = [
    path('',orm_view)
]

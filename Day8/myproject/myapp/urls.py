from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
]

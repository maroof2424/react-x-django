from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_create, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
]

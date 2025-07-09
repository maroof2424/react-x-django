from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),  # FBV
    path('products/<int:pk>/', views.product_detail),  # FBV
    # path('products/', views.ProductList.as_view()),  # CBV
]

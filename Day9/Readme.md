# Day 9

### ✅ Part 1: Installation

### ✅ Part 2: Serializers

### ✅ Part 3: Views (Function-based and Class-based)

---

## ✅ Part 1: DRF Installation

### 📦 Step 1: Install DRF

```bash
pip install djangorestframework
```

### ⚙️ Step 2: Add `'rest_framework'` to `INSTALLED_APPS`

In your Django `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### 🚀 Step 3: Create App (if you haven’t)

```bash
python manage.py startapp api
```

---

## ✅ Part 2: Serializers

### 🔸 What is a Serializer?

Serializers convert Django model instances to JSON (and back).

### 🧱 Example Model (`models.py`)

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

### 🧰 Create a Serializer (`serializers.py`)

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # or list like ['id', 'name', 'price']
```

---

## ✅ Part 3: Views

### Option 1: 📌 **Function-Based Views (FBV)**

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
```

```python
@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data)
```

---

### Option 2: 📦 **Class-Based Views (CBV)** using `APIView`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
```

---

### Option 3: 🚀 **Generic Views / ViewSets**

```python
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

## ✅ Step 4: URLs

### In your `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),  # FBV
    path('products/<int:pk>/', views.product_detail),  # FBV
    # path('products/', views.ProductList.as_view()),  # CBV
]
```

---

## ✅ Bonus: Use Postman or DRF’s built-in API browser

Run:

```bash
python manage.py runserver
```

Visit:
`http://127.0.0.1:8000/products/` – You'll see JSON!


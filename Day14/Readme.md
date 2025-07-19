# Day14

### 🔹 Step 1: Install & Setup

📦 Install Django & DRF:

```bash
pip install django djangorestframework
```

🛠 Create your project and app:

```bash
django-admin startproject myapi
cd myapi
python manage.py startapp products
```

🔧 Add to `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'products',  # your app name
]
```

---

### 🔹 Step 2: Create Product Model

📄 `products/models.py`

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

⚙ Migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🔹 Step 3: Create Serializer

📄 `products/serializers.py`

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

---

### 🔹 Step 4: Create Views (CRUD)

📄 `products/views.py`

```python
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# GET (List) & POST (Create)
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# GET (Retrieve), PUT (Update), DELETE
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

### 🔹 Step 5: Setup URLs

📄 `products/urls.py`

```python
from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]
```

📄 `myapi/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),  # your app's API
]
```

---

### 🔹 Step 6: Run Server

```bash
python manage.py runserver
```

Then visit:
`http://127.0.0.1:8000/api/products/`
You’ll see the browsable API!

---

### 🔹 Step 7: Test APIs

Use Postman or browser to:

| Method | URL                | Action         |
| ------ | ------------------ | -------------- |
| GET    | `/api/products/`   | List products  |
| POST   | `/api/products/`   | Create product |
| GET    | `/api/products/1/` | Retrieve       |
| PUT    | `/api/products/1/` | Update         |
| DELETE | `/api/products/1/` | Delete         |


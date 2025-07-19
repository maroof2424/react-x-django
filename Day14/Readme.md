# **Day 14 (Jul 14)**

* Product Model
* Serializer
* Views (APIView or ViewSet)
* URLs
* Image support (MEDIA setup)
* CORS config

---

## ✅ **1. `models.py` – Product Model**

```python
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

## ✅ **2. `serializers.py` – Product Serializer**

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

---

## ✅ **3. `views.py` – Product API Views**

Using **DRF ViewSets** (recommended for CRUD).

```python
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
```

---

## ✅ **4. `urls.py` – API Routing**

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
]
```

Also in your **project-level `urls.py`**, don’t forget:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('your_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ✅ **5. `settings.py` – Media & CORS Setup**

```python
# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CORS
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
CORS_ALLOW_ALL_ORIGINS = True  # or specify allowed origins
```

---

## ✅ **6. `admin.py` – Register Model**

```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

---

## ✅ **7. Testing with Postman**

### Sample Endpoints:

* `GET /api/products/` → list all products
* `POST /api/products/` → create new product (with image using `multipart/form-data`)
* `GET /api/products/<id>/` → retrieve product
* `PUT /api/products/<id>/` → update
* `DELETE /api/products/<id>/` → delete

To upload images, make sure you use **`multipart/form-data`** and test with an image file in Postman under "Body" > form-data.

---

## 🛠 Command Checklist

```bash
# Run these in your terminal
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🎉 Done!

You now have a fully working **Product API with image support** using **Django REST Framework**, ready to connect with React in Week 4.

Let me know if you'd like:

* Token Auth or JWT added here
* Sample React fetch for testing this API
* Or Docker setup for full-stack later


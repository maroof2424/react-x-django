## Day7

## 🔷 1. **Django Models**

**Models** are Python classes that define the structure of your database.

### 📌 Basic Example:

```python
# myapp/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

### 📘 Common Field Types:

| Field             | Description                        |
| ----------------- | ---------------------------------- |
| `CharField`       | Short text (must set `max_length`) |
| `TextField`       | Long text                          |
| `IntegerField`    | Whole numbers                      |
| `DecimalField`    | For prices/money                   |
| `BooleanField`    | True/False                         |
| `DateTimeField`   | Date and Time                      |
| `ImageField`      | For images (requires Pillow lib)   |
| `ForeignKey`      | Many-to-one relationship           |
| `ManyToManyField` | Many-to-many relationship          |

---

## 🔷 2. **Django ORM (Object-Relational Mapping)**

ORM lets you interact with the database using Python instead of SQL.

### 🧪 CRUD Example Using ORM:

```python
# Create
Product.objects.create(name="Laptop", price=999.99)

# Read
products = Product.objects.all()
product = Product.objects.get(id=1)

# Filter
Product.objects.filter(in_stock=True)
Product.objects.filter(name__icontains='lap')

# Update
product = Product.objects.get(id=1)
product.price = 899.99
product.save()

# Delete
product = Product.objects.get(id=1)
product.delete()
```

### 🛠️ Useful ORM Queries:

| Query         | Example                                  |
| ------------- | ---------------------------------------- |
| `.all()`      | `Product.objects.all()`                  |
| `.get()`      | `Product.objects.get(id=1)`              |
| `.filter()`   | `Product.objects.filter(price__gte=500)` |
| `.exclude()`  | `Product.objects.exclude(in_stock=True)` |
| `.order_by()` | `Product.objects.order_by('price')`      |
| `.count()`    | `Product.objects.count()`                |

---

## 🔷 3. **Django Admin Panel**

The Django Admin is a built-in interface to manage your models.

### 🧱 Steps:

1. **Register the model**:

```python
# myapp/admin.py
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

2. **Create a Superuser**:

```bash
python manage.py createsuperuser
```

3. **Run the server** and log in:

```bash
python manage.py runserver
# Visit http://127.0.0.1:8000/admin
```

### 🎨 Customizing Admin Display:

```python
# myapp/admin.py
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('in_stock',)

admin.site.register(Product, ProductAdmin)
```

---

## ✅ Final Tips

* Always run `python manage.py makemigrations` + `migrate` after changing models.
* Keep `__str__()` meaningful for better admin readability.
* Use `related_name` in ForeignKey for reverse lookups.
* Explore `ModelForm` for easy form creation based on models.


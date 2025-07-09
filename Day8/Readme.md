# Day 8

## ✅ 1. **Create a Model**

Example: `models.py`

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
```

---

## ✅ 2. **Create a Form**

Example: `forms.py`

```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
```

---

## ✅ 3. **Create Views for Create & Update**

Example: `views.py`

```python
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.contrib import messages

# Create
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')  # change as needed
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

# Update
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')  # change as needed
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})
```

---

## ✅ 4. **Template: `product_form.html`**

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Product Form</title>
</head>
<body>

<h2>Product Form</h2>

{% if messages %}
    <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
    </ul>
{% endif %}

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

</body>
</html>
```

---

## ✅ 5. **URLs**

Example: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
]
```

---

## ✅ 6. **Enable Messages in Settings (Usually default)**

Check in `settings.py`:

```python
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
```

Add `django.contrib.messages` in `INSTALLED_APPS` (already added by default).

And in your base template, make sure `{% for message in messages %}` is supported where needed.

## Day 5

## ✅ **Goal:** Set up a Django project and app, create views, connect URLs.

---

### ⚙️ 1. Create Django Project (10 min)

```bash
pip install django  # install if not yet
django-admin startproject mysite
cd mysite
python manage.py runserver
```

Check: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🧱 2. Create Django App (5 min)

```bash
python manage.py startapp core
```

---

### 🔧 3. Add App to `settings.py` (5 min)

Open `mysite/settings.py`
Add `'core',` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

---

### 🧠 4. Create a View (10 min)

In `core/views.py`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django!")
```

---

### 🌐 5. Set up URLs (15 min)

* In `core/urls.py` (create this file):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

* In `mysite/urls.py`, include the app:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

---

### 🚀 6. Run the Server (5 min)

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### ✅ Output:

You should see `Welcome to Django!` on the homepage.

---

### 🧪 Bonus Practice:

* Make another view like `about()` and route it to `/about/`
* Add basic HTML using `render()` with templates (optional)

---

Want me to give you that bonus practice or template structure too?

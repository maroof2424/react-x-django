## Day 6

## 🔧 1. **Templates** (HTML Files)

Templates are HTML files used to render dynamic content using Django’s **template language**.

### 🔹 Folder Structure:

```
project/
│
├── app/
│   ├── templates/
│   │   └── app/
│   │       └── home.html
```

### 🔹 Example `home.html`

```html
{% extends 'base.html' %}

{% block content %}
<h1>Welcome to My Website</h1>
<p>This is the homepage.</p>
{% endblock %}
```

---

## 🖼️ 2. **Static Files** (CSS, JS, Images)

Static files are CSS, JavaScript, images, fonts etc., used in your site.

### 🔹 Folder Structure:

```
project/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
```

### 🔹 settings.py

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / "static" ]
```

### 🔹 Using Static in Template:

```html
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

---

## 🧱 3. **Base Layout (`base.html`)**

A base layout helps **reuse common design** across pages (e.g., navbars, footers).

### 🔹 Example `base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}My Website{% endblock %}</title>
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <nav>
    <a href="/">Home</a> | <a href="/about/">About</a>
  </nav>

  <main>
    {% block content %}{% endblock %}
  </main>

  <footer>
    <p>&copy; 2025 My Website</p>
  </footer>
</body>
</html>
```

---

## 🔁 Template Inheritance Flow:

* `home.html` ➡️ extends `base.html`
* Uses `block` tags to insert page-specific content
* Static files are included via `{% static %}`

---

## ✅ Summary

| Feature      | Purpose                     | Key Tag / Setting                       |
| ------------ | --------------------------- | --------------------------------------- |
| Templates    | Display dynamic HTML        | `{% extends %}`, `{% block %}`          |
| Static Files | Add design & interactivity  | `{% load static %}`, `STATICFILES_DIRS` |
| Base Layout  | Common layout for all pages | `base.html` with `{% block %}`          |

---


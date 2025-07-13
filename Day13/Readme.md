# Day13

> ❌ `Access to fetch at 'http://localhost:8000/api/...' from origin 'http://localhost:3000' has been blocked by CORS policy...`

---

# ✅ CORS Setup (`django-cors-headers`)

> 📅 For **July 13** in your full-stack roadmap.

---

## ⚙️ 1. **Install `django-cors-headers`**

```bash
pip install django-cors-headers
```

---

## 🧩 2. **Add to `INSTALLED_APPS` in `settings.py`**

```python
INSTALLED_APPS = [
    ...
    'corsheaders',       # ✅ Add this
    'rest_framework',
    'products',          # your app
]
```

---

## 🛡️ 3. **Add Middleware**

Add `'corsheaders.middleware.CorsMiddleware'` **at the top** of your `MIDDLEWARE` list:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ✅ Must be first
    'django.middleware.security.SecurityMiddleware',
    ...
]
```

---

## 🌍 4. **Allow Local React (Frontend) Origin**

Add this to your `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React local dev server
]
```

---

## 🔁 5. **(Optional)** If you want to allow all origins (not safe for production):

```python
CORS_ALLOW_ALL_ORIGINS = True
```

> ✅ Good for testing, but **don’t use in production**!

---

## ✅ 6. Restart Django Server

```bash
python manage.py runserver
```

---

## 🔍 7. Test from React Frontend

Now your frontend should be able to make `GET`, `POST`, `PUT`, `DELETE` requests using Axios or Fetch without CORS errors.

---

## ✅ Example Axios Request (React)

```javascript
import axios from 'axios';

axios.get('http://127.0.0.1:8000/api/products/')
  .then(res => console.log(res.data))
  .catch(err => console.error(err));
```

---

## ✅ Summary Checklist

| ✅ Task                          | Status |
| ------------------------------- | ------ |
| Installed `django-cors-headers` | ✅      |
| Added to `INSTALLED_APPS`       | ✅      |
| Added to `MIDDLEWARE` (on top)  | ✅      |
| Set `CORS_ALLOWED_ORIGINS`      | ✅      |
| Restarted Django server         | ✅      |
| Tested React → Django API       | ✅      |

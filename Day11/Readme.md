### Day 11
---

# ✅ **Test API with Postman & Fix Bugs**

## 🔧 1. **Start Your Django Server**

In terminal:

```bash
python manage.py runserver
```

---

## 🔗 2. **Your API Base URL**

```
http://127.0.0.1:8000/api/products/
```

> Replace `products` if your app or URL path is different.

---

## 📮 3. **Test Endpoints in Postman**

### 🟩 A. **GET All Products**

* **Method:** `GET`
* **URL:** `http://127.0.0.1:8000/api/products/`
* ✅ Expected: List of products

---

### 🟨 B. **POST Create a New Product**

* **Method:** `POST`
* **URL:** `http://127.0.0.1:8000/api/products/`
* **Headers:**
  `Content-Type: application/json`
* **Body (raw, JSON):**

```json
{
  "name": "Dell XPS 13",
  "price": "1399.99",
  "description": "A high-end ultrabook"
}
```

* ✅ Expected: Product is created and returned

---

### 🟦 C. **GET Single Product**

* **Method:** `GET`
* **URL:** `http://127.0.0.1:8000/api/products/1/`

---

### 🟧 D. **PUT (Update Product)**

* **Method:** `PUT`
* **URL:** `http://127.0.0.1:8000/api/products/1/`
* **Headers:**
  `Content-Type: application/json`
* **Body:**

```json
{
  "name": "Dell XPS 13 Updated",
  "price": "1299.99",
  "description": "Updated description"
}
```

* ✅ Expected: Updated product returned

---

### 🟥 E. **DELETE a Product**

* **Method:** `DELETE`
* **URL:** `http://127.0.0.1:8000/api/products/1/`
* ✅ Expected: 204 No Content

---

## 🧪 4. **Fix Common Bugs**

| 🐛 Bug / Error                          | 🛠 Fix                                                            |
| --------------------------------------- | ----------------------------------------------------------------- |
| `415 Unsupported Media Type`            | Set `Content-Type: application/json` in Postman headers           |
| `400 Bad Request`                       | Ensure all required fields are provided, check serializer fields  |
| `404 Not Found`                         | Make sure the object with given `id` exists                       |
| `500 Internal Server Error`             | Check server logs, most likely code typo or model issue           |
| `CSRF Verification Failed` (not in DRF) | Use `@api_view()` to bypass CSRF or test via Postman, not browser |
| `Image not uploading`                   | Wait for Jul 12: media setup + `ImageField` support               |

---

## 🧼 5. **Optional: Improve Response Messages**

```python
# Example for POST success response
return Response({"message": "Product created successfully", "data": serializer.data}, status=201)

# Example for DELETE
return Response({"message": "Product deleted successfully"}, status=204)
```

---

## 📝 6. **Add Debug Info (If Needed)**

```python
import logging
logger = logging.getLogger(__name__)

def product_list_create(request):
    logger.debug("Request Data: %s", request.data)
```

---

## ✅ Final Checklist

| ✅ Task                                         | Status |
| ---------------------------------------------- | ------ |
| Server running (`python manage.py runserver`)  | ✅      |
| API tested in Postman (GET, POST, PUT, DELETE) | ✅      |
| Content-Type header set for JSON requests      | ✅      |
| Bugs fixed (404, 415, 500, validation)         | ✅      |
| Responses readable and clean                   | ✅      |


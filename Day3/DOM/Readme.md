Awesome, Maroof! Let's learn the **DOM (Document Object Model)** — one of the most important things in JavaScript when you're building interactive websites.

---

## 🧠 What is the DOM?

The **DOM** is a tree-like structure created by the browser from your HTML.
With JavaScript, you can use the DOM to:

* ✅ Select elements
* ✅ Change text, HTML, or styles
* ✅ Respond to user actions (like clicks)
* ✅ Add or remove elements

---

## ✅ Basic DOM Actions

### 🔍 1. **Select Elements**

```js
document.getElementById("title");
document.querySelector(".btn");       // selects first match
document.querySelectorAll("p");       // returns all <p> elements
```

---

### ✏️ 2. **Change Text or HTML**

```js
const heading = document.getElementById("title");

heading.innerText = "Welcome Maroof!";    // Only text
heading.innerHTML = "<em>Hi Maroof</em>"; // Can add tags
```

---

### 🎨 3. **Change CSS Styles**

```js
const box = document.querySelector(".box");

box.style.backgroundColor = "yellow";
box.style.fontSize = "20px";
```

---

### 🎯 4. **Add Event Listeners**

```html
<button id="clickMe">Click Me</button>
<p id="output"></p>

<script>
  document.getElementById("clickMe").addEventListener("click", () => {
    document.getElementById("output").innerText = "You clicked the button!";
  });
</script>
```

---

### ➕ 5. **Create and Append Elements**

```js
const newPara = document.createElement("p");
newPara.innerText = "This is a new paragraph";

document.body.appendChild(newPara); // adds it to the end of body
```

---

## 🛠 Mini DOM Project: Counter Button

```html
<button id="btn">Click Me</button>
<p id="count">0</p>

<script>
  let counter = 0;

  document.getElementById("btn").addEventListener("click", () => {
    counter++;
    document.getElementById("count").innerText = counter;
  });
</script>
```

---

## 📌 Summary

| Task                 | Method                            |
| -------------------- | --------------------------------- |
| Select 1 element     | `getElementById`, `querySelector` |
| Select many elements | `querySelectorAll`                |
| Change text/HTML     | `.innerText`, `.innerHTML`        |
| Change styles        | `.style.property`                 |
| Handle clicks/events | `.addEventListener("click", fn)`  |
| Create elements      | `document.createElement()`        |
| Add to DOM           | `.appendChild()`                  |


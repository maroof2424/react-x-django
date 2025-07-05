## Day3

## 🗓️ **July 3 (Thu) — JavaScript Fundamentals**

**Goal:** Master essential JavaScript features required for React and API communication.

---

### ✅ **1. ES6+ Features (60 min)**

Learn modern JavaScript (ES6+) which is the base for React.

#### 📚 Topics:

* `let`, `const`, and scope
* Arrow functions: `() => {}`
* Template literals: \`\${variable}\`
* Destructuring: `const {name} = obj`
* Spread/rest operators: `[...arr]`, `{...obj}`
* Array methods: `map()`, `filter()`, `reduce()`
* `Promises`, `async/await`

#### 💡 Practice:

```js
const fruits = ['apple', 'banana', 'orange'];
const upperFruits = fruits.map(fruit => fruit.toUpperCase());
console.log(upperFruits);
```

---

### ✅ **2. DOM Manipulation (45 min)**

How to interact with HTML using JavaScript.

#### 📚 Topics:

* `document.querySelector()`, `getElementById()`
* Changing content: `.innerText`, `.innerHTML`
* Handling events: `.addEventListener()`
* Creating elements: `createElement()`, `appendChild()`

#### 💡 Practice:

```html
<button id="btn">Click me</button>
<p id="output"></p>
<script>
  document.getElementById("btn").addEventListener("click", () => {
    document.getElementById("output").innerText = "Hello DOM!";
  });
</script>
```

---

### ✅ **3. Fetch API (45 min)**

Used to connect frontend with backend (e.g., Django API).

#### 📚 Topics:

* `fetch()` basics
* `then()` vs `async/await`
* Error handling: `.catch()` / `try-catch`

#### 💡 Practice:

```js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

### 🔄 **Wrap-Up & To-Do (15 min)**

* ✅ Revise and summarize what you learned
* ✅ Build a mini app (e.g., fetch random quote and display)
* ✅ Push to GitHub

---

### 💻 Mini Project Suggestion:

**Random Quote Generator**

* Button to fetch quote from an API
* Display it in a styled box
* Add loader using `innerText = "Loading..."`

---

Let me know if you want:

* Practice exercises with solutions
* A mini project template
* GitHub push guide for this practice

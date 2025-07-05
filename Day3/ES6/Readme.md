
## ✅ **1. ES6+ Features in 60 Minutes**

### 🧠 What is ES6?

ES6 (ECMAScript 2015) introduced modern JavaScript features that make your code cleaner and more powerful — **a must-know before React**.

---

### ⏱️ **0–10 min: `let` and `const` + Block Scope**

* `var` is function-scoped ❌
* `let` and `const` are block-scoped ✅
* Use `const` for values that don’t change, `let` when it does.

```js
let name = "Maroof";
const age = 17;
// age = 18 ❌ // const can't be changed
```

✅ **Exercise:**

```js
let count = 0;
count += 1;
console.log(count); // 1
```

---

### ⏱️ **10–20 min: Arrow Functions `() => {}`**

* Shorter syntax for functions.
* Inherits `this` from parent scope.

```js
// Normal
function greet(name) {
  return `Hello, ${name}`;
}

// Arrow
const greetArrow = (name) => `Hello, ${name}`;
```

✅ **Exercise:** Convert:

```js
function square(x) {
  return x * x;
}
```

➡️ Into arrow function.

---

### ⏱️ **20–30 min: Template Literals**

* Use backticks (\``) and `\${}\` to insert variables in strings.

```js
let user = "Maroof";
let msg = `Welcome, ${user}!`;
console.log(msg);
```

✅ **Exercise:**

```js
let fruit = "apple";
let price = 100;
console.log(`The price of ${fruit} is PKR ${price}.`);
```

---

### ⏱️ **30–40 min: Destructuring**

Extract values from arrays or objects easily.

```js
const person = { name: "Ali", age: 25 };
const { name, age } = person;

const arr = [1, 2, 3];
const [a, b] = arr;
```

✅ **Exercise:**

```js
const laptop = { brand: "HP", ram: "8GB" };
// Destructure to get `brand` and `ram`
```

---

### ⏱️ **40–50 min: Spread & Rest `...`**

* **Spread**: Expands arrays/objects
* **Rest**: Gathers remaining values

```js
const a = [1, 2];
const b = [...a, 3, 4]; // [1, 2, 3, 4]

function sum(...nums) {
  return nums.reduce((total, n) => total + n, 0);
}
```

✅ **Exercise:**

```js
const car = { brand: "Toyota", model: "Corolla" };
const car2025 = { ...car, year: 2025 };
```

---

### ⏱️ **50–60 min: Array Methods — `map()`, `filter()`, `reduce()`**

**`map()`**: Transform items
**`filter()`**: Select items
**`reduce()`**: Accumulate values

```js
const nums = [1, 2, 3, 4];

// map
const squared = nums.map(n => n * n); // [1, 4, 9, 16]

// filter
const even = nums.filter(n => n % 2 === 0); // [2, 4]

// reduce
const total = nums.reduce((sum, n) => sum + n, 0); // 10
```

✅ **Mini Exercise:**

```js
const prices = [100, 200, 300];
const discounted = prices.map(p => p * 0.9);
```

---

### 🚀 Wrap-Up:

* You now know the core ES6 features used in React, Node.js, and modern JS projects.
* Try building a mini quiz or notes app using these features.

---

Would you like me to give you:

* 🧪 A mini quiz (5 MCQs)
* 🛠️ A code challenge using all these features in one file
* 📁 GitHub-ready boilerplate to practice

Let me know!

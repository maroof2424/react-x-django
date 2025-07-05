let name_ = "Maroof";
const age_ = 17;
// age = 18 ❌ // const can't be changed

let count = 0;
count += 1;
console.log(count); // 1


// Normal
function greet(name){
    return `Hello ${name}`;
}

// Arrow 
const greetArrow = (name) => `Hello ${name}`;

const square = (x) => x * x ;

// Template Literals 

let user = "Maroof";
let msg = `Welcome, ${user}!`;
console.log(msg);

let fruit = "apple";
let price = 100;
console.log(`The price of ${fruit} is PKR ${price}.`);

// Destructuring 

const person = { name: "Ali", age: 25 };
const { name, age } = person;

const arr = [1, 2, 3];
const [a, b] = arr;

const laptop = { brand: "HP", ram: "8GB" };
// Destructure to get `brand` and `ram`

// Spread & Rest

const c = [1,2];
const d = [...c,3,4];

function sum(...nums) {
    return nums.reduce((total,n)=>total+n,0);
}
console.log(sum(1, 2, 3, 4)); // 10


const car = { brand: "Toyota", model: "Corolla" };
const car2025 = { ...car, year: 2025 };

---
title: Classes and Instances
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is a class?

A **class** is a blueprint; an **instance** is the object created from that blueprint. One class can produce many instances.

```javascript
class Car {
  // empty class: valid, but does nothing yet
}

const myCar = new Car();
console.log(myCar); // Car {}
```

- `Car` is the **class** (the blueprint).
- `myCar` is an **instance** (a specific object created from the class).
- Calling `new Car()` creates a new instance.

## Creating instances

You create an instance by calling the class with `new`. JavaScript allocates a new object and runs the class’s `constructor`.

```javascript
class Car {}

const car1 = new Car();
const car2 = new Car();
```

Each call to `new` returns a fresh object with its own identity.

## Adding properties manually

You can add properties after creation (JavaScript objects are open by default):

```javascript
class Car {}

const myCar = new Car();
myCar.color = "blue";
myCar.make = "Toyota";
myCar.model = "Camry";

console.log(myCar.color); // "blue"
```

Each instance can hold different data:

```javascript
const car1 = new Car();
car1.color = "blue";

const car2 = new Car();
car2.color = "red";

console.log(car1.color); // "blue"
console.log(car2.color); // "red"
```

Adding properties manually works, but it’s easy to forget or be inconsistent. Prefer setting them up in the constructor.

## Using `constructor` to set up instances

`constructor` runs automatically when you call `new`. It’s the right place to initialize instance state.

```javascript
class Car {
  constructor(make, model, color) {
    console.log("Vroom! A car was created!");
    this.make = make;   // property on the instance
    this.model = model; // property on the instance
    this.color = color; // property on the instance
  }
}

const myCar = new Car("Toyota", "Camry", "Blue");
// Logs: Vroom! A car was created!

const yourCar = new Car("Honda", "Civic", "Red");
// Logs: Vroom! A car was created!
```

- `constructor` is a special method that runs when you create a new instance.
- Arguments you pass to `new Car(...)` are passed into `constructor`.
- `this` inside `constructor` refers to the instance being created.

## Instance properties

Instance properties live on each individual object created from the class.

```javascript
class Car {
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
  }
}

const myCar = new Car("Toyota", "Camry", "Blue");
console.log(myCar.color); // "Blue"

myCar.color = "Green";    // modify the property
console.log(myCar.color); // "Green"
```

Changing one instance does **not** affect another:

```javascript
const car1 = new Car("Toyota", "Camry", "Blue");
const car2 = new Car("Honda", "Civic", "Red");

car1.color = "Green";

console.log(car1.color); // "Green"
console.log(car2.color); // "Red" (unchanged)
```

If you access a property that doesn’t exist, you get `undefined` (not an error):

```javascript
const car = new Car("Toyota", "Camry", "Blue");
console.log(car.year); // undefined (property not set)
```

You can check for a property with `"prop" in obj` or `Object.hasOwn(obj, "prop")`:

```javascript
if ("year" in car) {
  console.log(car.year);
} else {
  console.log("No year set");
}
```

## Instance methods (preview)

Instance methods are functions defined on the class that operate on each instance’s data:

```javascript
class Car {
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
    this.mileage = 0;
  }

  drive(miles) {
    this.mileage += miles;
    return this.mileage;
  }

  getInfo() {
    return `${this.color} ${this.make} ${this.model}`;
  }
}

const car = new Car("Toyota", "Camry", "Blue");
car.drive(100);
console.log(car.getInfo()); // "Blue Toyota Camry"
```

Methods live on the prototype and share the same implementation across instances; `this` refers to the instance that called the method. (The next guide dives deeper into methods and `this`.)

## Summary

- A **class** is a blueprint; an **instance** is an object created from it.
- Create instances with `new`—JavaScript allocates an object and runs `constructor`.
- Store instance data on `this`; each instance gets its own copy.
- Missing properties return `undefined`; check with `"prop" in obj` or `Object.hasOwn`.
- Methods let instances act on their own data; they’re defined on the class and shared across instances.

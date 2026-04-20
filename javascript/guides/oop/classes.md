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

## What are classes and instances?

A **class** is a blueprint for creating objects. An **instance** is an object created from that class.

```javascript
class Car {}

const myCar = new Car();

console.log(myCar); // Car {}
```

`Car` is the class. `myCar` is an instance.

## Why this matters

Classes are useful when you need many objects with the same shape and behavior. Instead of manually creating similar objects over and over, you define the structure once in a class and create instances with `new`.

## Creating instances with `new`

Use `new ClassName()` to create an instance:

```javascript
class Car {}

const car1 = new Car();
const car2 = new Car();

console.log(car1 === car2); // false
```

Each call to `new Car()` creates a fresh object.

## The `constructor`

The `constructor` method runs automatically when you create a new instance. Use it to set up instance data.

```javascript
class Car {
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
  }
}

const car = new Car("Toyota", "Camry", "Blue");

console.log(car.make);  // "Toyota"
console.log(car.model); // "Camry"
console.log(car.color); // "Blue"
```

Arguments passed to `new Car(...)` become arguments to `constructor`.

## Instance properties

Instance properties store data on each individual object:

```javascript
class Car {
  constructor(make, model) {
    this.make = make;
    this.model = model;
    this.mileage = 0;
  }
}

const car1 = new Car("Toyota", "Camry");
const car2 = new Car("Honda", "Civic");

car1.mileage = 100;

console.log(car1.mileage); // 100
console.log(car2.mileage); // 0
```

Changing one instance does not change another instance.

## Adding properties manually

JavaScript objects are flexible, so you can add properties after creation:

```javascript
class Car {}

const car = new Car();
car.make = "Toyota";
car.model = "Camry";

console.log(car.make); // "Toyota"
```

This works, but it is easy to forget a property or create inconsistent objects. Prefer setting expected properties in the constructor.

## Missing properties

If you read a property that does not exist, JavaScript returns `undefined`:

```javascript
class Car {
  constructor(make) {
    this.make = make;
  }
}

const car = new Car("Toyota");

console.log(car.year); // undefined
```

Use `in` or `Object.hasOwn()` when you need to check for a property:

```javascript
if ("year" in car) {
  console.log(car.year);
} else {
  console.log("No year set");
}
```

## Instance methods

Methods are functions defined inside a class. They usually work with instance data through `this`.

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

console.log(car.drive(100)); // 100
console.log(car.getInfo());  // "Blue Toyota Camry"
```

The next guide covers methods and `this` in more detail.

## Common patterns

### Default property values

```javascript
class Task {
  constructor(title) {
    this.title = title;
    this.isComplete = false;
  }
}

const task = new Task("Learn classes");

console.log(task.isComplete); // false
```

### Creating multiple instances

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
}

const users = [
  new User("Alice"),
  new User("Bob"),
  new User("Charlie")
];

console.log(users[0].name); // "Alice"
```

### Checking an instance's class

```javascript
class User {}

const user = new User();

console.log(user instanceof User); // true
```

## Best practices

- **Use classes for repeated shapes**: Classes are useful when many objects share the same setup and behavior.
- **Initialize expected properties in `constructor`**.
- **Use `this` for instance data**.
- **Avoid adding random properties later** unless the object is intentionally flexible.
- **Keep constructors simple**: Heavy work usually belongs in methods or helper functions.
- **Use clear class names**: Class names usually use PascalCase, like `UserAccount`.

## Summary

Classes are blueprints, and instances are objects created from those blueprints. Use `new` to create an instance, `constructor` to initialize instance data, and `this` to store properties on the current instance. Each instance has its own state, while methods define shared behavior.

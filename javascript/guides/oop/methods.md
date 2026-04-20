---
title: Methods and `this`
sidebar_position: 2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are methods?

**Methods** are functions that belong to an object or class. Instance methods work with the data stored on a specific instance.

```javascript
class User {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello, ${this.name}!`;
  }
}

const user = new User("Alice");

console.log(user.greet()); // "Hello, Alice!"
```

The method `greet()` uses `this.name`, which belongs to the `user` instance.

## Why this matters

Methods are how objects do things. They let you keep behavior close to the data it works with, which is the main reason to use classes.

Understanding `this` is essential because methods usually read or update instance state through `this`.

## Defining instance methods

Define methods inside the class body:

```javascript
class Car {
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
  }

  getInfo() {
    return `${this.color} ${this.make} ${this.model}`;
  }
}

const car = new Car("Toyota", "Camry", "Blue");

console.log(car.getInfo()); // "Blue Toyota Camry"
```

Methods are shared across instances, but `this` changes based on which instance calls the method.

## What `this` means

Inside an instance method, `this` refers to the instance that called the method:

```javascript
class Counter {
  constructor() {
    this.value = 0;
  }

  increment() {
    this.value += 1;
    return this.value;
  }
}

const first = new Counter();
const second = new Counter();

console.log(first.increment());  // 1
console.log(first.increment());  // 2
console.log(second.increment()); // 1
```

`first` and `second` each have their own `value`.

## Methods that modify state

Methods can change instance properties:

```javascript
class BankAccount {
  constructor(owner, balance = 0) {
    this.owner = owner;
    this.balance = balance;
  }

  deposit(amount) {
    this.balance += amount;
    return this.balance;
  }

  withdraw(amount) {
    if (amount > this.balance) {
      throw new Error("Insufficient funds");
    }

    this.balance -= amount;
    return this.balance;
  }
}

const account = new BankAccount("Alice", 100);

console.log(account.deposit(50));  // 150
console.log(account.withdraw(30)); // 120
```

These methods modify `account.balance`.

## Methods that return values

Methods can also compute values without changing state:

```javascript
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  area() {
    return this.width * this.height;
  }

  isSquare() {
    return this.width === this.height;
  }
}

const rectangle = new Rectangle(5, 5);

console.log(rectangle.area());     // 25
console.log(rectangle.isSquare()); // true
```

These methods read instance state and return results.

## Calling methods from methods

Methods can call other methods on the same instance with `this.methodName()`:

```javascript
class Car {
  constructor(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.mileage = 0;
  }

  drive(miles) {
    this.mileage += miles;
  }

  getInfo() {
    return `${this.year} ${this.make} ${this.model}`;
  }

  getFullInfo() {
    return `${this.getInfo()} with ${this.mileage} miles`;
  }
}

const car = new Car("Toyota", "Camry", 2020);
car.drive(100);

console.log(car.getFullInfo()); // "2020 Toyota Camry with 100 miles"
```

## Losing `this`

`this` depends on how a function is called. If you pull a method off an instance and call it by itself, `this` can be lost:

```javascript
class User {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello, ${this.name}!`;
  }
}

const user = new User("Alice");
const greet = user.greet;

// This would cause an error:
// greet(); // TypeError in many environments
```

Use `bind()` to lock `this` to the instance:

```javascript
const boundGreet = user.greet.bind(user);

console.log(boundGreet()); // "Hello, Alice!"
```

Or use an arrow wrapper:

```javascript
const callGreet = () => user.greet();

console.log(callGreet()); // "Hello, Alice!"
```

## Common patterns

### Validation inside methods

```javascript
class TodoList {
  constructor() {
    this.items = [];
  }

  addItem(text) {
    if (!text.trim()) {
      throw new Error("Todo text is required");
    }

    this.items.push(text);
  }
}
```

### Chainable methods

Some methods return `this` so calls can be chained:

```javascript
class Builder {
  constructor() {
    this.parts = [];
  }

  add(part) {
    this.parts.push(part);
    return this;
  }
}

const builder = new Builder();
builder.add("header").add("body");

console.log(builder.parts); // ["header", "body"]
```

Use chaining only when it makes the code clearer.

## Best practices

- **Use methods for behavior tied to instance state**.
- **Use `this` only when you need instance data**.
- **Keep methods focused**: One method should do one clear job.
- **Validate inputs before changing state**.
- **Be careful when passing methods as callbacks**: Use `bind()` or an arrow wrapper.
- **Prefer clear method names**: Use verbs like `deposit`, `getBalance`, `markComplete`, or `calculateTotal`.

## Summary

Methods are functions attached to classes or objects. Instance methods use `this` to read and update the current instance. `this` is set by how a method is called, so passing methods around can lose the original instance. Use methods to keep behavior close to the state it works with, and keep each method focused.

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

Instance methods are functions attached to a class that work with the instance’s data. They’re defined once on the class and shared across instances. Understanding how `this` works is key.

## Defining instance methods

Define methods inside the class body. When you call them on an instance, JavaScript sets `this` to that instance.

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

  repaint(newColor) {
    this.color = newColor;
    return `The car is now ${newColor}`;
  }
}

const myCar = new Car("Toyota", "Camry", "Blue");
console.log(myCar.getInfo());    // "Blue Toyota Camry"
console.log(myCar.repaint("Red")); // "The car is now Red"
console.log(myCar.getInfo());    // "Red Toyota Camry"
```

- `getInfo()` is a **method** that uses the instance’s data.
- `repaint()` is a **method** that modifies the instance’s data.
- When you call `myCar.getInfo()`, JavaScript passes `myCar` as `this`.

## The `this` reference

Inside instance methods, `this` refers to the **instance that called the method**.

```javascript
class Counter {
  constructor() {
    this.value = 0;
  }
  increment() {
    this.value += 1;
  }
}

const c1 = new Counter();
const c2 = new Counter();

c1.increment(); // changes c1.value to 1
c2.increment(); // changes c2.value to 1

console.log(c1.value); // 1
console.log(c2.value); // 1
```

Each call works on the instance that invoked it.

## Methods that modify instance state

Methods can change the instance’s properties:

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

  getBalance() {
    return this.balance;
  }
}

const account = new BankAccount("Alice", 100);
account.deposit(50);
console.log(account.getBalance()); // 150

account.withdraw(30);
console.log(account.getBalance()); // 120
```

## Methods that return values

Methods can return values computed from instance state:

```javascript
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  area() {
    return this.width * this.height;
  }

  perimeter() {
    return 2 * (this.width + this.height);
  }

  isSquare() {
    return this.width === this.height;
  }
}

const rect = new Rectangle(5, 5);
console.log(rect.area());      // 25
console.log(rect.perimeter()); // 20
console.log(rect.isSquare());  // true
```

## Calling methods from other methods

Methods can call other methods on the same instance:

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

  fullInfo() {
    const info = this.getInfo();
    return `${info} with ${this.mileage} miles`;
  }
}

const car = new Car("Toyota", "Camry", 2020);
car.drive(100);
console.log(car.fullInfo()); // "2020 Toyota Camry with 100 miles"
```

## Methods with multiple parameters

Methods can take any parameters you need beyond `this`:

```javascript
class Calculator {
  constructor() {
    this.history = [];
  }

  add(a, b) {
    const result = a + b;
    this.history.push(`${a} + ${b} = ${result}`);
    return result;
  }

  multiply(a, b) {
    const result = a * b;
    this.history.push(`${a} * ${b} = ${result}`);
    return result;
  }
}

const calc = new Calculator();
console.log(calc.add(5, 3));      // 8
console.log(calc.multiply(4, 7)); // 28
console.log(calc.history);        // ["5 + 3 = 8", "4 * 7 = 28"]
```

## Keeping `this` intact (common gotcha)

If you pull a method off an instance and call it later, `this` can be lost:

```javascript
const car = new Car("Toyota", "Camry", "Blue");
const info = car.getInfo;
info(); // `this` is undefined; throws or returns wrong data
```

Bind the method or use an arrow wrapper when passing as a callback:

```javascript
const boundInfo = car.getInfo.bind(car);
console.log(boundInfo());
```

## Summary

- Instance methods are defined on the class and shared across instances.
- `this` inside a method refers to the instance that called it.
- Methods can read/modify instance state and return computed values.
- Methods can call other methods on the same instance.
- Be careful when passing methods as callbacks—bind them to keep `this`.

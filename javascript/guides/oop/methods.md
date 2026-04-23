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

# Methods and `this`

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

**What happens:**

1. `user.greet()` calls the method on the `user` instance.
2. Inside `greet()`, `this` refers to `user`.
3. The method reads `this.name` and returns a greeting.

## Why this matters

Methods are how objects do things. They let you keep behavior close to the data it works with, which is the main reason to use classes.

Understanding `this` is essential because methods usually read or update instance state through `this`.

Methods are useful when a behavior naturally belongs to the object. A `BankAccount` can `deposit()`, a `TodoItem` can `complete()`, and a `Cart` can `calculateTotal()`.

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

Class method syntax does not use the `function` keyword:

```javascript
class User {
  greet() {
    return "Hello!";
  }
}
```

You also do not put commas between methods in a class:

```javascript
class User {
  greet() {
    return "Hello!";
  }

  sayGoodbye() {
    return "Goodbye!";
  }
}
```

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

**Rule of thumb:** look to the left of the method call. In `first.increment()`, `this` is `first`. In `second.increment()`, `this` is `second`.

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

When a method changes state, validate the input before making the change. In `withdraw()`, the method checks the balance before subtracting money.

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

Read-only methods are useful when other code needs information about an object without changing it.

## Methods with parameters

Methods can accept parameters just like regular functions:

```javascript
class Scoreboard {
  constructor() {
    this.score = 0;
  }

  addPoints(points) {
    this.score += points;
    return this.score;
  }
}

const scoreboard = new Scoreboard();

console.log(scoreboard.addPoints(10)); // 10
console.log(scoreboard.addPoints(5));  // 15
```

Use parameters when the method needs extra information from the caller.

## Calling one method from another

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

Calling one method from another helps you reuse behavior instead of repeating the same formatting or calculation in multiple places.

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

This also matters when passing methods as callbacks:

```javascript
class ButtonCounter {
  constructor() {
    this.count = 0;
  }

  increment() {
    this.count += 1;
    console.log(this.count);
  }
}

const counter = new ButtonCounter();

// This would lose `this` in many callback situations:
// setTimeout(counter.increment, 1000);

setTimeout(() => counter.increment(), 1000);
```

The arrow wrapper calls the method on `counter`, so `this` still points to the instance.

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

Validation keeps the object from moving into an invalid state.

### Read methods and write methods

Some methods only read state. Other methods change state.

```javascript
class TodoItem {
  constructor(text) {
    this.text = text;
    this.isComplete = false;
  }

  complete() {
    this.isComplete = true;
  }

  getLabel() {
    return this.isComplete ? `${this.text} (done)` : this.text;
  }
}

const todo = new TodoItem("Practice methods");

console.log(todo.getLabel()); // "Practice methods"

todo.complete();

console.log(todo.getLabel()); // "Practice methods (done)"
```

`complete()` changes the object. `getLabel()` reads the object and returns a value.

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

- **Use methods for behavior tied to instance state**: If the behavior belongs to the object, a method is a good fit.
- **Use `this` only when you need instance data**: If the logic does not need instance state, a plain helper function may be clearer.
- **Keep methods focused**: One method should do one clear job.
- **Validate inputs before changing state**: Check for invalid values before updating properties.
- **Be careful when passing methods as callbacks**: Use `bind()` or an arrow wrapper.
- **Prefer clear method names**: Use verbs like `deposit`, `getBalance`, `markComplete`, or `calculateTotal`.

## Summary

Methods are functions attached to classes or objects. Instance methods use `this` to read and update the current instance. `this` is set by how a method is called, so passing methods around can lose the original instance. Use methods to keep behavior close to the state it works with, and keep each method focused.

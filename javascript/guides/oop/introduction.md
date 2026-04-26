---
title: Intro to JS OOP
sidebar_position: 0
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is object-oriented programming?

**Object-oriented programming (OOP)** is a way to organize code around objects that bundle data and behavior together. In JavaScript, this usually means using classes to create objects with their own state and methods.

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

In this example, the `User` instance has data (`name`) and behavior (`greet()`).

**What happens:**

1. `class User` defines the shape and behavior of a user.
2. `new User("Alice")` creates one user instance.
3. `user.greet()` runs a method that uses the instance's own `name`.

## Why this matters

OOP can make code easier to organize when your program has many related things with their own state and behavior: users, orders, game characters, shapes, accounts, tasks, and more.

JavaScript is flexible. You do not need to use OOP for everything. Use it when it makes the model clearer, and use plain objects or functions when those are simpler.

## The OOP mental model

Think of an object as a small unit that owns some state and exposes actions for working with that state.

For example, a counter owns a number and exposes methods that change or read that number:

```javascript
class Counter {
  constructor() {
    this.value = 0;
  }

  increment() {
    this.value += 1;
    return this.value;
  }

  reset() {
    this.value = 0;
  }
}

const counter = new Counter();

console.log(counter.increment()); // 1
console.log(counter.increment()); // 2

counter.reset();

console.log(counter.value); // 0
```

The important idea is not just that the object stores data. The object also controls the operations that belong with that data.

## OOP in JavaScript

JavaScript supports OOP with classes:

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
```

Classes are modern syntax built on JavaScript's prototype system. You do not need to understand prototypes deeply before using classes, but it helps to know this rule of thumb:

**Rule of thumb:** each instance gets its own property values, while methods are shared through the class.

## Core OOP ideas

### Classes and instances

A **class** is a blueprint. An **instance** is an object created from that blueprint.

```javascript
class Car {
  constructor(make) {
    this.make = make;
  }
}

const car1 = new Car("Toyota");
const car2 = new Car("Honda");

console.log(car1.make); // "Toyota"
console.log(car2.make); // "Honda"
```

`car1` and `car2` are separate instances.

### Properties

**Properties** store data on an object:

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
}

const user = new User("Alice");

console.log(user.name); // "Alice"
```

### Methods

**Methods** are functions attached to objects or classes:

```javascript
class User {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello, ${this.name}!`;
  }
}
```

Methods usually use `this` to work with the current instance.

### `this`

Inside a method, `this` refers to the object the method was called on.

```javascript
class User {
  constructor(name) {
    this.name = name;
  }

  rename(newName) {
    this.name = newName;
  }
}

const user = new User("Alice");

user.rename("Dirk");

console.log(user.name); // "Dirk"
```

Here, `this.name` means "the `name` property on this particular `user` instance."

### Encapsulation

**Encapsulation** means hiding internal details and exposing a clear interface:

```javascript
class BankAccount {
  #balance = 0;

  deposit(amount) {
    this.#balance += amount;
  }

  getBalance() {
    return this.#balance;
  }
}
```

Callers can use `deposit()` and `getBalance()`, but they cannot directly change `#balance`.

### Inheritance

**Inheritance** lets one class build on another class:

```javascript
class Animal {
  speak() {
    return "Some sound";
  }
}

class Dog extends Animal {
  speak() {
    return "Woof";
  }
}

const dog = new Dog();

console.log(dog.speak()); // "Woof"
```

Inheritance can be useful, but deep inheritance trees become hard to change. Prefer simple designs.

## When OOP is a good fit

OOP is usually a good fit when the code has:

- **State**: Each object needs to remember information.
- **Behavior**: The object has actions that belong with that information.
- **Repeated shape**: You need many objects that work the same way.
- **Rules**: The object should protect its data from invalid changes.

Use a plain object when you only need to group values:

```javascript
const user = {
  name: "Alice",
  role: "admin",
};
```

Use a function when you only need to transform inputs into an output:

```javascript
function formatUserName(user) {
  return `${user.name} (${user.role})`;
}
```

Use a class when state and behavior naturally belong together:

```javascript
class TodoItem {
  constructor(text) {
    this.text = text;
    this.completed = false;
  }

  complete() {
    this.completed = true;
  }
}
```

## What this section covers

This OOP section covers:

- Classes and instances
- Methods and `this`
- Encapsulation and private fields
- Inheritance
- Static properties and methods
- Classes vs plain objects
- When to use OOP

Start with [Classes and Instances](./classes), then move through methods, encapsulation, inheritance, and the final guide on choosing when to use OOP.

## What this section does not cover

This section does not go deep into:

- Manual prototype manipulation
- Framework-specific class patterns
- Advanced design patterns
- TypeScript-specific OOP features

The goal is to help you read and write everyday JavaScript classes confidently.

## Best practices

- **Use OOP when it clarifies the model**: Classes work well for stateful entities with behavior.
- **Do not force everything into classes**: Plain objects and functions are often simpler.
- **Keep classes focused**: A class should have one clear responsibility.
- **Prefer composition over deep inheritance**: Combine smaller pieces instead of building tall class trees.
- **Use clear method names**: Methods should describe actions the object can perform.

## Summary

OOP organizes code around objects that combine data and behavior. In JavaScript, classes create instances, properties store state, methods define behavior, and `this` refers to the current instance. OOP is useful when it makes a problem easier to model, but JavaScript also works well with plain objects, functions, and modules.

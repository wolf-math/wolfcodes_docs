---
title: When to Use OOP in JavaScript
sidebar_position: 7
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Use object-oriented programming when it makes the problem easier to model.

JavaScript supports OOP, but it does not force every problem into classes.

## Why the choice matters

Good structure makes code easier to change.

If a class clearly represents a thing in your program, OOP can make the code feel natural.

If a class only wraps a few unrelated functions, it can add noise.

The goal is not to use OOP everywhere. The goal is to choose the shape that makes the code easier to understand.

## Use OOP for stateful entities

OOP works well when you have objects that own state and behavior.

```javascript
class Timer {
  constructor() {
    this.seconds = 0;
  }

  tick() {
    this.seconds += 1;
  }

  reset() {
    this.seconds = 0;
  }
}

const timer = new Timer();

timer.tick();
timer.tick();

console.log(timer.seconds);
```

The timer owns its state.

Its methods describe what can happen to that state.

## Use OOP for repeated objects

Classes are helpful when you need many similar objects.

```javascript
class Player {
  constructor(name) {
    this.name = name;
    this.score = 0;
  }

  addPoint() {
    this.score += 1;
  }
}

const playerOne = new Player("Maya");
const playerTwo = new Player("Nia");

playerOne.addPoint();

console.log(playerOne.score);
console.log(playerTwo.score);
```

Each player has separate state.

They share the same behavior.

## Use OOP for rules and invariants

OOP is useful when an object has rules that should stay true.

```javascript
class InventoryItem {
  #quantity;

  constructor(name, quantity) {
    this.name = name;
    this.#quantity = quantity;
  }

  remove(amount) {
    if (amount > this.#quantity) {
      throw new Error("Not enough inventory");
    }

    this.#quantity -= amount;
  }

  get quantity() {
    return this.#quantity;
  }
}
```

The class protects its own state.

Outside code cannot directly change `#quantity` to an invalid value.

## Use simpler patterns for simple data

If you only need to group values, a plain object is usually enough.

```javascript
const profile = {
  name: "Maya",
  location: "Portland",
  interests: ["JavaScript", "design", "music"],
};
```

There is no need for a class if the object does not manage behavior or rules.

## Use functions for stateless logic

If a piece of logic only turns inputs into outputs, a function may be clearer than a class.

```javascript
function calculateDiscount(price, percent) {
  return price * (percent / 100);
}

console.log(calculateDiscount(50, 10));
```

This does not need an object.

It just needs a useful function name.

## Be careful with inheritance

Inheritance is powerful, but it can make code rigid when the hierarchy gets too deep.

```javascript
class Bird {
  fly() {
    return "Flying";
  }
}

class Penguin extends Bird {}
```

This model has a problem: a penguin is a bird, but it does not fly.

When the real world has exceptions, inheritance can become awkward.

## Prefer composition for flexible behavior

Composition means building objects from smaller pieces of behavior.

```javascript
function logMessage(message) {
  console.log(message);
}

class PaymentService {
  constructor(logger) {
    this.logger = logger;
  }

  charge(amount) {
    this.logger(`Charging $${amount}`);
  }
}

const service = new PaymentService(logMessage);

service.charge(25);
```

The service does not need to inherit from a logging class.

It just receives the behavior it needs.

## Mixing paradigms

Most JavaScript programs mix objects, functions, arrays, modules, and classes.

That is normal.

You might use a class for a `Cart`, plain objects for cart items, and functions for formatting prices.

```javascript
class Cart {
  constructor() {
    this.items = [];
  }

  addItem(item) {
    this.items.push(item);
  }

  getTotal() {
    return this.items.reduce((total, item) => total + item.price, 0);
  }
}

function formatPrice(price) {
  return `$${price.toFixed(2)}`;
}

const cart = new Cart();

cart.addItem({ name: "Notebook", price: 8 });
cart.addItem({ name: "Pen", price: 2 });

console.log(formatPrice(cart.getTotal()));
```

Use each tool where it fits.

## Decision checklist

Use OOP when the answer to several of these questions is yes:

- Does this concept have state?
- Does the state need rules?
- Will I create many similar objects?
- Do the methods naturally belong to the data?
- Would a public interface make this easier to use correctly?

Use a simpler pattern when the answer to these questions is no.

## Best practices

Start simple.

Use classes when they make a concept clearer, not just because they are available.

Keep classes focused on one responsibility.

Prefer composition when behavior needs to be mixed and matched.

Avoid deep inheritance trees.

## Summary

OOP is useful for stateful concepts, repeated objects, and data with rules.

Plain objects are often better for simple data.

Functions are often better for stateless logic.

Good JavaScript uses the pattern that makes the code easiest to understand.

---
title: Classes vs Plain Objects
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

JavaScript gives you both plain objects and classes.

They overlap, but they are useful in different situations.

## Why the difference matters

Not every group of values needs a class.

Plain objects are great when you only need data.

Classes are useful when you need many similar objects that share behavior.

Choosing the simpler tool keeps your code easier to read.

## Plain objects

A plain object is a direct collection of key-value pairs.

```javascript
const user = {
  name: "Maya",
  role: "admin",
  active: true,
};

console.log(user.name);
```

Plain objects are common for configuration, API data, and simple records.

```javascript
const settings = {
  theme: "dark",
  notifications: true,
  language: "en",
};
```

Use a plain object when the main job is to hold data.

## Classes

A class is a blueprint for creating objects with shared behavior.

```javascript
class User {
  constructor(name, role) {
    this.name = name;
    this.role = role;
  }

  canEdit() {
    return this.role === "admin";
  }
}

const user = new User("Maya", "admin");

console.log(user.canEdit());
```

Use a class when the data and behavior belong together.

## Multiple instances

Classes are especially useful when you need many objects with the same structure and methods.

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

const first = new TodoItem("Study objects");
const second = new TodoItem("Practice classes");

first.complete();

console.log(first.completed);
console.log(second.completed);
```

Each instance has its own state.

The methods are shared through the class.

## Plain objects with functions

Plain objects can contain functions too.

```javascript
const counter = {
  value: 0,
  increment() {
    this.value += 1;
  },
};

counter.increment();

console.log(counter.value);
```

This is useful for one-off objects.

If you need many counters, a class may be clearer.

## Classes are objects too

Instances created from classes are still objects.

```javascript
class Product {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}

const product = new Product("Notebook", 8);

console.log(typeof product);
```

The value of `typeof product` is `"object"`.

Classes are a structured way to create objects, not a separate kind of value.

## Choosing the right tool

Choose a plain object when you are grouping data.

Choose a plain object when the shape is small and obvious.

Choose a class when you need constructors, methods, private fields, or many instances.

Choose a class when the object has rules that should be enforced through methods.

## Common patterns

Use plain objects for JSON-like data.

Use classes for domain concepts such as `Cart`, `Timer`, `UserSession`, or `BankAccount`.

Use plain module functions when behavior does not need to live inside an object.

```javascript
function formatPrice(price) {
  return `$${price.toFixed(2)}`;
}

const product = {
  name: "Notebook",
  price: 8,
};

console.log(formatPrice(product.price));
```

This can be clearer than creating a class only to hold one helper method.

## Best practices

Start with a plain object when you only need data.

Move to a class when behavior, validation, or repeated instances make the object more complex.

Avoid creating classes just because a value has several properties.

Keep the shape of your data easy to see.

## Summary

Plain objects are best for simple data.

Classes are best for repeated objects that share behavior and manage state.

In JavaScript, class instances are still objects. A class is a tool for creating objects with a consistent structure.

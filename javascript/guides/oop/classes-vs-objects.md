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

## What are plain objects and classes?

JavaScript gives you both **plain objects** and **classes**.

Plain objects are a simple way to group data.

Classes are a way to create many similar objects that share behavior.

```javascript
const userObject = { name: "Dirk" };

class User {
  constructor(name) {
    this.name = name;
  }
}

const userClass = new User("Dirk");

console.log(userObject.name); // "Dirk"
console.log(userClass.name);  // "Dirk"
```

Both are objects at runtime. The difference is how you create and organize them.

## Why the difference matters

Not every group of values needs a class.

Plain objects are great when you only need data.

Classes are useful when you need many similar objects that share behavior.

Choosing the simpler tool keeps your code easier to read.

## Plain objects

A plain object is a direct collection of key-value pairs.

```javascript
const user = {
  name: "Dirk",
  role: "admin",
  active: true,
};

console.log(user.name); // "Dirk"
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

const user = new User("Dirk", "admin");

console.log(user.canEdit()); // true
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

console.log(first.completed);  // true
console.log(second.completed); // false
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

console.log(counter.value); // 1
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

console.log(typeof product);             // "object"
console.log(product instanceof Product); // true
```

Classes are a structured way to create objects, not a separate kind of value.

## Choosing the right tool

**Default choice:** start with a plain object when you are grouping data.

Use a plain object when:

- The value is mostly data (config, API response, record-like values).
- You only need one object or a couple of objects.
- The shape is small and obvious.

Use a class when:

- You need many objects with the same shape.
- The object owns state and behavior (methods that use `this`).
- The object has rules (invariants) that should be protected with methods or private fields.
- You want a constructor to set up consistent instance state.

:::tip
If you are not sure, start with a plain object. Move to a class once you feel friction: repeated setup, repeated functions, or state you want to protect.
:::

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

## Common mistakes

### Making a class for data-only values

If the value is just a record, a class often adds ceremony without clarity.

```javascript
// Usually fine as a plain object:
const user = {
  name: "Dirk",
  role: "admin",
};
```

Prefer a class when you also have behavior, validation, or invariants that the object should enforce.

### Forgetting `this` in object methods

When you use a method on a plain object, it still uses `this`:

```javascript
const counter = {
  value: 0,
  increment() {
    this.value += 1;
  },
};

counter.increment();

console.log(counter.value); // 1
```

This is one reason classes can be easier for repeated objects: the shape and methods stay consistent across instances.

## Best practices

Start with a plain object when you only need data.

Move to a class when behavior, validation, or repeated instances make the object more complex.

Avoid creating classes just because a value has several properties.

Keep the shape of your data easy to see.

## Summary

Plain objects are best for simple data.

Classes are best for repeated objects that share behavior and manage state.

In JavaScript, class instances are still objects. A class is a tool for creating objects with a consistent structure.

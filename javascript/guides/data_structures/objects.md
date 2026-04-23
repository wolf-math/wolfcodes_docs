---
title: Objects (Plain Objects)
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

## What are objects?

**Objects** are collections of key-value pairs. They let you group related data together and access values by name.

```javascript
const user = {
  name: "Alice",
  age: 30,
  isAdmin: false
};

console.log(user.name); // "Alice"
console.log(user.age);  // 30
```

This guide covers **plain objects**, also called object literals. Classes and object-oriented programming are covered in the [OOP guide](../oop/introduction).

## Why this matters

Objects are how JavaScript represents structured data. You'll use them for users, settings, API responses, products, form values, and many other things that have named properties.

Objects are also the foundation for many JavaScript APIs. When you understand plain objects, arrays of objects, property access, and reference behavior, much of JavaScript becomes easier to read.

## Creating objects

Use curly braces to create an object literal:

```javascript
const empty = {};

const person = {
  name: "Alice",
  age: 30,
  city: "Cleveland"
};
```

Each property has a key and a value:

```javascript
const person = {
  name: "Alice", // key: name, value: "Alice"
  age: 30        // key: age, value: 30
};
```

Keys are usually strings, and values can be any JavaScript value: strings, numbers, booleans, arrays, other objects, or functions.

## Accessing properties

### Dot notation

Use dot notation when you know the property name and it is a valid identifier:

```javascript
const person = {
  name: "Alice",
  age: 30
};

console.log(person.name); // "Alice"
console.log(person.age);  // 30
```

### Bracket notation

Use bracket notation when the property name is stored in a variable or is not a valid identifier:

```javascript
const person = {
  name: "Alice",
  age: 30
};

const key = "name";

console.log(person[key]); // "Alice"
```

Bracket notation is required for property names with spaces or special characters:

```javascript
const settings = {
  "font size": 16,
  "2faEnabled": true
};

console.log(settings["font size"]); // 16
console.log(settings["2faEnabled"]); // true
```

If a property does not exist, JavaScript returns `undefined`:

```javascript
const person = {
  name: "Alice"
};

console.log(person.city); // undefined
```

## Property shorthand and computed keys

When a variable name matches the property name you want, you can use property shorthand:

```javascript
const name = "Alice";
const age = 30;

const person = {
  name,
  age
};

console.log(person); // { name: "Alice", age: 30 }
```

Use computed property names when the key is stored in a variable:

```javascript
const key = "theme";
const value = "dark";

const settings = {
  [key]: value
};

console.log(settings); // { theme: "dark" }
```

## Adding, changing, and removing properties

Objects are mutable. You can add, update, and remove properties after creating the object.

### Adding properties

```javascript
const person = {
  name: "Alice"
};

person.age = 30;
person.city = "Cleveland";

console.log(person); // { name: "Alice", age: 30, city: "Cleveland" }
```

### Changing properties

```javascript
const person = {
  name: "Alice",
  age: 30
};

person.age = 31;

console.log(person.age); // 31
```

### Removing properties

Use `delete` to remove a property:

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "Cleveland"
};

delete person.city;

console.log(person); // { name: "Alice", age: 30 }
```

## Nested objects

Objects can contain other objects and arrays:

```javascript
const user = {
  name: "Alice",
  address: {
    city: "Cleveland",
    zipCode: "10001"
  },
  roles: ["admin", "editor"]
};

console.log(user.address.city); // "Cleveland"
console.log(user.roles[0]);     // "admin"
```

Nested data is common in API responses. Keep nesting reasonable; deeply nested objects can become hard to read and update.

Use optional chaining (`?.`) when a nested property might be missing:

```javascript
const user = {
  name: "Alice"
};

console.log(user.address?.city); // undefined
```

Without `?.`, `user.address.city` would cause an error because `address` is missing.

## Objects are reference values

Objects are **reference values**. When you assign an object to another variable, both variables refer to the same object:

```javascript
const first = { name: "Alice" };
const second = first;

second.name = "Bob";

console.log(first.name);  // "Bob"
console.log(second.name); // "Bob"
```

This is the same reference behavior you saw with arrays. To make a shallow copy, use spread syntax:

```javascript
const original = { name: "Alice", age: 30 };
const copy = { ...original };

copy.name = "Bob";

console.log(original.name); // "Alice"
console.log(copy.name);     // "Bob"
```

This is a shallow copy. Nested objects are still shared.

```javascript
const original = {
  name: "Alice",
  address: {
    city: "Cleveland"
  }
};

const copy = { ...original };

copy.address.city = "Boston";

console.log(original.address.city); // "Boston"
```

The top-level object was copied, but the nested `address` object was still shared.

Rest and spread syntax are covered in more detail in the [rest and spread guide](./rest_and_spread).

## Looping over objects

There are several ways to loop over an object's properties.

### `Object.keys()`

Use `Object.keys()` when you need property names:

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "Cleveland"
};

for (const key of Object.keys(person)) {
  console.log(key, person[key]);
}
```

**Output:**

```text
name Alice
age 30
city Cleveland
```

### `Object.values()`

Use `Object.values()` when you only need values:

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "Cleveland"
};

for (const value of Object.values(person)) {
  console.log(value);
}
```

**Output:**

```text
Alice
30
Cleveland
```

### `Object.entries()`

Use `Object.entries()` when you need both keys and values:

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "Cleveland"
};

for (const [key, value] of Object.entries(person)) {
  console.log(`${key}: ${value}`);
}
```

**Output:**

```text
name: Alice
age: 30
city: Cleveland
```

### `for...in`

You may also see `for...in`:

```javascript
const person = {
  name: "Alice",
  age: 30
};

for (const key in person) {
  console.log(key, person[key]);
}
```

`for...in` can include inherited properties. For most beginner code, prefer `Object.keys()`, `Object.values()`, or `Object.entries()`.

## Checking properties

Use the `in` operator to check whether a property exists:

```javascript
const person = {
  name: "Alice",
  age: 30
};

console.log("name" in person); // true
console.log("city" in person); // false
```

Use `Object.hasOwn()` when you specifically want an object's own property:

```javascript
const person = {
  name: "Alice"
};

console.log(Object.hasOwn(person, "name")); // true
console.log(Object.hasOwn(person, "city")); // false
```

If you only care whether a property value is not missing, check the value:

```javascript
if (person.name !== undefined) {
  console.log(person.name);
}
```

## Default values

Use `??` when you want a default only for `null` or `undefined`:

```javascript
const settings = {
  retries: 0
};

const retries = settings.retries ?? 3;

console.log(retries); // 0
```

Use `||` when any falsy value should use the default:

```javascript
const user = {
  displayName: ""
};

const displayName = user.displayName || "Guest";

console.log(displayName); // "Guest"
```

**Rule of thumb:** Use `??` when `0`, `false`, or `""` should remain valid values.

## Copying and merging objects

Use spread syntax to copy or merge objects:

```javascript
const defaults = {
  theme: "light",
  language: "en"
};

const userPrefs = {
  theme: "dark"
};

const settings = {
  ...defaults,
  ...userPrefs
};

console.log(settings); // { theme: "dark", language: "en" }
```

Later properties override earlier properties when keys are the same.

For more copying, merging, and destructuring patterns, see the [rest and spread guide](./rest_and_spread).

## Destructuring

Destructuring lets you pull properties into variables:

```javascript
const person = {
  name: "Alice",
  age: 30
};

const { name, age } = person;

console.log(name); // "Alice"
console.log(age);  // 30
```

You can rename a property while destructuring:

```javascript
const { name: userName } = person;

console.log(userName); // "Alice"
```

You can also provide a default value while destructuring:

```javascript
const person = {
  name: "Alice"
};

const { name, role = "member" } = person;

console.log(name); // "Alice"
console.log(role); // "member"
```

## Objects vs arrays

Use objects when:

- You need named properties
- The data represents one structured thing
- You need to look up values by key

Use arrays when:

- Order matters
- You have a list of similar items
- You want to process every item with array methods

Objects and arrays often work together:

```javascript
const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

const names = users.map((user) => user.name);

console.log(names); // ["Alice", "Bob"]
```

## Common patterns

### Building an object incrementally

```javascript
const scores = {};

scores.alice = 95;
scores.bob = 87;

console.log(scores); // { alice: 95, bob: 87 }
```

### Counting values

```javascript
const words = ["apple", "banana", "apple"];
const counts = {};

for (const word of words) {
  counts[word] = (counts[word] ?? 0) + 1;
}

console.log(counts); // { apple: 2, banana: 1 }
```

### Grouping related settings

```javascript
const config = {
  apiUrl: "https://api.example.com",
  timeout: 5000,
  retries: 3
};
```

## Best practices

- **Use object literals**: `{}` is the clearest way to create plain objects.
- **Use dot notation when possible**: It is shorter and easier to read.
- **Use bracket notation for dynamic keys**: Use it when the property name is stored in a variable.
- **Use optional chaining for uncertain nested data**: `user.address?.city` avoids errors when a middle property is missing.
- **Prefer `Object.entries()` for key-value loops**: It makes both pieces visible.
- **Use `??` for safe defaults**: It preserves valid falsy values like `0` and `""`.
- **Remember reference behavior**: Copy objects before changing them if the original should stay unchanged.
- **Remember that spread is shallow**: Nested objects are still shared unless you copy them too.
- **Avoid deep nesting when possible**: Deep data is harder to update safely.

## Summary

Objects group related values under meaningful property names. Use dot notation for known property names, bracket notation for dynamic names, and `Object.keys()`, `Object.values()`, or `Object.entries()` when looping. Objects are reference values, so copying and mutation matter. When your data has named properties, an object is usually the right tool.

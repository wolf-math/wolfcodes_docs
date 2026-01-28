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

**Objects** are collections of key-value pairs. They let you group related data together and access it by name rather than by position (like arrays).

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "New York"
};
```

In JavaScript, objects are used for:
- Representing structured data (like a user, product, or configuration)
- Creating namespaces (grouping related functions)
- As maps/dictionaries (storing data you look up by key)

**Note:** This guide covers **plain objects** (also called "object literals"). We'll cover classes and object-oriented programming in the [OOP guide](../oop/introduction).

## Objects as key–value maps

Objects store data as **properties** (also called keys) with associated **values**:

```javascript
const person = {
  name: "Alice",        // key: "name", value: "Alice"
  age: 30,              // key: "age", value: 30
  isActive: true        // key: "isActive", value: true
};
```

Each property is a `key: value` pair. Keys are strings (or symbols), and values can be any JavaScript type.

## Dot notation vs bracket notation

You can access object properties in two ways:

### Dot notation

```javascript
const person = {
  name: "Alice",
  age: 30
};

person.name;  // "Alice"
person.age;   // 30
```

**Use dot notation when:** You know the property name at write-time and it's a valid identifier.

### Bracket notation

```javascript
const person = {
  name: "Alice",
  age: 30
};

person["name"];  // "Alice"
person["age"];   // 30

// Bracket notation allows variables
const key = "name";
person[key];     // "Alice"
```

**Use bracket notation when:**
- The property name is stored in a variable
- The property name contains special characters or spaces
- The property name starts with a number

```javascript
const obj = {
  "first name": "Alice",  // Property name with space
  "2nd item": "value"     // Property name starting with number
};

obj["first name"];  // "Alice" (bracket notation required)
obj["2nd item"];    // "value" (bracket notation required)
```

## Adding and removing properties

Objects are **mutable**, meaning you can add, modify, and remove properties after creation.

### Adding properties

```javascript
const person = {
  name: "Alice"
};

person.age = 30;           // Add new property with dot notation
person["city"] = "NYC";    // Add new property with bracket notation
person.isActive = true;    // Add boolean property

console.log(person);
// { name: "Alice", age: 30, city: "NYC", isActive: true }
```

### Modifying properties

```javascript
const person = {
  name: "Alice",
  age: 30
};

person.age = 31;  // Modify existing property
person["name"] = "Bob";  // Also works
```

### Removing properties

Use the `delete` operator:

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "NYC"
};

delete person.city;  // Remove the "city" property
console.log(person); // { name: "Alice", age: 30 }
```

## Nested objects

Objects can contain other objects (and arrays):

```javascript
const person = {
  name: "Alice",
  age: 30,
  address: {
    street: "123 Main St",
    city: "New York",
    zipCode: "10001"
  },
  hobbies: ["reading", "coding"]
};

person.address.city;           // "New York"
person.hobbies[0];             // "reading"
person.address.street;         // "123 Main St"
```

You can nest objects as deeply as needed, though too much nesting can make code harder to read.

## Looping over objects

There are several ways to iterate over an object's properties:

### `for...in` loop

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "NYC"
};

for (const key in person) {
  console.log(key, person[key]);
}
// Output:
// name Alice
// age 30
// city NYC
```

:::note 
`for...in` also iterates over inherited properties (from prototypes). In most cases, you'll want to use `Object.keys()`, `Object.values()`, or `Object.entries()` instead.
:::

### `Object.keys()` — get property names

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "NYC"
};

Object.keys(person);  // ["name", "age", "city"]

// Iterate over keys
for (const key of Object.keys(person)) {
  console.log(key, person[key]);
}
```

### `Object.values()` — get property values

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "NYC"
};

Object.values(person);  // ["Alice", 30, "NYC"]

for (const value of Object.values(person)) {
  console.log(value);
}
```

### `Object.entries()` — get key-value pairs

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "NYC"
};

Object.entries(person);
// [["name", "Alice"], ["age", 30], ["city", "NYC"]]

for (const [key, value] of Object.entries(person)) {
  console.log(key, value);
}
```

**Prefer `Object.keys()`, `Object.values()`, or `Object.entries()`** over `for...in` for iterating over own properties.

## Objects vs arrays (when to use each)

Both objects and arrays store collections of data, but they serve different purposes:

### Use objects when:

- You need to look up values by name/key
- The data has a structure with meaningful property names
- Order doesn't matter (though modern JavaScript preserves insertion order)
- You're representing a real-world entity (person, product, configuration)

Examples:
```javascript
const user = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
};

const config = {
  apiUrl: "https://api.example.com",
  timeout: 5000,
  retries: 3
};
```

### Use arrays when:

- Order matters
- You need to iterate over all elements
- You have a list of similar items
- You need array methods (map, filter, reduce)

Examples:
```javascript
const scores = [95, 87, 92, 88];
const names = ["Alice", "Bob", "Charlie"];
```

### Combining both

Objects and arrays work great together:

```javascript
const users = [
  { name: "Alice", age: 30 },
  { name: "Bob", age: 25 },
  { name: "Charlie", age: 35 }
];

// Find user by name
const alice = users.find(user => user.name === "Alice");

// Get all names
const names = users.map(user => user.name);
```

## Common object operations

### Checking if property exists

Use the `in` operator or `hasOwnProperty()` method to check if a property exists on an object:

```javascript
const person = {
  name: "Alice",
  age: 30
};

// Check if property exists (including undefined values)
"name" in person;  // true
"city" in person;  // false

// Check if property exists and is not undefined
person.name !== undefined;  // true
person.city !== undefined;  // false

// Using hasOwnProperty() (for own properties only)
person.hasOwnProperty("name");  // true
```

### Getting property with default

Use the nullish coalescing operator (`??`) or logical OR operator (`||`) to provide default values when a property is missing:

```javascript
const person = {
  name: "Alice"
};

// If property doesn't exist, use default
const age = person.age ?? 0;  // 0 (nullish coalescing)
const city = person.city || "Unknown";  // "Unknown" (logical OR)
```

### Copying objects

Use the spread operator (`...`) or `Object.assign()` method to create a shallow copy of an object:

```javascript
const original = {
  name: "Alice",
  age: 30
};

// Shallow copy using spread operator
const copy = { ...original };

// Shallow copy using Object.assign()
const copy2 = Object.assign({}, original);

// Note: These are shallow copies. Nested objects are still shared.
```

### Merging objects

Use the spread operator (`...`) or `Object.assign()` method to merge multiple objects into one:

```javascript
const defaults = {
  theme: "light",
  language: "en"
};

const userPrefs = {
  theme: "dark"
};

// Merge with spread operator
const settings = { ...defaults, ...userPrefs };
// { theme: "dark", language: "en" }

// Merge with Object.assign()
const settings2 = Object.assign({}, defaults, userPrefs);
```

### Destructuring (preview)

Use destructuring syntax to extract properties from objects into variables:

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "NYC"
};

const { name, age } = person;
console.log(name);  // "Alice"
console.log(age);   // 30

// With renaming
const { name: personName } = person;
console.log(personName);  // "Alice"
```

Destructuring is a powerful feature we'll explore more in later guides.

## Objects are reference types

Objects are **reference types**, meaning variables store a reference to the object, not the object itself:

```javascript
const obj1 = { name: "Alice" };
const obj2 = obj1;  // obj2 points to the same object as obj1

obj2.name = "Bob";
console.log(obj1.name);  // "Bob" (both variables point to same object!)
```

To create a true copy, use the spread operator or `Object.assign()` as shown above.

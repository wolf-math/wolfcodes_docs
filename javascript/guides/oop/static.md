---
title: Static Properties and Methods
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are static properties and methods?

**Static properties and methods** belong to the class itself. They do not belong to individual instances.

:::note
Static class fields like `static role = "member"` are supported in modern JavaScript. In older environments, you may see `User.role = "member"` after the class definition instead.
:::

```javascript
class User {
  static role = "member";

  constructor(name) {
    this.name = name;
  }
}

const user = new User("David");

console.log(User.role); // "member"
console.log(user.name); // "David"
```

`role` belongs to the `User` class. `name` belongs to the `user` instance.

**Rule of thumb:** use instance members for data or behavior tied to one object. Use static members for behavior or values tied to the class as a whole.

## Why static members matter

Most class methods describe something an instance can do.

Static methods describe something the class can do.

That makes them useful for factory methods, utility methods, and shared values that do not depend on one specific object.

Static members can also make code easier to read when a helper clearly belongs with the class concept but does not need `this` from an instance.

## Instance methods

An instance method is called on an object created from the class.

```javascript
class User {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello, ${this.name}!`;
  }
}

const user = new User("David");

console.log(user.greet()); // "Hello, David!"
```

`greet()` needs a specific user's `name`, so it belongs on the instance.

## Static methods

Use the `static` keyword to define a method on the class.

```javascript
class User {
  constructor(name) {
    this.name = name;
  }

  static fromObject(data) {
    return new User(data.name);
  }
}

const user = User.fromObject({ name: "Nia" });

console.log(user.name); // "Nia"
```

`fromObject()` is called on `User`, not on a user instance.

It creates and returns a new instance.

**What happens:**

1. `User.fromObject(...)` calls the static method on the class.
2. The static method reads the plain object.
3. The static method returns `new User(data.name)`.

## Static properties

Static properties store values on the class.

```javascript
class Course {
  static platform = "Wolf Codes";

  constructor(title) {
    this.title = title;
  }
}

console.log(Course.platform); // "Wolf Codes"
```

This is useful for values that are shared by the class as a whole.

Use static properties for class-level constants or defaults, not for data that belongs to one instance.

## Factory methods

A factory method creates an instance in a named way.

```javascript
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  static fromArray(values) {
    return new Point(values[0], values[1]);
  }

  static origin() {
    return new Point(0, 0);
  }
}

const point = Point.fromArray([3, 4]);
const origin = Point.origin();

console.log(point.x);  // 3
console.log(point.y);  // 4
console.log(origin.x); // 0
console.log(origin.y); // 0
```

Factory methods are helpful when the constructor would become unclear or too crowded.

They are also useful when the input format has a name, like `fromArray()`, `fromObject()`, or `fromJSON()`.

## Utility methods

A static method can also be a utility related to the class.

```javascript
class Temperature {
  static celsiusToFahrenheit(celsius) {
    return (celsius * 9) / 5 + 32;
  }
}

console.log(Temperature.celsiusToFahrenheit(20)); // 68
```

This method does not need instance state.

It can live on the class as a named utility.

If the helper does not belong to the class idea, use a plain function instead.

## Accessing static members

Static members are accessed through the class name.

```javascript
class Counter {
  static description = "Counts things";
}

console.log(Counter.description); // "Counts things"
```

Instances do not automatically expose static members.

```javascript
class Counter {
  static description = "Counts things";
}

const counter = new Counter();

console.log(counter.description); // undefined
```

This prints `undefined`.

Use the class name when reading static members:

```javascript
console.log(Counter.description); // "Counts things"
```

If you already have an instance, you can also reach the class through `constructor`:

```javascript
console.log(counter.constructor.description); // "Counts things"
```

## Static members and `this`

Inside a static method, `this` refers to the class, not an instance.

```javascript
class Product {
  static taxRate = 0.08;

  static calculateTax(price) {
    return price * this.taxRate;
  }
}

console.log(Product.calculateTax(100)); // 8
```

There is no individual product instance here. The method uses the class-level `taxRate`.

### Static methods and inheritance

When a static method uses `this`, a subclass can inherit the method and change the static data it uses.

```javascript
class Product {
  static taxRate = 0.08;

  static calculateTax(price) {
    return price * this.taxRate;
  }
}

class FoodProduct extends Product {
  static taxRate = 0.02;
}

console.log(Product.calculateTax(100));     // 8
console.log(FoodProduct.calculateTax(100)); // 2
```

`FoodProduct` reuses the parent static method, but `this.taxRate` refers to the class you called it on.

If a method needs instance data like `this.name`, `this.price`, or `this.items`, make it an instance method instead.

## Common patterns

### Creating instances from other data

Use static methods for `fromJSON()`, `fromObject()`, `fromArray()`, or other named ways to create instances.

```javascript
class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  static fromObject(data) {
    return new User(data.name, data.email);
  }
}

const user = User.fromObject({
  name: "David",
  email: "david@wolfcodes.dev",
});

console.log(user.email); // "david@wolfcodes.dev"
```

### Class-level constants

Use static properties for values that belong to the class concept.

```javascript
class PasswordValidator {
  static minLength = 8;

  static isLongEnough(password) {
    return password.length >= this.minLength;
  }
}

console.log(PasswordValidator.isLongEnough("secret")); // false
console.log(PasswordValidator.isLongEnough("secret123")); // true
```

### Instance behavior stays on instances

Use instance methods when the method needs data from a specific object.

```javascript
class Cart {
  constructor(items) {
    this.items = items;
  }

  getTotal() {
    return this.items.reduce((total, item) => total + item.price, 0);
  }
}

const cart = new Cart([
  { name: "Notebook", price: 8 },
  { name: "Pen", price: 2 },
]);

console.log(cart.getTotal()); // 10
```

`getTotal()` belongs on the instance because each cart has different items.

## Common mistakes

### Shared mutable static state

Static properties are shared by every instance. That can be useful for constants, but surprising for arrays and objects.

```javascript
class UserCache {
  static users = [];

  static addUser(name) {
    this.users.push(name);
  }
}

UserCache.addUser("Maya");
UserCache.addUser("Nia");

console.log(UserCache.users); // ["Maya", "Nia"]
```

This is fine if you intentionally want one shared cache.

If each instance should have its own list, make it an instance property instead:

```javascript
class UserList {
  constructor() {
    this.users = [];
  }

  addUser(name) {
    this.users.push(name);
  }
}
```

## Best practices

- **Use static methods for named constructors**: `fromObject()` and `fromArray()` make alternative inputs clear.
- **Use static properties for shared constants**: Keep values like `minLength` or `platform` on the class when they apply to the class as a whole.
- **Do not put instance-specific data in static properties**: Instance data belongs on `this` inside the constructor.
- **Do not use static methods as a dumping ground**: Keep static members closely related to the class they are attached to.
- **Prefer plain module-level functions** when the helper does not belong to a class concept.
- **Call static members on the class**: Use `User.fromObject(...)`, not `user.fromObject(...)`.

## Summary

Static members belong to the class, not to individual instances. Use static methods for factory methods and class-level utilities. Use static properties for values shared by the class as a whole. If a method needs data from one specific object, make it an instance method instead.

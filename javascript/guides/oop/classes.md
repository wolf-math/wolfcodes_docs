---
title: Classes and Instances
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are classes and instances?

A **class** is a blueprint for creating objects. An **instance** is an object created from that class.

Classes let you define one reusable shape, then create many objects that follow that shape.

```javascript
class Car {
  constructor(make) {
    this.make = make;
  }
}

const myCar = new Car("Toyota");

console.log(myCar.make); // "Toyota"
```

`Car` is the class. `myCar` is an instance.

## Why this matters

Classes are useful when you need many objects with the same shape and behavior. Instead of manually creating similar objects over and over, you define the structure once in a class and create instances with `new`.

## Creating instances with `new`

Use `new ClassName()` to create an instance:

```javascript
class Car {
  constructor(make) {
    this.make = make;
  }
}

const car1 = new Car("Toyota");
const car2 = new Car("Honda");

console.log(car1 === car2); // false
console.log(car1.make);     // "Toyota"
console.log(car2.make);     // "Honda"
```

Each call to `new Car()` creates a fresh object.

**What happens:**

1. JavaScript creates a new empty object.
2. The class constructor runs.
3. `this` points to the new object.
4. The finished object is assigned to the variable.

## The `constructor`

The `constructor` method is a special method that runs automatically when you create a new instance. Use it to set up instance data.

```javascript
class Car {
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
  }
}

const car = new Car("Toyota", "Camry", "Blue");

console.log(car.make);  // "Toyota"
console.log(car.model); // "Camry"
console.log(car.color); // "Blue"
```

Arguments passed to `new Car(...)` become arguments to `constructor`.

The constructor should usually set up the object's starting state. Keep it predictable and avoid doing unrelated work there.

:::warning
Call a class with `new`. Calling `Car("Toyota", "Camry", "Blue")` without `new` causes an error.
:::

## Instance properties

Instance properties store data on each individual object:

```javascript
class Car {
  constructor(make, model) {
    this.make = make;
    this.model = model;
    this.mileage = 0;
  }
}

const car1 = new Car("Toyota", "Camry");
const car2 = new Car("Honda", "Civic");

car1.mileage = 100;

console.log(car1.mileage); // 100
console.log(car2.mileage); // 0
```

Changing one instance does not change another instance.

This is the main mental model for instances: each instance has its own property values.

## Adding properties manually

JavaScript objects are flexible, so you can add properties after creation:

```javascript
class Car {}

const car = new Car();
car.make = "Toyota";
car.model = "Camry";

console.log(car.make); // "Toyota"
```

This works, but it is easy to forget a property or create inconsistent objects. Prefer setting expected properties in the constructor.

```javascript
class Car {
  constructor(make, model) {
    this.make = make;
    this.model = model;
  }
}

const car = new Car("Toyota", "Camry");

console.log(car.model); // "Camry"
```

**Rule of thumb:** if every instance should have the property, initialize it in the constructor.

## Missing properties

If you read a property that does not exist, JavaScript returns `undefined`:

```javascript
class Car {
  constructor(make) {
    this.make = make;
  }
}

const car = new Car("Toyota");

console.log(car.year); // undefined
```

Use `in` or `Object.hasOwn()` when you need to check for a property:

```javascript
if ("year" in car) {
  console.log(car.year);
} else {
  console.log("No year set");
}
```

Use this kind of check when missing data is expected. If the property should always exist, it is usually better to initialize it in the constructor.

## Instance methods

Methods are functions defined inside a class. They usually work with instance data through `this`.

```javascript
class Car {
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
    this.mileage = 0;
  }

  drive(miles) {
    this.mileage += miles;
    return this.mileage;
  }

  getInfo() {
    return `${this.color} ${this.make} ${this.model}`;
  }
}

const car = new Car("Toyota", "Camry", "Blue");

console.log(car.drive(100)); // 100
console.log(car.getInfo());  // "Blue Toyota Camry"
```

Instance methods are shared through the class, but they work with the specific instance that calls them.

The next guide covers methods and `this` in more detail.

## Class names and file organization

Class names usually use **PascalCase**, where each word starts with a capital letter:

```javascript
class UserAccount {}
class ShoppingCart {}
class GamePlayer {}
```

Use names that describe the kind of object the class creates. `UserAccount` is clearer than `Data` or `Manager` when the class represents a user account.

In larger programs, it is common to put one main class in its own module:

```javascript
// UserAccount.js
export class UserAccount {
  constructor(name) {
    this.name = name;
  }
}
```

This keeps the class easy to find and reuse.

## Common patterns

### Default property values

```javascript
class Task {
  constructor(title) {
    this.title = title;
    this.isComplete = false;
  }
}

const task = new Task("Learn classes");

console.log(task.isComplete); // false
```

### Creating multiple instances

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
}

const users = [
  new User("Alice"),
  new User("Bob"),
  new User("Charlie"),
];

console.log(users[0].name); // "Alice"
```

Use this pattern when you need a collection of similar objects.

### Checking an instance's class

```javascript
class User {}

const user = new User();

console.log(user instanceof User); // true
```

`instanceof` checks whether an object was created by a class or inherits from it. It is useful for debugging and occasional validation, but most everyday code works better by calling methods or checking the data you actually need.

## Common mistakes

### Forgetting `new`

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
}

// This would cause an error:
// const user = User("Alice");

const user = new User("Alice");

console.log(user.name); // "Alice"
```

### Sharing state accidentally

Be careful with object or array values that are meant to belong to each instance.

```javascript
const sharedSongs = [];

class Playlist {
  constructor(name) {
    this.name = name;
    this.songs = sharedSongs;
  }
}

const roadTrip = new Playlist("Road trip");
const focus = new Playlist("Focus");

roadTrip.songs.push("Song A");

console.log(focus.songs); // ["Song A"]
```

Both playlists point at the same array. That is usually not what you want.

Create arrays and objects inside the constructor when each instance needs its own copy:

```javascript
class Playlist {
  constructor(name) {
    this.name = name;
    this.songs = [];
  }

  addSong(song) {
    this.songs.push(song);
  }
}

const roadTrip = new Playlist("Road trip");
const focus = new Playlist("Focus");

roadTrip.addSong("Song A");

console.log(roadTrip.songs); // ["Song A"]
console.log(focus.songs);    // []
```

## Best practices

- **Use classes for repeated shapes**: Classes are useful when many objects share the same setup and behavior.
- **Initialize expected properties in `constructor`**: This keeps instances consistent.
- **Use `this` for instance data**: `this.name` means the `name` property on the current instance.
- **Avoid adding random properties later** unless the object is intentionally flexible.
- **Keep constructors simple**: Heavy work usually belongs in methods or helper functions.
- **Use clear class names**: Class names usually use PascalCase, like `UserAccount`.

## Summary

Classes are blueprints, and instances are objects created from those blueprints. Use `new` to create an instance, `constructor` to initialize instance data, and `this` to store properties on the current instance. Each instance has its own state, while methods define shared behavior.

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

Static properties and methods belong to the class itself.

They do not belong to individual instances.

## Why static members matter

Most class methods describe something an instance can do.

Static methods describe something the class can do.

That makes them useful for factory methods, utility methods, and shared values that do not depend on one specific object.

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

const user = new User("Maya");

console.log(user.greet());
```

`greet` needs a specific user's `name`, so it belongs on the instance.

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

console.log(user.name);
```

`fromObject` is called on `User`, not on a user instance.

It creates and returns a new instance.

## Static properties

Static properties store values on the class.

```javascript
class Course {
  static platform = "Wolf Codes";

  constructor(title) {
    this.title = title;
  }
}

console.log(Course.platform);
```

This is useful for values that are shared by the class as a whole.

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

console.log(point);
console.log(origin);
```

Factory methods are helpful when the constructor would become unclear or too crowded.

## Utility methods

A static method can also be a utility related to the class.

```javascript
class Temperature {
  static celsiusToFahrenheit(celsius) {
    return (celsius * 9) / 5 + 32;
  }
}

console.log(Temperature.celsiusToFahrenheit(20));
```

This method does not need instance state.

It can live on the class as a named utility.

## Accessing static members

Static members are accessed through the class name.

```javascript
class Counter {
  static description = "Counts things";
}

console.log(Counter.description);
```

Instances do not automatically expose static members.

```javascript
class Counter {
  static description = "Counts things";
}

const counter = new Counter();

console.log(counter.description);
```

This prints `undefined`.

## Common patterns

Use static methods for `fromJSON`, `fromObject`, `fromArray`, or other named ways to create instances.

Use static properties for shared constants.

Use instance methods when the method needs data from `this`.

## Best practices

Do not put instance-specific data in static properties.

Do not use static methods as a dumping ground for unrelated helper functions.

Keep static members closely related to the class they are attached to.

Prefer plain module-level functions when the helper does not belong to a class concept.

## Summary

Static members belong to the class, not to individual instances.

Use static methods for factory methods and class-level utilities.

Use static properties for values shared by the class as a whole.

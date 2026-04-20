---
title: Inheritance
sidebar_position: 4
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Inheritance lets one class build on another class.

The child class gets behavior from the parent class and can add or replace behavior of its own.

## Why inheritance matters

Inheritance can reduce duplication when several classes share the same core behavior.

It works best when the relationship is truly an **is-a** relationship.

A `Dog` is an `Animal`. A `SavingsAccount` is an `Account`. A `VideoLesson` is a `Lesson`.

If the relationship feels more like **has-a**, composition is usually a better fit.

## Extending a class

Use `extends` to create a child class.

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a sound.`;
  }
}

class Dog extends Animal {
  wagTail() {
    return `${this.name} wags its tail.`;
  }
}

const dog = new Dog("Maple");

console.log(dog.speak());
console.log(dog.wagTail());
```

`Dog` inherits the constructor and `speak` method from `Animal`.

It also adds its own `wagTail` method.

## Calling the parent constructor

If a child class defines its own constructor, it must call `super()` before using `this`.

```javascript
class Lesson {
  constructor(title) {
    this.title = title;
  }
}

class VideoLesson extends Lesson {
  constructor(title, durationInMinutes) {
    super(title);
    this.durationInMinutes = durationInMinutes;
  }
}

const lesson = new VideoLesson("Objects", 12);

console.log(lesson.title);
console.log(lesson.durationInMinutes);
```

`super(title)` runs the parent constructor.

After that, the child constructor can set its own properties.

## Overriding methods

A child class can define a method with the same name as a parent method.

This is called overriding.

```javascript
class Notification {
  send() {
    return "Sending notification.";
  }
}

class EmailNotification extends Notification {
  send() {
    return "Sending email notification.";
  }
}

const notification = new EmailNotification();

console.log(notification.send());
```

The child version replaces the parent version for instances of the child class.

## Calling a parent method

Use `super.methodName()` when the child method should reuse the parent behavior.

```javascript
class Report {
  print() {
    return "Printing report";
  }
}

class DetailedReport extends Report {
  print() {
    return `${super.print()} with details`;
  }
}

const report = new DetailedReport();

console.log(report.print());
```

This is useful when the child class wants to extend behavior instead of replacing it completely.

## Inheritance chains

A class can inherit from a class that already inherits from another class.

```javascript
class Shape {
  describe() {
    return "This is a shape.";
  }
}

class Rectangle extends Shape {}

class Square extends Rectangle {}

const square = new Square();

console.log(square.describe());
```

This works, but deep inheritance chains can become difficult to understand.

Prefer shallow inheritance.

## Composition as an alternative

Composition means giving an object another object or function to use.

```javascript
class Logger {
  log(message) {
    console.log(message);
  }
}

class OrderService {
  constructor(logger) {
    this.logger = logger;
  }

  createOrder(item) {
    this.logger.log(`Creating order for ${item}`);
  }
}

const service = new OrderService(new Logger());

service.createOrder("coffee");
```

`OrderService` has a logger.

It does not need to inherit from `Logger`.

## Common patterns

Use inheritance for specialized versions of a shared concept.

Use method overriding when child classes need different behavior for the same action.

Use `super` when the parent behavior is still useful.

Use composition when behavior needs to be mixed, swapped, or reused across unrelated classes.

## Best practices

Keep inheritance trees shallow.

Do not use inheritance only to share a helper method.

Ask whether the child class truly is a kind of the parent class.

If several subclasses override most of the parent methods, the inheritance model may be fighting the problem.

## Summary

Inheritance lets child classes reuse and specialize parent class behavior.

Use `extends` to create a child class and `super` to call parent constructors or methods.

Inheritance is useful for clear **is-a** relationships, but composition is often better for flexible behavior.

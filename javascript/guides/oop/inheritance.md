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

## What is inheritance?

**Inheritance** lets one class build on another class. The child class gets behavior from the parent class and can add or replace behavior of its own.

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

console.log(dog.speak());   // "Maple makes a sound."
console.log(dog.wagTail()); // "Maple wags its tail."
```

`Dog` inherits the constructor and `speak()` method from `Animal`. It also adds its own `wagTail()` method.

**What happens:**

1. `class Dog extends Animal` makes `Dog` a child class of `Animal`.
2. `new Dog("Maple")` uses the inherited `Animal` constructor.
3. The `dog` instance can use methods from both `Animal` and `Dog`.

## Why inheritance matters

Inheritance can reduce duplication when several classes share the same core behavior.

It works best when the relationship is truly an **is-a** relationship.

A `Dog` is an `Animal`. A `SavingsAccount` is an `Account`. A `VideoLesson` is a `Lesson`.

If the relationship feels more like **has-a**, composition is usually a better fit.

**Rule of thumb:** use inheritance when the child is a more specific kind of the parent. Use composition when one object simply uses another object.

## Extending a class

Use `extends` to create a child class.

```javascript
class User {
  constructor(name) {
    this.name = name;
  }

  getProfile() {
    return this.name;
  }
}

class AdminUser extends User {
  deletePost(postId) {
    return `Deleted post ${postId}`;
  }
}

const admin = new AdminUser("Dirk");

console.log(admin.getProfile());    // "Dirk"
console.log(admin.deletePost(123)); // "Deleted post 123"
```

`AdminUser` inherits the constructor and `getProfile()` method from `User`.

It also adds its own `deletePost()` method.

## The inheritance mental model

When JavaScript looks for a method, it starts on the instance's class. If it does not find the method there, it looks up the inheritance chain.

```javascript
class Animal {
  eat() {
    return "Eating";
  }
}

class Dog extends Animal {
  bark() {
    return "Woof";
  }
}

const dog = new Dog();

console.log(dog.bark()); // "Woof"
console.log(dog.eat());  // "Eating"
```

`bark()` comes from `Dog`. `eat()` comes from `Animal`.

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

console.log(lesson.title);             // "Objects"
console.log(lesson.durationInMinutes); // 12
```

`super(title)` runs the parent constructor.

After that, the child constructor can set its own properties.

**In a child constructor, `super()` must run before you use `this`.**

The following code without `super()` first would cause an error:

```javascript
class VideoLesson extends Lesson {
  constructor(title, durationInMinutes) {
    // This would cause an error because `super()` has not run yet:
    // this.durationInMinutes = durationInMinutes;

    super(title);
    this.durationInMinutes = durationInMinutes;
  }
}
```


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

console.log(notification.send()); // "Sending email notification."
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

console.log(report.print()); // "Printing report with details"
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

console.log(square.describe()); // "This is a shape."
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

service.createOrder("coffee"); // Logs "Creating order for coffee"
```

`OrderService` has a logger.

It does not need to inherit from `Logger`.

Composition is usually more flexible because you can swap the helper object without changing the class hierarchy.

## When inheritance is a poor fit

Inheritance is easy to overuse. If the parent and child relationship is not clear, the code can become harder to change.

```javascript
class Logger {
  log(message) {
    console.log(message);
  }
}

// Weak model: an OrderService is not really a Logger.
class OrderService extends Logger {
  createOrder(item) {
    this.log(`Creating order for ${item}`);
  }
}
```

This only uses inheritance to borrow a helper method. Composition is clearer:

```javascript
class OrderService {
  constructor(logger) {
    this.logger = logger;
  }

  createOrder(item) {
    this.logger.log(`Creating order for ${item}`);
  }
}
```

If the class only wants to use another object's behavior, give it that object instead of extending it.

## Common patterns

### Specialized versions of a shared concept

Use inheritance for specialized versions of a shared concept.

```javascript
class Lesson {
  constructor(title) {
    this.title = title;
  }

  getLabel() {
    return this.title;
  }
}

class QuizLesson extends Lesson {
  constructor(title, questionCount) {
    super(title);
    this.questionCount = questionCount;
  }

  getLabel() {
    return `${super.getLabel()} (${this.questionCount} questions)`;
  }
}

const lesson = new QuizLesson("Inheritance", 5);

console.log(lesson.getLabel()); // "Inheritance (5 questions)"
```

`QuizLesson` is a kind of `Lesson`, so inheritance fits.

### Different behavior for the same action

Use method overriding when child classes need different behavior for the same action.

```javascript
class PaymentMethod {
  getFee() {
    return 0;
  }
}

class CreditCardPayment extends PaymentMethod {
  getFee() {
    return 2.5;
  }
}

class BankTransferPayment extends PaymentMethod {
  getFee() {
    return 0.5;
  }
}

const cardPayment = new CreditCardPayment();
const transferPayment = new BankTransferPayment();

console.log(cardPayment.getFee());     // 2.5
console.log(transferPayment.getFee()); // 0.5
```

Each payment method understands the same action, but the details differ.

### Reusing part of the parent behavior

Use `super.methodName()` when the parent behavior is still useful.

```javascript
class Message {
  format() {
    return "Message";
  }
}

class UrgentMessage extends Message {
  format() {
    return `Urgent: ${super.format()}`;
  }
}

const message = new UrgentMessage();

console.log(message.format()); // "Urgent: Message"
```

## Best practices

- **Use inheritance for clear is-a relationships**: A `Dog` is an `Animal`; an `OrderService` is not a `Logger`.
- **Keep inheritance trees shallow**: One parent-child layer is easier to understand than a long chain.
- **Call `super()` first in child constructors**: Use it before touching `this`.
- **Use `super.methodName()` to extend behavior**: Use it when the parent method is still helpful.
- **Do not inherit only to share a helper method**: Use composition or a plain function instead.
- **Watch for repeated overrides**: If subclasses override most parent methods, the model may be fighting the problem.

## Summary

Inheritance lets child classes reuse and specialize parent class behavior. Use `extends` to create a child class and `super` to call parent constructors or methods. Inheritance works best for clear **is-a** relationships, but composition is often better when behavior needs to be mixed, swapped, or reused across unrelated classes.

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

Inheritance lets you create new classes that build on existing ones. Use it to share behavior when classes have a clear **is-a** relationship.

## What inheritance is

- A child class extends a parent class.
- The child **is a** more specific version of the parent.

## `extends`

- Use `extends` to inherit behavior and state.

```javascript
class Animal {
  speak() {
    console.log("Some sound");
  }
}

class Dog extends Animal {
  speak() {
    console.log("Woof");
  }
}
```

## `super`

- Call `super()` in the child constructor to run the parent constructor.
- Use `super.methodName()` to reuse parent methods.

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(`${this.name} makes a noise`);
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name);
  }
  speak() {
    super.speak(); // optional: call parent behavior
    console.log(`${this.name} barks`);
  }
}
```

## Method overriding

- Child classes can replace inherited methods.
- Use overriding when behavior truly differs.

## Inheritance cautions

- Avoid deep hierarchies—they become hard to change.
- Prefer composition over inheritance when:
  - Behavior varies a lot between instances.
  - You need to mix features (composition is more flexible).

---
title: Class
sidebar_position: 20
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## Definition

The `class` keyword is used to declare a class in JavaScript. Classes are syntactic sugar over JavaScript's existing prototype-based inheritance, providing a cleaner way to create objects and handle inheritance.

```javascript
class MyClass {}
typeof MyClass  // "function" (classes are functions)
```

## Class declaration

```javascript
class Person {
  constructor(name) {
    this.name = name
  }
  
  greet() {
    return `Hello, I'm ${this.name}`
  }
}

const person = new Person('Alice')
person.greet()  // "Hello, I'm Alice"
```

## Class components

### Constructor

```javascript
class Person {
  constructor(name, age) {
    this.name = name
    this.age = age
  }
}
```

### Methods

```javascript
class Person {
  constructor(name) {
    this.name = name
  }
  
  greet() {
    return `Hello, I'm ${this.name}`
  }
  
  getAge() {
    return this.age
  }
}
```

### Static Methods

```javascript
class Math {
  static add(a, b) {
    return a + b
  }
}

Math.add(1, 2)  // 3
```

### Getters and Setters

```javascript
class Person {
  constructor(name) {
    this._name = name
  }
  
  get name() {
    return this._name
  }
  
  set name(value) {
    this._name = value
  }
}
```

## Inheritance

### extends

```javascript
class Animal {
  constructor(name) {
    this.name = name
  }
  
  speak() {
    return 'Some sound'
  }
}

class Dog extends Animal {
  speak() {
    return 'Woof!'
  }
}

const dog = new Dog('Buddy')
dog.speak()  // "Woof!"
```

### super

```javascript
class Animal {
  constructor(name) {
    this.name = name
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name)  // Call parent constructor
    this.breed = breed
  }
}
```

## Private fields (es2022)

```javascript
class Person {
  #privateField = 'secret'
  
  getPrivate() {
    return this.#privateField
  }
}

const person = new Person()
person.#privateField  // SyntaxError
person.getPrivate()   // "secret"
```

## Class expressions

```javascript
const Person = class {
  constructor(name) {
    this.name = name
  }
}
```

## Best practices

1. **Use classes for OOP**: When you need object-oriented patterns.

2. **Understand prototype chain**: Classes are syntactic sugar over prototypes.

3. **Use extends for inheritance**: Cleaner than manual prototype manipulation.

4. **Call super() in derived constructors**: Required before using `this`.

5. **Consider composition over inheritance**: Sometimes composition is better than deep inheritance chains.


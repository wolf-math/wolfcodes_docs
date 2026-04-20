---
title: Encapsulation
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Encapsulation means keeping an object's internal details behind a clear public interface.

Instead of letting the rest of your program change every piece of data directly, you decide which actions are allowed.

## Why encapsulation matters

Encapsulation helps you protect the rules of an object.

A bank account should not have its balance changed to a random negative number. A user email should not be stored if it is missing an `@` symbol. A shopping cart should not let outside code quietly replace its item list with invalid data.

Encapsulation gives you one place to enforce those rules.

## Public fields

Public fields and properties can be read or changed from outside the object.

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
}

const user = new User("Maya");

user.name = "Nia";

console.log(user.name);
```

This is simple and useful when the data does not need protection.

## Private fields

Private fields start with `#`.

They can only be used inside the class that defines them.

```javascript
class BankAccount {
  #balance = 0;

  deposit(amount) {
    if (amount <= 0) {
      throw new Error("Amount must be positive");
    }

    this.#balance += amount;
  }

  getBalance() {
    return this.#balance;
  }
}

const account = new BankAccount();

account.deposit(50);

console.log(account.getBalance());
```

Outside code cannot access `#balance` directly.

That means every change to the balance has to go through a method like `deposit`.

## A public interface

The public interface is the set of methods and properties outside code is supposed to use.

```javascript
class Cart {
  #items = [];

  addItem(name, price) {
    if (price < 0) {
      throw new Error("Price cannot be negative");
    }

    this.#items.push({ name, price });
  }

  getTotal() {
    return this.#items.reduce((total, item) => total + item.price, 0);
  }

  getItemCount() {
    return this.#items.length;
  }
}

const cart = new Cart();

cart.addItem("Notebook", 8);
cart.addItem("Pen", 2);

console.log(cart.getTotal());
console.log(cart.getItemCount());
```

The code using `Cart` does not need to know how the items are stored.

It only needs to know how to add an item and ask for the total.

## Getters

A getter lets code read a value like a property while still letting the class control how the value is produced.

```javascript
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  get area() {
    return this.width * this.height;
  }
}

const rectangle = new Rectangle(5, 4);

console.log(rectangle.area);
```

Use getters for values that are derived from other state.

## Setters

A setter lets code assign a value like a property while still letting the class validate it.

```javascript
class User {
  #email;

  constructor(email) {
    this.email = email;
  }

  get email() {
    return this.#email;
  }

  set email(value) {
    if (!value.includes("@")) {
      throw new Error("Invalid email");
    }

    this.#email = value.toLowerCase();
  }
}

const user = new User("MAYA@example.com");

console.log(user.email);

user.email = "nia@example.com";
```

Setters are useful when a value should look like a normal property, but still needs rules.

## Protecting invariants

An invariant is a rule that should always stay true.

For example, an account balance should never become negative if withdrawals are not allowed to overdraw the account.

```javascript
class Account {
  #balance;

  constructor(startingBalance) {
    if (startingBalance < 0) {
      throw new Error("Starting balance cannot be negative");
    }

    this.#balance = startingBalance;
  }

  withdraw(amount) {
    if (amount > this.#balance) {
      throw new Error("Insufficient funds");
    }

    this.#balance -= amount;
  }

  get balance() {
    return this.#balance;
  }
}
```

Because `#balance` is private, outside code cannot skip the withdrawal rules.

## Common patterns

Use private fields for state that must stay valid.

Use public methods for actions the rest of the program is allowed to take.

Use getters for read-only computed values.

Use setters only when property-style assignment makes the code clearer.

## Best practices

Keep the public interface small.

Do not make every property private by default. Use privacy when it protects a real rule or makes the class easier to change.

Avoid returning private arrays or objects directly if outside code could mutate them.

```javascript
class Playlist {
  #songs = [];

  addSong(title) {
    this.#songs.push(title);
  }

  getSongs() {
    return [...this.#songs];
  }
}
```

Returning a copy protects the private array from accidental outside changes.

## Summary

Encapsulation keeps object internals behind a clear interface.

Private fields protect data that should not be changed directly.

Methods, getters, and setters give you controlled ways to read, update, and validate object state.

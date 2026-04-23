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

## What is encapsulation?

**Encapsulation** means keeping an object's internal details behind a clear public interface.

Instead of letting the rest of your program change every piece of data directly, you decide which actions are allowed.

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

console.log(account.getBalance()); // 50
```

The private field `#balance` can only be changed through methods the class provides.

**What happens:**

1. Outside code calls `deposit(50)`.
2. The method validates the amount.
3. The method updates the private `#balance` field.
4. Outside code reads the balance through `getBalance()`.

## Why encapsulation matters

Encapsulation helps you protect the rules of an object.

A bank account should not have its balance changed to a random negative number. A user email should not be stored if it is missing an `@` symbol. A shopping cart should not let outside code quietly replace its item list with invalid data.

Encapsulation gives you one place to enforce those rules.

It also makes code easier to change. If the inside of a class changes later, the rest of the program can keep using the same public methods.

## Public fields

Public fields and properties can be read or changed from outside the object.

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
}

const user = new User("Dirk");

user.name = "Nia";

console.log(user.name); // "Nia"
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

console.log(account.getBalance()); // 50
```

Outside code cannot access `#balance` directly.

That means every change to the balance has to go through a method like `deposit`.

```javascript
// This would cause an error:
// console.log(account.#balance);
```

Private fields are enforced by JavaScript itself. They are not just a naming convention.

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

console.log(cart.getTotal());     // 10
console.log(cart.getItemCount()); // 2
```

The code using `Cart` does not need to know how the items are stored.

It only needs to know how to add an item and ask for the total.

**Rule of thumb:** the public interface should describe what outside code can do, not how the class stores its data.

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

console.log(rectangle.area); // 20
```

Use getters for values that are derived from other state.

Getters should usually be simple and predictable. Avoid using a getter for work that changes state or surprises the caller.

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

const user = new User("DIRK@example.com");

console.log(user.email); // "dirk@example.com"

user.email = "nia@example.com";

console.log(user.email); // "nia@example.com"
```

Setters are useful when a value should look like a normal property, but still needs rules.

Use setters carefully. If assigning a value does something complicated, a method like `changeEmail()` may be clearer.

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

const account = new Account(100);

account.withdraw(30);

console.log(account.balance); // 70
```

Because `#balance` is private, outside code cannot skip the withdrawal rules.

## Returning private data safely

Private fields protect the field itself, but arrays and objects can still be mutated if you return them directly.

```javascript
class Playlist {
  #songs = [];

  addSong(title) {
    this.#songs.push(title);
  }

  getSongs() {
    return this.#songs;
  }
}

const playlist = new Playlist();

playlist.addSong("Song A");

const songs = playlist.getSongs();
songs.push("Unexpected song");

console.log(playlist.getSongs()); // ["Song A", "Unexpected song"]
```

The outside code changed the private array because `getSongs()` returned the actual array.

Return a copy when outside code should not be able to mutate the internal value:

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

const playlist = new Playlist();

playlist.addSong("Song A");

const songs = playlist.getSongs();
songs.push("Unexpected song");

console.log(playlist.getSongs()); // ["Song A"]
```

Returning a copy protects the private array from accidental outside changes.

## Common patterns

### Private state with public actions

Use private fields for state that must stay valid, and public methods for actions the rest of the program is allowed to take.

```javascript
class Counter {
  #value = 0;

  increment() {
    this.#value += 1;
  }

  getValue() {
    return this.#value;
  }
}
```

### Read-only computed values

Use getters for values that are calculated from other state.

```javascript
class Cart {
  #items = [];

  addItem(price) {
    this.#items.push(price);
  }

  get total() {
    return this.#items.reduce((sum, price) => sum + price, 0);
  }
}
```

### Validated assignment

Use setters only when property-style assignment makes the code clearer.

```javascript
class Profile {
  #displayName;

  set displayName(value) {
    if (!value.trim()) {
      throw new Error("Display name is required");
    }

    this.#displayName = value.trim();
  }

  get displayName() {
    return this.#displayName;
  }
}
```

## Best practices

- **Keep the public interface small**: Expose the methods and properties other code actually needs.
- **Use private fields to protect real rules**: Do not make every property private by default.
- **Validate before changing state**: Check inputs before updating private fields.
- **Prefer methods for actions**: Use names like `deposit()`, `addItem()`, and `markComplete()`.
- **Use getters for simple reads**: Derived values like `total` or `area` are good getter candidates.
- **Use setters sparingly**: If assignment hides too much behavior, use a clearly named method instead.
- **Return copies of private arrays or objects** when outside code should not mutate them.

Privacy is a tool for clarity and safety. Use it when it helps the class protect its own state.

## Summary

Encapsulation keeps object internals behind a clear interface. Private fields protect data that should not be changed directly, while methods, getters, and setters give controlled ways to read, update, and validate object state. Use encapsulation when it protects real rules or makes the class easier to change safely.

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

Encapsulation hides internal details and exposes a clear interface. It helps prevent accidental misuse and keeps invariants intact.

## What is encapsulation?

- Keep internal details private.
- Expose only what callers need.
- Protect invariants (rules your object must always satisfy).

## Public vs private data

- Public fields are accessible from anywhere.
- Private fields start with `#` and are only accessible inside the class.

```javascript
class BankAccount {
  #balance = 0; // private field
  deposit(amount) {
    if (amount <= 0) throw new Error("Amount must be positive");
    this.#balance += amount;
  }
  getBalance() {
    return this.#balance;
  }
}
```

Private fields are not enumerable and cannot be accessed outside the class. Note: older environments may need transpilation for `#private`.

## Getters and setters

Use getters/setters to expose computed or validated properties.

```javascript
class User {
  #email;
  constructor(email) {
    this.email = email; // uses setter
  }
  get email() {
    return this.#email.toLowerCase();
  }
  set email(value) {
    if (!value.includes("@")) throw new Error("Invalid email");
    this.#email = value;
  }
}
```

Getters compute values on access; setters let you validate or transform input. Use them when you need control, otherwise keep plain fields.

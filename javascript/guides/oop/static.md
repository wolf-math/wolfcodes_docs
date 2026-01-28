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

Static members belong to the **class itself**, not to individual instances. Use them for behavior or data that is shared across all instances.

## What static members are

- Accessed on the class (`ClassName.method()`), not on instances.
- Useful for utilities, factories, or shared constants.

## Static methods

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
  static fromJSON(json) {
    return new User(json.name);
  }
}

const user = User.fromJSON({ name: "Alice" });
```

## Static properties

```javascript
class Config {
  static APP_NAME = "MyApp";
  static VERSION = "1.0.0";
}

console.log(Config.APP_NAME);
```

## When to use static members

- Use for:
  - Utility functions that don’t depend on instance state.
  - Factories that create instances (`fromJSON`, `fromId`, etc.).
  - Shared constants or configuration.
- Avoid for:
  - Per-instance data (belongs on `this`).
  - Behavior that depends on instance state.

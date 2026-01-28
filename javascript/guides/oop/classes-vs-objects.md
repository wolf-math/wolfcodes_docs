---
title: Classes vs Plain Objects
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Not everything needs a class. JavaScript’s plain objects are great for simple data. Use classes when you need shared behavior and multiple instances.

## Plain objects

- Best for data containers, configuration, and one-off structures.
- No methods required; just shape your data.

```javascript
const userConfig = {
  theme: "dark",
  language: "en",
};
```

## Classes

- Best for multiple instances that share behavior and manage state.
- Encapsulate data + methods together.

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
  greet() {
    return `Hello, ${this.name}!`;
  }
}
```

## Choosing the right tool

- Choose a plain object when:
  - You just need to group data.
  - There’s no shared behavior.
- Choose a class when:
  - You need methods and state together.
  - You will create multiple similar instances.

---
title: JSON
sidebar_position: 7.5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is JSON?

**JSON** (JavaScript Object Notation) is a text format for representing data. It is commonly used to send data between programs, like a browser and a server.

In JavaScript, JSON is usually a string:

```javascript
const jsonText = '{"name":"Maya","points":42}';

console.log(typeof jsonText); // "string"
```

JavaScript can convert between:

- JSON text (a string)
- JavaScript values (objects, arrays, strings, numbers, booleans, `null`)

## Why this matters

You will see JSON constantly in real programs:

- API responses and requests
- Configuration files
- Saving data to storage
- Logging and debugging structured data

The two core tools are:

- `JSON.stringify(value)` to convert a JavaScript value into JSON text
- `JSON.parse(text)` to convert JSON text into a JavaScript value

## Converting values to JSON: `JSON.stringify()`

Use `JSON.stringify()` to convert a JavaScript value into JSON text:

```javascript
const user = { name: "Maya", points: 42 };

const jsonText = JSON.stringify(user);

console.log(jsonText); // {"name":"Maya","points":42}
```

### Pretty printing

You can format JSON with indentation for readability:

```javascript
const user = { name: "Maya", points: 42, tags: ["admin", "beta"] };

console.log(JSON.stringify(user, null, 2));
```

**Output:**

```text
{
  "name": "Maya",
  "points": 42,
  "tags": [
    "admin",
    "beta"
  ]
}
```

## Converting JSON to values: `JSON.parse()`

Use `JSON.parse()` to convert JSON text into a JavaScript value:

```javascript
const jsonText = '{"name":"Maya","points":42}';

const user = JSON.parse(jsonText);

console.log(user.name);   // "Maya"
console.log(user.points); // 42
```

If the JSON is invalid, `JSON.parse()` throws an error.

```javascript
try {
  JSON.parse("{ bad json }");
} catch (error) {
  console.log(error.name); // "SyntaxError"
}
```

## What JSON can represent

JSON supports a smaller set of data types than JavaScript.

JSON values can be:

- Objects (with string keys)
- Arrays
- Strings
- Numbers
- Booleans
- `null`

JSON cannot represent:

- `undefined`
- Functions
- `Symbol`
- `BigInt`
- Class instances with methods

**Rule of thumb:** JSON is for plain data, not behavior.

## Common gotchas

### `undefined` and functions are not preserved

When you stringify an object, values that are `undefined` or functions are omitted:

```javascript
const user = {
  name: "Maya",
  email: undefined,
  greet() {
    return "Hi";
  },
};

console.log(JSON.stringify(user)); // {"name":"Maya"}
```

In arrays, `undefined` becomes `null`:

```javascript
console.log(JSON.stringify([1, undefined, 3])); // [1,null,3]
```

### `NaN` and `Infinity` become `null`

JSON does not support `NaN` or infinity. They are converted to `null` when stringified:

```javascript
console.log(JSON.stringify({ value: NaN }));      // {"value":null}
console.log(JSON.stringify({ value: Infinity })); // {"value":null}
```

### Dates become strings

JavaScript `Date` objects are stringified as ISO strings:

```javascript
const payload = { createdAt: new Date("2026-04-23T12:00:00Z") };

const jsonText = JSON.stringify(payload);

console.log(jsonText); // {"createdAt":"2026-04-23T12:00:00.000Z"}
```

When you parse the JSON back, you get a string, not a `Date` object:

```javascript
const parsed = JSON.parse(jsonText);

console.log(typeof parsed.createdAt); // "string"
```

### Circular references throw an error

If an object refers to itself, `JSON.stringify()` throws:

```javascript
const user = { name: "Maya" };
user.self = user;

// This would cause an error:
// JSON.stringify(user);
```

## Validating parsed JSON

`JSON.parse()` returns "some value". It does not guarantee the shape is what your program expects.

For beginner code, validate the shape you need with simple checks:

```javascript
function parseUser(jsonText) {
  const value = JSON.parse(jsonText);

  if (typeof value !== "object" || value === null) {
    throw new Error("Expected an object");
  }

  if (typeof value.name !== "string") {
    throw new Error("Expected name to be a string");
  }

  return { name: value.name };
}

const user = parseUser('{"name":"Maya"}');

console.log(user.name); // "Maya"
```

When invalid JSON is expected (like user input), `try/catch` around `JSON.parse()` is appropriate. The [errors guide](../control_flow/errors) covers `try/catch` in more detail.

## Common patterns

### Cloning plain data

For simple plain-data objects, you will sometimes see:

```javascript
const original = { name: "Maya", points: 42 };

const clone = JSON.parse(JSON.stringify(original));

console.log(clone); // { name: 'Maya', points: 42 }
```

:::warning
This is not a general cloning tool. It drops functions and `undefined`, converts dates to strings, and cannot handle circular references.
:::

For plain objects, prefer explicit copying patterns like object spread. The [rest and spread guide](./rest_and_spread) covers spread syntax in more detail.

```javascript
const original = { name: "Maya", points: 42 };
const copy = { ...original };
```

## Best practices

- **Treat JSON as data-only**: Use plain objects and arrays, not classes.
- **Always handle parse failures** when the input might be invalid: wrap `JSON.parse()` in `try/catch`.
- **Validate the shape you need** after parsing: check key types before using them.
- **Prefer explicit copying** over JSON-based cloning when possible.
- **Pretty print when helpful**: `JSON.stringify(value, null, 2)` is great for debugging output.

## Summary

JSON is a text format for data. Use `JSON.stringify()` to convert JavaScript values into JSON text, and `JSON.parse()` to convert JSON text into JavaScript values. JSON is best for plain data, so validate parsed values before using them and remember common gotchas like dates turning into strings and `undefined` being dropped.

---
title: Boolean
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
## Properties

<!-- ```javascript
> Object.getOwnPropertyNames(Boolean.prototype)
['constructor', 'toString', 'valueOf']
``` -->

## Definition

A `Boolean` is a logical value: `true` or `false`. It answers questions like "Is this statement correct?"

```javascript
> typeof true
"boolean"

> typeof false
"boolean"
```

## Using booleans

Booleans can be created using literals or the `Boolean` constructor:

```javascript
// Literal syntax
> true
true

> false
false

// Boolean constructor
> new Boolean(true)
[Boolean: true]

> Boolean(true)
true
```

### Truthy and falsy values

In JavaScript, values are automatically converted to booleans in boolean contexts. Some values are "truthy" (convert to `true`) and others are "falsy" (convert to `false`).

#### Falsy Values

These values evaluate to `false`:

| Value      | Type        | Notes                    |
| ---------- | ----------- | ------------------------ |
| `false`    | `boolean`   | The literal `false`      |
| `0`        | `number`    | Zero                     |
| `-0`       | `number`    | Negative zero            |
| `0n`       | `bigint`    | BigInt zero              |
| `""`       | `string`    | Empty string             |
| `null`     | `null`      | Represents "no value"     |
| `undefined`| `undefined` | Represents "not defined" |
| `NaN`      | `number`    | Not-a-Number             |

#### Truthy Values

Everything else is truthy, including:

| Value           | Type        | Notes                           |
| --------------- | ----------- | ------------------------------- |
| `true`          | `boolean`   | The literal `true`              |
| `1`             | `number`    | Any non-zero number             |
| `-1`            | `number`    | Negative numbers                |
| `"hello"`       | `string`    | Any non-empty string            |
| `"0"`           | `string`    | String "0" (string, not number) |
| `"false"`       | `string`    | String "false" (string, not boolean) |
| `[]`            | `array`     | Empty array                     |
| `{}`            | `object`    | Empty object                    |
| `function() {}` | `function`  | Functions                       |

## Operations on booleans

### Logical operators: Truth tables

#### The `&&` operator

Returns the first falsy value, or the last value if all are truthy.

| Expression        | Result | Explanation                    |
| ----------------- | ------ | ------------------------------ |
| `true && true`    | `true` | Both values are true           |
| `true && false`   | `false`| One is false                   |
| `false && true`   | `false`| One is false                   |
| `false && false`  | `false`| Both are false                 |

When used with non-boolean values, `&&` returns the first falsy value or the last truthy value:

| Expression           | Result      | Explanation                    |
| -------------------- | ----------- | ------------------------------ |
| `"hello" && "world"` | `"world"`   | Returns last truthy            |
| `"" && "world"`      | `""`        | Returns first falsy            |

#### The `||` operator

Returns the first truthy value, or the last value if all are falsy.

| Expression       | Result | Explanation                    |
| ---------------- | ------ | ------------------------------ |
| `true \|\| true`   | `true` | At least one is true           |
| `true \|\| false`  | `true` | First value is true            |
| `false \|\| true`  | `true` | Second value is true           |
| `false \|\| false` | `false`| Both are false                 |

When used with non-boolean values, `||` returns the first truthy value or the last falsy value:

| Expression          | Result    | Explanation                    |
| ------------------- | --------- | ------------------------------ |
| `"hello" \|\| "world"`| `"hello"` | Returns first truthy           |
| `"" \|\| "world"`     | `"world"` | Returns first truthy           |

#### The `!` operator

Returns the opposite boolean value.

| Expression | Result  | Explanation       |
| ---------- | ------- | ----------------- |
| `!true`    | `false` | Negates the value |
| `!false`   | `true`  | Negates the value |

When used with non-boolean values, `!` converts to boolean first, then negates:

| Expression | Result  | Explanation                    |
| ---------- | ------- | ------------------------------ |
| `!"hello"` | `false` | String is truthy, negated to false |
| `!""`      | `true`  | Empty string is falsy, negated to true |
| `!0`       | `true`  | Zero is falsy, negated to true |
| `!1`       | `false` | One is truthy, negated to false |

#### Double NOT (`!!`)

Converts a value to a boolean by negating twice.

| Expression  | Result | Explanation                    |
| ----------- | ------ | ------------------------------ |
| `!!"hello"` | `true` | Double negation converts to boolean |
| `!!""`      | `false`| Double negation converts to boolean |
| `!!0`       | `false`| Double negation converts to boolean |
| `!!1`       | `true` | Double negation converts to boolean |

### Comparison operations

Comparison operations return boolean values:

```javascript
// Equality
> 5 == 8
false

> 5 === 8
false

// Inequality
> 5 != 8
true

> 5 !== 8
true

// Greater than
> 5 > 8
false

// Less than
> 5 < 8
true

// Greater than or equal
> 5 >= 8
false

// Less than or equal
> 5 <= 8
true
```

### Boolean conversion

The `Boolean` constructor can convert values to booleans:

```javascript
> Boolean(1)
true

> Boolean(0)
false

> Boolean("hello")
true

> Boolean("")
false

> Boolean(null)
false

> Boolean(undefined)
false
```

## Boolean methods

### `toString()`

Converts a boolean to a string.

```javascript
> true.toString()
"true"

> false.toString()
"false"
```

### `valueOf()`

Returns the primitive value of a boolean object.

```javascript
> const bool = new Boolean(true)
undefined

> bool.valueOf()
true
```

---
title: RegExp
sidebar_position: 13
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

A `RegExp` (regular expression) is a pattern used to match character combinations in strings. Regular expressions are powerful tools for pattern matching and text manipulation.

```javascript
typeof /pattern/  // "object"
/pattern/ instanceof RegExp  // true
```

## Creating regular expressions

### Literal Syntax

```javascript
const regex = /pattern/
const regexWithFlags = /pattern/gi
```

### Constructor Syntax

```javascript
const regex = new RegExp('pattern')
const regexWithFlags = new RegExp('pattern', 'gi')
```

### Dynamic Patterns

Use constructor when pattern is dynamic:

```javascript
const pattern = 'hello'
const regex = new RegExp(pattern, 'i')
```

## Flags

Regular expressions can have flags that modify behavior:

- `g` - Global (find all matches, not just first)
- `i` - Case-insensitive
- `m` - Multiline
- `s` - Dotall (`.` matches newlines)
- `u` - Unicode
- `y` - Sticky

```javascript
/hello/gi  // Global and case-insensitive
```

## Common patterns

### Literal Characters

```javascript
/hello/  // Matches "hello"
```

### Character Classes

```javascript
/[abc]/        // Matches a, b, or c
/[a-z]/        // Matches any lowercase letter
/[0-9]/        // Matches any digit
/[^abc]/       // Matches anything except a, b, or c
/\d/           // Matches any digit (same as [0-9])
/\w/           // Matches word character (letter, digit, underscore)
/\s/           // Matches whitespace
```

### Quantifiers

```javascript
/a*/           // Zero or more a's
/a+/           // One or more a's
/a?/           // Zero or one a
/a{3}/         // Exactly 3 a's
/a{3,}/        // 3 or more a's
/a{3,5}/       // 3 to 5 a's
```

### Anchors

```javascript
/^hello/       // Starts with "hello"
/hello$/       // Ends with "hello"
/^hello$/      // Exactly "hello"
/\bword\b/    // Word boundary
```

### Groups

```javascript
/(abc)/        // Capturing group
/(?:abc)/     // Non-capturing group
/(a|b)/       // Alternation (a or b)
```

## Regexp methods

### `test()`

Tests whether a pattern matches a string:

```javascript
/hello/.test("hello world")  // true
/hello/.test("hi there")      // false
```

### `exec()`

Executes a search and returns match information:

```javascript
const regex = /hello/
const result = regex.exec("hello world")
// result is ["hello", index: 0, input: "hello world", groups: undefined]
```

## String methods with regexp

### `match()`

Returns matches:

```javascript
"hello world".match(/hello/)  // ["hello"]
"hello hello".match(/hello/g) // ["hello", "hello"]
```

### `search()`

Returns index of first match:

```javascript
"hello world".search(/world/)  // 6
"hello world".search(/xyz/)    // -1
```

### `replace()`

Replaces matches:

```javascript
"hello world".replace(/world/, "JavaScript")  // "hello JavaScript"
"hello hello".replace(/hello/g, "hi")          // "hi hi"
```

### `split()`

Splits string by pattern:

```javascript
"a,b,c".split(/,/)      // ["a", "b", "c"]
"hello world".split(/\s/) // ["hello", "world"]
```

## Common use cases

### Email Validation

```javascript
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
emailRegex.test("user@example.com")  // true
```

### Phone Number

```javascript
const phoneRegex = /^\+?[\d\s-()]+$/
phoneRegex.test("+1-555-123-4567")  // true
```

### Extract Numbers

```javascript
const numbers = "Price: $123.45".match(/\d+\.?\d*/)
// ["123.45"]
```

### Remove Whitespace

```javascript
"  hello  world  ".replace(/\s+/g, " ")  // " hello world "
```

## Best practices

1. **Use literal syntax when possible**: More readable and slightly faster.

2. **Be careful with special characters**: Escape special regex characters with `\`.

3. **Test your patterns**: Regular expressions can be tricky—test thoroughly.

4. **Consider performance**: Complex regex can be slow on large strings.

5. **Use flags appropriately**: `g` flag for multiple matches, `i` for case-insensitive.


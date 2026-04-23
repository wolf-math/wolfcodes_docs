---
title: Strings
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

## What are strings?

**Strings** are values that represent text. Use strings for names, messages, labels, URLs, file paths, and any other text in your program.

```javascript
const greeting = "Hello";
const name = "Alice";
const message = `Hello, ${name}!`;

console.log(message); // "Hello, Alice!"
```

Strings are primitive values and are **immutable**. String methods return new strings instead of changing the original string.

## Why this matters

Strings are everywhere in JavaScript: user input, page text, API responses, error messages, and configuration values. Understanding strings helps you build readable messages, search and transform text, handle whitespace, and avoid bugs with quotes, escaping, and case sensitivity.

## Creating strings

JavaScript has three common string literal forms:

```javascript
const single = 'single quotes';
const double = "double quotes";
const template = `template literal`;
```

Single and double quotes behave the same way. Choose one style and stay consistent in a project.

Template literals use backticks and support interpolation:

```javascript
const name = "Alice";
const message = `Hello, ${name}!`;

console.log(message); // "Hello, Alice!"
```

They also support multi-line strings:

```javascript
const text = `Line 1
Line 2
Line 3`;

console.log(text);
```

**Output:**

```text
Line 1
Line 2
Line 3
```

## Combining strings

Use `+` to concatenate strings:

```javascript
const firstName = "Alice";
const lastName = "Smith";
const fullName = firstName + " " + lastName;

console.log(fullName); // "Alice Smith"
```

For strings that include variables, prefer template literals:

```javascript
const name = "Alice";
const age = 30;
const message = `${name} is ${age} years old.`;

console.log(message); // "Alice is 30 years old."
```

Template literals are usually easier to read than long concatenation.

## Escaping characters

Use a backslash to escape characters with special meaning:

```javascript
const quote = "She said \"Hello\"";
const path = "C:\\Users\\Alice\\file.txt";
const lines = "Line 1\nLine 2";

console.log(quote); // She said "Hello"
console.log(path);  // C:\Users\Alice\file.txt
console.log(lines);
```

The `\n` escape creates a new line.

**Output from `lines`:**

```text
Line 1
Line 2
```

Often, you can avoid escaping quotes by using the other quote style:

```javascript
const sentence = "It's a nice day";
const quoted = 'She said "Hello"';

console.log(sentence); // "It's a nice day"
console.log(quoted);   // She said "Hello"
```

In template literals, escape backticks:

```javascript
const text = `Use \`backticks\` for template literals`;

console.log(text); // "Use `backticks` for template literals"
```

## String length and indexing

Use `.length` to get the number of characters:

```javascript
const word = "Hello";

console.log(word.length); // 5
```

Use bracket notation to access a character by index:

```javascript
const word = "Hello";

console.log(word[0]); // "H"
console.log(word[1]); // "e"
console.log(word[word.length - 1]); // "o"
```

String indexes start at `0`.

If an index does not exist, JavaScript returns `undefined`:

```javascript
const word = "Hello";

console.log(word[10]); // undefined
```

For most everyday strings, `.length` tells you how many characters are in the string. Some emoji and symbols can count differently because JavaScript stores strings as UTF-16 code units:

```javascript
console.log("A".length);  // 1
console.log("😊".length); // 2
```

You usually do not need to worry about this for beginner code, but it is useful to know when working with emoji-heavy text.

## Strings are immutable

String methods do not change the original string:

```javascript
const text = "hello";
const upper = text.toUpperCase();

console.log(text);  // "hello"
console.log(upper); // "HELLO"
```

Trying to change one character does not update the string:

```javascript
const text = "hello";

// This does not change the string:
// text[0] = "H";

console.log(text); // "hello"
```

To change text, create a new string.

## Common string methods

### Changing case

```javascript
const text = "Hello, World!";

console.log(text.toUpperCase()); // "HELLO, WORLD!"
console.log(text.toLowerCase()); // "hello, world!"
```

Use these before comparisons when case should not matter:

```javascript
const input = "ALICE";

if (input.toLowerCase() === "alice") {
  console.log("Match");
}
```

String comparisons are case-sensitive unless you normalize the values first:

```javascript
console.log("Alice" === "alice"); // false
console.log("Alice".toLowerCase() === "alice"); // true
```

### Searching strings

Use `includes()`, `startsWith()`, and `endsWith()` when you need a boolean:

```javascript
const text = "Hello, World!";

console.log(text.includes("World")); // true
console.log(text.startsWith("Hello")); // true
console.log(text.endsWith("!")); // true
```

Use `indexOf()` when you need the position:

```javascript
const text = "Hello, World!";

console.log(text.indexOf("World")); // 7
console.log(text.indexOf("JavaScript")); // -1
```

`indexOf()` returns `-1` when the text is not found.

String searches are case-sensitive:

```javascript
const text = "Hello, World!";

console.log(text.includes("World")); // true
console.log(text.includes("world")); // false
```

### Slicing strings

Use `slice()` to extract part of a string:

```javascript
const text = "Hello, World!";

console.log(text.slice(0, 5)); // "Hello"
console.log(text.slice(7));    // "World!"
console.log(text.slice(-6));   // "World!"
```

`slice(start, end)` includes `start` but does not include `end`.

### Replacing text

Use `replace()` for the first match and `replaceAll()` for every match:

```javascript
const text = "red, blue, red";

console.log(text.replace("red", "green")); // "green, blue, red"
console.log(text.replaceAll("red", "green")); // "green, blue, green"
```

### Splitting and joining

Use `split()` to turn a string into an array:

```javascript
const text = "apple,banana,cherry";
const fruits = text.split(",");

console.log(fruits); // ["apple", "banana", "cherry"]
```

Use `join()` on an array to build a string:

```javascript
const names = ["Alice", "Bob", "Charlie"];
const text = names.join(", ");

console.log(text); // "Alice, Bob, Charlie"
```

### Trimming whitespace

Use `trim()` to remove whitespace from both ends:

```javascript
const input = "  Alice  ";

console.log(input.trim());      // "Alice"
console.log(input.trimStart()); // "Alice  "
console.log(input.trimEnd());   // "  Alice"
```

This is especially useful for user input.

## Truthiness

Empty strings are falsy. Non-empty strings are truthy:

```javascript
const name = "";

if (!name) {
  console.log("Name is empty");
}
```

Be careful with strings like `"false"` and `"0"`. They are non-empty strings, so they are truthy:

```javascript
console.log(Boolean("false")); // true
console.log(Boolean("0"));     // true
```

If you need to parse `"true"` or `"false"`, compare explicitly:

```javascript
const input = "false";
const value = input === "true";

console.log(value); // false
```

## Common patterns

### Checking if a string is empty

```javascript
const text = "";

if (text.length === 0) {
  console.log("String is empty");
}
```

Use `text.trim().length === 0` if whitespace-only text should count as empty:

```javascript
const text = "   ";

if (text.trim().length === 0) {
  console.log("String is blank");
}
```

### Building display messages

```javascript
const itemCount = 3;
const message = `You have ${itemCount} items.`;

console.log(message); // "You have 3 items."
```

### Normalizing user input

```javascript
const input = "  ALICE@example.COM  ";
const email = input.trim().toLowerCase();

console.log(email); // "alice@example.com"
```

### Turning comma-separated text into values

```javascript
const input = "red, green, blue";
const colors = input.split(",").map((color) => color.trim());

console.log(colors); // ["red", "green", "blue"]
```

## Best practices

- **Prefer template literals**: They are clearer when strings include variables.
- **Use string methods intentionally**: Methods return new strings; they do not change the original.
- **Normalize before comparing**: Use `trim()` and `toLowerCase()` when input may vary.
- **Use `includes()` for presence checks**: It is clearer than `indexOf(...) !== -1`.
- **Use `join()` for arrays of text**: It avoids trailing separators.
- **Be explicit with blank strings**: Use `.length` or `.trim().length` depending on what "empty" means.
- **Remember case sensitivity**: Most string checks are case-sensitive.
- **Watch out for unusual characters**: Emoji and some symbols can make `.length` behave differently than you expect.

## Summary

Strings represent text in JavaScript. Create them with quotes or template literals, use indexes and `.length` to inspect them, and use methods like `slice()`, `includes()`, `replace()`, `split()`, `join()`, and `trim()` to work with text. Strings are immutable, so methods return new strings. For readable code, prefer template literals, normalize user input before comparing, and use explicit checks when empty strings matter.

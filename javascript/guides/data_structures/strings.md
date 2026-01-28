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

**Strings** are sequences of characters used to represent text. In JavaScript, strings are one of the primitive data types and are immutable (cannot be changed once created).

```javascript
const greeting = "Hello, World!";
const name = 'Alice';
const message = `Welcome`;
```

## String literals

JavaScript supports three ways to create string literals:

### Single quotes `'`

```javascript
const text = 'This is a string';
```

### Double quotes `"`

```javascript
const text = "This is also a string";
```

Single and double quotes work the same way. Choose one style and be consistent. If your string contains one type of quote, use the other:

```javascript
const message = "It's a beautiful day";  // Use double quotes for apostrophe
const quote = 'He said "Hello"';         // Use single quotes for quotes
```

### Template literals `` ` ``

Template literals (backticks) allow you to embed expressions and create multi-line strings:

```javascript
const name = "Alice";
const greeting = `Hello, ${name}!`;  // "Hello, Alice!"
```

Template literals support:

1. **Expression interpolation** — embedding variables and expressions
2. **Multi-line strings** — strings that span multiple lines

We'll explore these features next.

## Template literals

Template literals provide a modern syntax for string creation and interpolation in JavaScript (but for simple, static strings, single or double quotes are still commonly used).

### Expression interpolation

Embed variables and expressions using `${}`:

```javascript
const name = "Alice";
const age = 30;

// Old way (concatenation)
const message1 = "Hello, " + name + "! You are " + age + " years old.";

// Modern way (template literal)
const message2 = `Hello, ${name}! You are ${age} years old.`;
// "Hello, Alice! You are 30 years old."
```

You can use any JavaScript expression inside `${}`:

```javascript
const x = 5;
const y = 10;
const sum = `The sum of ${x} and ${y} is ${x + y}`;
// "The sum of 5 and 10 is 15"

const isActive = true;
const status = `User is ${isActive ? "active" : "inactive"}`;
// "User is active"
```

### Multi-line strings

Template literals preserve line breaks:

```javascript
// Old way (concatenation)
const oldWay = "Line 1\n" +
               "Line 2\n" +
               "Line 3";

// Modern way (template literal)
const newWay = `Line 1
Line 2
Line 3`;
```

This makes template literals perfect for:
- Long messages
- HTML templates
- SQL queries
- Configuration strings

## Common string methods

Strings have many built-in methods. Here are the most common ones:

### Getting length

```javascript
const text = "Hello";
text.length;  // 5
```

### Accessing characters

```javascript
const text = "Hello";
text[0];        // "H" (first character)
text[1];        // "e"
text[text.length - 1]; // "o" (last character)

// Using charAt() method
text.charAt(0); // "H"
```

### Converting case

```javascript
const text = "Hello World";

text.toUpperCase();  // "HELLO WORLD"
text.toLowerCase();  // "hello world"
```

### Finding substrings

```javascript
const text = "Hello, World!";

text.indexOf("World");    // 7 (position where "World" starts)
text.indexOf("xyz");      // -1 (not found)
text.includes("World");   // true
text.includes("xyz");     // false
text.startsWith("Hello"); // true
text.endsWith("!");       // true
```

### Extracting substrings

```javascript
const text = "Hello, World!";

text.slice(0, 5);     // "Hello" (start at 0, end before 5)
text.slice(7);        // "World!" (from position 7 to end)
text.slice(-6);       // "World!" (6 characters from end)
text.substring(0, 5); // "Hello" (similar to slice, but behaves differently with negative numbers)
```

### Replacing text

```javascript
const text = "Hello, World!";

text.replace("World", "JavaScript");  // "Hello, JavaScript!"
text.replace("l", "L");               // "HeLlo, World!" (only first occurrence)
text.replaceAll("l", "L");            // "HeLLo, WorLd!" (all occurrences)
```

### Splitting strings

```javascript
const text = "apple,banana,cherry";
text.split(",");  // ["apple", "banana", "cherry"]

const words = "Hello World";
words.split(" ");  // ["Hello", "World"]
words.split("");   // ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"]
```

### Trimming whitespace

```javascript
const text = "  Hello, World!  ";

text.trim();        // "Hello, World!" (removes leading and trailing whitespace)
text.trimStart();   // "Hello, World!  " (removes leading whitespace)
text.trimEnd();     // "  Hello, World!" (removes trailing whitespace)
```

### Combining strings

```javascript
const part1 = "Hello";
const part2 = "World";

part1 + " " + part2;           // "Hello World" (concatenation)
part1.concat(" ", part2);      // "Hello World" (using concat method)
`${part1} ${part2}`;           // "Hello World" (template literal - preferred)
```

## String immutability

Strings are **immutable**, meaning you cannot change them after creation. When you call a method on a string, it returns a **new string** rather than modifying the original:

```javascript
const text = "Hello";
text.toUpperCase();  // Returns "HELLO", but doesn't change text
console.log(text);   // Still "Hello"

// To save the result, assign it to a variable
const upperText = text.toUpperCase();
console.log(upperText); // "HELLO"
```

This is important to remember. Methods like `replace()`, `toUpperCase()`, and `slice()` return new strings; they don't modify the original.

## Common string patterns

### Checking if string is empty

```javascript
const text = "";

// Falsy check (works because empty string is falsy)
if (!text) {
  console.log("String is empty");
}

// Explicit length check
if (text.length === 0) {
  console.log("String is empty");
}
```

### Building strings with loops

```javascript
const names = ["Alice", "Bob", "Charlie"];
let result = "";

for (const name of names) {
  result += name + ", ";
}

console.log(result); // "Alice, Bob, Charlie, "
```

Or more elegantly with array methods (covered in the [arrays guide](./arrays)):

```javascript
const names = ["Alice", "Bob", "Charlie"];
const result = names.join(", ");
console.log(result); // "Alice, Bob, Charlie"
```

### Escaping characters

Sometimes you need to include special characters in strings:

```javascript
const quote = 'He said "Hello"';           // Using different quotes
const quote2 = "He said \"Hello\"";        // Escaping with backslash
const path = "C:\\Users\\Alice\\file.txt"; // Escaping backslashes
const newline = "Line 1\nLine 2";          // Newline character
const tab = "Column1\tColumn2";            // Tab character
```

In template literals, you still need to escape some characters:

```javascript
const text = `He said "Hello"`;        // Quotes work fine
const text2 = `Use \`backticks\` here`; // Need to escape backticks
```

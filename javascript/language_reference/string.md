---
title: String
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
<!-- ## Properties

```javascript
Object.getOwnPropertyNames(String.prototype)
// ['length', 'constructor', 'anchor', 'big', 'blink', 'bold', 'charAt', 'charCodeAt', 'codePointAt', 'concat', 'endsWith', 'fontcolor', 'fontsize', 'includes', 'indexOf', 'italics', 'lastIndexOf', 'link', 'localeCompare', 'match', 'matchAll', 'normalize', 'padEnd', 'padStart', 'repeat', 'replace', 'replaceAll', 'search', 'slice', 'small', 'split', 'startsWith', 'strike', 'sub', 'substr', 'substring', 'sup', 'toLocaleLowerCase', 'toLocaleUpperCase', 'toLowerCase', 'toString', 'toUpperCase', 'trim', 'trimEnd', 'trimLeft', 'trimRight', 'trimStart', 'valueOf', 'at']
``` -->

## Definition

A `String` is a sequence of characters used to represent text. Strings in JavaScript are immutable, meaning, once created, they cannot be changed. Only new strings can be created.

```javascript
typeof "hello"   // "string"
typeof 'world'   // "string"
typeof `template` // "string"
```

## Using strings

If a string does not have quotation marks it will be interpreted as a variable.

```javascript
"this is a string"
'this is also a string'
this is not a string  // ReferenceError if not defined
```

A multiline string can be created with template literals (backticks) or by escaping newlines.

```javascript
// Template literals (ES6+)
`multi
line
string`

// Escaped newlines
"multi\nline\nstring"
```

### Escape characters

The backslash `\` can "escape" a quotation mark. When escaped, JavaScript will interpret the quotation mark as a character instead of the termination of the string.

```javascript
"The cow says \"moo\""
// "The cow says "moo""

'It\'s a string'
// "It's a string"
```

A new line can be created within a string with `\n`.

```javascript
console.log("This string will print\non 2 lines")
// This string will print
// on 2 lines
```

Other common escape sequences:

```javascript
"Tab\tseparated"       // Tab    separated
"Backslash\\"          // Backslash\
"Carriage return\r"    // Carriage return
"Single quote\'"       // Single quote'
"Double quote\""       // Double quote"
```

### Template literals

Template literals (backticks) allow values to be interpolated into a string. They can be used with expressions inside curly braces.

```javascript
const year = 1995
console.log(`JavaScript was first released in ${year}`)
// "JavaScript was first released in 1995"
```

Expressions can be executed inside of a template literal:

```javascript
console.log(`For computers, time began in the year ${2000 - 30}`)
// "For computers, time began in the year 1970"
```

### Basic operations on strings

Two or more strings can be added with a `+` operator or a string can be multiplied by a `number` with the `repeat()` method.

```javascript
"hello" + "world"
// "helloworld"

"hello".repeat(3)
// "hellohellohello"
```

### Accessing characters

String characters are accessed by their index. Indices start at `0`. A negative index can be used with the `at()` method (ES2022).

```javascript
const str = "hello"

str[0]        // "h"
str[1]        // "e"
str[4]        // "o"
str[10]       // undefined (out of bounds)

// Using at() method (ES2022)
str.at(-1)    // "o" (last character)
str.at(-2)    // "l" (second from end)
```

### Slicing strings

A substring can be extracted from a string by slicing using the syntax:

```javascript
string.slice(start, end)
```

The `start` is the index of the first character of the slice. The slice continues up to but not including the index `end`. If no index is specified the respective beginning or end of the string is considered.

```javascript
"chicken-nuggets".slice(0, 7)
// "chicken"

"chicken-nuggets".slice(3, 9)
// "cken-n"

"chicken-nuggets".slice(8)
// "nuggets"

"chicken-nuggets".slice(-7)
// "nuggets" (from end)
```

### `includes()` and membership testing

Existence of a substring within a string can be checked with `includes()`.

```javascript
"chicken nuggets".includes("gg")
// true

"chicken nuggets".includes("potatoes")
// false

"chicken nuggets".includes("chicken")
// true
```

## Operations on strings

JavaScript provides various operations that can be performed on strings through operators and built-in methods.

| Operation | Syntax | Example | Result |
| --- | --- | --- | --- |
| Concatenation | `+` | `"cat" + "fish"` | `"catfish"` |
| Index access | `[index]` | `"cat"[1]` | `"a"` |
| Length | `.length` | `"hello".length` | `5` |
| Equality | `===` | `"dog" === "dog"` | `true` |
| Inequality | `!==` | `"dog" !== "cat"` | `true` |
| Less than | `<` | `"ant" < "bat"` | `true` |
| Less than or equal | `<=` | `"ant" <= "ant"` | `true` |
| Greater than | `>` | `"bat" > "ant"` | `true` |
| Greater than or equal | `>=` | `"bat" >= "bat"` | `true` |

---

## String methods

### `at`

Returns the character at a specified index. Accepts negative indices to count from the end.

```javascript
"hello".at(0)
// "h"

"hello".at(-1)
// "o"

"hello".at(10)
// undefined
```

---

### `charAt`

Returns the character at a specified index.

```javascript
"hello".charAt(0)
// "h"

"hello".charAt(10)
// "" (empty string, not undefined)
```

---

### `charCodeAt`

Returns the Unicode value of the character at a specified index.

```javascript
"hello".charCodeAt(0)
// 104 (Unicode for 'h')
```

---

### `codePointAt`

Returns the Unicode code point value at a specified index.

```javascript
"😊".codePointAt(0)
// 128522
```

---

### `concat`

Combines two or more strings.

```javascript
"Hello".concat(" ", "world")
// "Hello world"

"Hello" + " " + "world"
// Same result (preferred)
```

---

### `endsWith`

Returns `true` if a string terminates with a specified substring. Otherwise returns `false`.

```javascript
"friend".endsWith("end")
// true

"friend".endsWith("fri")
// false
```

---

### `includes`

Determines whether a string contains a substring.

```javascript
"hello".includes("ell")
// true

"hello".includes("xyz")
// false
```

---

### `indexOf`

Returns the index of the first occurrence of a substring within a string. Returns `-1` if not found.

```javascript
"Hello world".indexOf("wo")
// 6

"hello world".indexOf("o")
// 4

"hello world".indexOf("x")
// -1
```

---

### `lastIndexOf`

Returns the index of the last occurrence of a substring within a string. Returns `-1` if not found.

```javascript
"to be or not to be".lastIndexOf("be")
// 16

"to be or not to be".lastIndexOf("to")
// 13

"to be or not to be".lastIndexOf("42")
// -1
```

---

### `localeCompare`

Compares two strings in the current locale.

```javascript
"a".localeCompare("b")
// -1 (a comes before b)

"b".localeCompare("a")
// 1 (b comes after a)

"a".localeCompare("a")
// 0 (equal)
```

---

### `match`

Matches a string against a regular expression.

```javascript
"hello".match(/l/g)
// ["l", "l"]

"hello".match(/x/)
// null
```

---

### `matchAll`

Returns an iterator of all matches of a regular expression.

```javascript
Array.from("hello hello".matchAll(/hello/g))
// [["hello"], ["hello"]]
```

---

### `normalize`

Returns the Unicode Normalization Form of a string.

```javascript
"\u0041\u030A".normalize()
// "Å"
```

---

### `padEnd`

Pads the end of a string to a specified length.

```javascript
"42".padEnd(5, "0")
// "42000"

"42".padEnd(5)
// "42   " (spaces by default)
```

---

### `padStart`

Pads the start of a string to a specified length.

```javascript
"42".padStart(5, "0")
// "00042"

"42".padStart(5)
// "   42" (spaces by default)
```

---

### `repeat`

Returns a new string with a specified number of copies.

```javascript
"hello".repeat(3)
// "hellohellohello"
```

---

### `replace`

Replaces the first occurrence of a substring or pattern.

```javascript
"hello world".replace("world", "JavaScript")
// "hello JavaScript"

"hello hello".replace("hello", "hi")
// "hi hello" (only first)
```

---

### `replaceAll`

Replaces all occurrences of a substring or pattern.

```javascript
"hello hello".replaceAll("hello", "hi")
// "hi hi"
```

---

### `search`

Searches for a match between a regular expression and a string.

```javascript
"hello".search(/l/)
// 2

"hello".search(/x/)
// -1
```

---

### `slice`

Extracts a section of a string and returns it as a new string.

```javascript
"hello".slice(1, 4)
// "ell"

"hello".slice(1)
// "ello"

"hello".slice(-3)
// "llo" (from end)
```

---

### `split`

Splits a string into an array of substrings.

```javascript
"hello world".split(" ")
// ["hello", "world"]

"a,b,c".split(",")
// ["a", "b", "c"]

"hello".split("")
// ["h", "e", "l", "l", "o"]
```

---

### `startsWith`

Returns `true` if the string begins with the indicated substring, otherwise returns `false`.

```javascript
"to be or not to be".startsWith("t")
// true

"to be or not to be".startsWith("to")
// true

"to be or not to be".startsWith("be")
// false
```

---

### `substring`

Similar to `slice()`, but doesn't accept negative indices.

```javascript
"hello".substring(1, 4)
// "ell"

"hello".substring(1)
// "ello"
```

---

### `substr` (deprecated)

Extracts a substring starting at a specified position. **Deprecated**: Use `slice()` instead.

---

### `toLowerCase`

Returns a string converted to lowercase.

```javascript
"HeLlO wOrLd!".toLowerCase()
// "hello world!"
```

---

### `toLocaleLowerCase`

Returns a string converted to lowercase according to locale-specific case mappings.

```javascript
"İ".toLocaleLowerCase("tr")
// "i"
```

---

### `toUpperCase`

Returns a string converted to uppercase.

```javascript
"lowercase".toUpperCase()
// "LOWERCASE"
```

---

### `toLocaleUpperCase`

Returns a string converted to uppercase according to locale-specific case mappings.

```javascript
"i".toLocaleUpperCase("tr")
// "İ"
```

---

### `trim`

Returns the given string with leading and trailing whitespace removed.

```javascript
"         hello        there              ".trim()
// "hello        there"
```

---

### `trimEnd` / `trimRight`

Returns the given string with trailing whitespace removed.

```javascript
"heehaw           ".trimEnd()
// "heehaw"
```

---

### `trimStart` / `trimLeft`

Returns the given string with leading whitespace removed.

```javascript
"     Hello there!".trimStart()
// "Hello there!"
```

---

### `valueOf`

Returns the primitive value of a string object.

```javascript
const str = new String("hello")
str.valueOf()
// "hello"
```

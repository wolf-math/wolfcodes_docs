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

## Definition

A `String` is a sequence of text characters. Strings are usually created with single quotes, double quotes, or backticks.

Strings in JavaScript are **immutable**. A string method never changes the original string; methods such as `trim()`, `replace()`, and `toUpperCase()` return new strings instead.

```javascript
> typeof "hello"
"string"

> typeof 'world'
"string"

> typeof `template`
"string"
```

:::note
JavaScript has string primitives, such as `"hello"`, and `String` objects, such as `new String("hello")`. Use string primitives in normal code. `String` objects are rarely needed and can make equality checks surprising.
:::

```javascript
> "hello" === "hello"
true

> new String("hello") === "hello"
false

> new String("hello").valueOf() === "hello"
true
```

## Using strings

### Creating strings

Strings can be created with single quotes, double quotes, or template literals.

```javascript
const single = 'hello'
const double = "hello"
const template = `hello`
```

If text is not wrapped in quotes, JavaScript treats it as a variable name.

```javascript
const greeting = "hello"

greeting  // "hello"

// This would cause an error if hello is not defined:
// hello  // ReferenceError: hello is not defined
```

Use either single quotes or double quotes consistently within a file. Use template literals when you need interpolation or a multiline string.

### Template literals

Template literals use backticks. They can include variables and expressions inside `${}`.

```javascript
const language = "JavaScript"
const year = 1995

console.log(`${language} was first released in ${year}`)
// JavaScript was first released in 1995
```

Expressions can run inside the placeholder.

```javascript
const price = 25
const quantity = 4

console.log(`Total: $${price * quantity}`)
// Total: $100
```

Template literals can also span multiple lines.

```javascript
const message = `First line
Second line`

console.log(message)
// First line
// Second line
```

### Escape characters

Use a backslash `\` to escape characters that would otherwise end the string or have special meaning.

```javascript
const quote = "The cow says \"moo\""
console.log(quote)
// The cow says "moo"

const contraction = 'It\'s a string'
console.log(contraction)
// It's a string
```

Common escape sequences:

| Escape sequence | Meaning |
| --------------- | ------- |
| `\\` | Backslash |
| `\"` | Double quote |
| `\'` | Single quote |
| `\n` | Newline |
| `\r` | Carriage return |
| `\t` | Tab |
| `\uXXXX` | Unicode escape |

```javascript
console.log("This string prints\non two lines")
// This string prints
// on two lines

console.log("Column 1\tColumn 2")
// Column 1    Column 2
```

### Accessing characters

String characters can be accessed by index. Indexes start at `0`.

```javascript
const word = "hello"

console.log(word[0])  // "h"
console.log(word[1])  // "e"
console.log(word[4])  // "o"
console.log(word[10]) // undefined
```

Use `at()` when you want negative indexes.

```javascript
const word = "hello"

console.log(word.at(0))  // "h"
console.log(word.at(-1)) // "o"
console.log(word.at(-2)) // "l"
```

:::note
String indexes are based on UTF-16 code units, not always full user-visible characters. Emoji and some symbols may take more than one index.
:::

```javascript
const smile = "😊"

console.log(smile.length) // 2
console.log(smile[0])     // "\ud83d"
```

### String length

The `length` property returns the number of UTF-16 code units in the string.

```javascript
console.log("hello".length) // 5
console.log("".length)      // 0
console.log("😊".length)    // 2
```

`length` is a property, not a method.

```javascript
"hello".length   // correct
// "hello".length()  // TypeError: "hello".length is not a function
```

### Combining strings

Use `+` to concatenate strings. Use template literals when variables are involved.

```javascript
const firstName = "Ada"
const lastName = "Lovelace"

console.log(firstName + " " + lastName)
// Ada Lovelace

console.log(`${firstName} ${lastName}`)
// Ada Lovelace
```

If one side of `+` is a string, JavaScript usually converts the other side to a string.

```javascript
console.log("Score: " + 10)
// Score: 10
```

Use template literals when this conversion should be obvious to the reader.

### Slicing strings

Use `slice()` to extract part of a string. It returns a new string and does not change the original.

```javascript
const food = "chicken-nuggets"

console.log(food.slice(0, 7)) // "chicken"
console.log(food.slice(8))    // "nuggets"
console.log(food.slice(-7))   // "nuggets"
console.log(food)             // "chicken-nuggets"
```

The start index is included. The end index is excluded.

```javascript
console.log("hello".slice(1, 4)) // "ell"
```

### Membership testing

Use `includes()` to check whether a string contains a substring.

```javascript
const sentence = "chicken nuggets"

console.log(sentence.includes("nug"))      // true
console.log(sentence.includes("potatoes")) // false
```

Use `startsWith()` and `endsWith()` when the position matters.

```javascript
const filename = "report.pdf"

console.log(filename.startsWith("report")) // true
console.log(filename.endsWith(".pdf"))     // true
```

## Operations on strings

| Operation | Syntax | Example | Result |
| --------- | ------ | ------- | ------ |
| Concatenation | `+` | `"cat" + "fish"` | `"catfish"` |
| Template interpolation | `` `${name}` `` | `` `Hi, ${"Ada"}` `` | `"Hi, Ada"` |
| Index access | `[index]` | `"cat"[1]` | `"a"` |
| Negative index access | `at(index)` | `"cat".at(-1)` | `"t"` |
| Length | `.length` | `"hello".length` | `5` |
| Equality | `===` | `"dog" === "dog"` | `true` |
| Inequality | `!==` | `"dog" !== "cat"` | `true` |
| Lexicographic comparison | `<` | `"ant" < "bat"` | `true` |
| Membership | `includes()` | `"hello".includes("ell")` | `true` |

String comparisons are based on Unicode code unit order. For human-language sorting, prefer `localeCompare()` or `Intl.Collator`.

```javascript
console.log("Z" < "a") // true
```

## String methods

String methods return new values. They do not mutate the original string.

:::note
Some JavaScript runtimes also expose old HTML wrapper methods on `String.prototype`, such as `bold()`, `link()`, and `fontcolor()`. They are obsolete and should not be used in modern code.
:::

### `at()`

Returns the character at a specified index. Accepts negative indexes to count backward from the end of the string. Returns `undefined` when the index is out of range.

```javascript
const word = "hello"

console.log(word.at(0))  // "h"
console.log(word.at(-1)) // "o"
console.log(word.at(10)) // undefined
```

Use `at()` when negative indexing makes the code clearer.

---

### `charAt()`

Returns the character at a specified index. Unlike bracket access and `at()`, `charAt()` returns an empty string when the index is out of range.

```javascript
const word = "hello"

console.log(word.charAt(0))  // "h"
console.log(word.charAt(10)) // ""
```

---

### `charCodeAt()`

Returns the UTF-16 code unit at a specified index. Returns `NaN` when the index is out of range.

```javascript
console.log("hello".charCodeAt(0)) // 104
console.log("hello".charCodeAt(9)) // NaN
```

Use `codePointAt()` when you need to work with full Unicode code points.

---

### `codePointAt()`

Returns the Unicode code point at a specified index. Returns `undefined` when the index is out of range.

```javascript
console.log("A".codePointAt(0))  // 65
console.log("😊".codePointAt(0)) // 128522
console.log("A".codePointAt(5))  // undefined
```

This is usually better than `charCodeAt()` for characters outside the basic multilingual plane, such as many emoji.

---

### `concat()`

Combines the string with one or more values and returns a new string.

```javascript
console.log("Hello".concat(" ", "world"))
// Hello world
```

The `+` operator or template literals are usually easier to read.

```javascript
const name = "Ada"

console.log("Hello, " + name)
console.log(`Hello, ${name}`)
```

---

### `endsWith()`

Returns `true` if the string ends with the specified substring. Otherwise, returns `false`.

```javascript
const filename = "photo.jpg"

console.log(filename.endsWith(".jpg")) // true
console.log(filename.endsWith(".png")) // false
```

An optional second argument limits the string length checked.

```javascript
console.log("JavaScript".endsWith("Java", 4)) // true
```

---

### `includes()`

Returns `true` if the string contains the specified substring. Otherwise, returns `false`.

```javascript
const message = "hello world"

console.log(message.includes("world")) // true
console.log(message.includes("WORLD")) // false
```

`includes()` is case-sensitive. Use `toLowerCase()` or `toLocaleLowerCase()` first when you need a case-insensitive check.

```javascript
const answer = "Yes"

console.log(answer.toLowerCase().includes("yes")) // true
```

---

### `indexOf()`

Returns the index of the first occurrence of a substring. Returns `-1` if the substring is not found.

```javascript
const message = "hello world"

console.log(message.indexOf("o")) // 4
console.log(message.indexOf("x")) // -1
```

An optional second argument sets the index where the search begins.

```javascript
console.log("hello world".indexOf("o", 5)) // 7
```

Use `includes()` when you only need a yes-or-no membership check.

---

### `lastIndexOf()`

Returns the index of the last occurrence of a substring. Returns `-1` if the substring is not found.

```javascript
const phrase = "to be or not to be"

console.log(phrase.lastIndexOf("be")) // 16
console.log(phrase.lastIndexOf("to")) // 13
console.log(phrase.lastIndexOf("x"))  // -1
```

---

### `localeCompare()`

Compares two strings according to locale-aware sorting rules. Returns a negative number, `0`, or a positive number.

```javascript
console.log("a".localeCompare("b")) // negative number
console.log("b".localeCompare("a")) // positive number
console.log("a".localeCompare("a")) // 0
```

Do not depend on the exact negative or positive value. Only the sign matters.

```javascript
const names = ["Zoe", "Ana", "Émile"]

names.sort((a, b) => a.localeCompare(b))
console.log(names)
// ["Ana", "Émile", "Zoe"]
```

For repeated sorting, `Intl.Collator` can be clearer and more configurable.

---

### `match()`

Matches the string against a regular expression. Returns an array of matches or `null` when there is no match.

```javascript
console.log("hello".match(/l/g))
// ["l", "l"]

console.log("hello".match(/x/))
// null
```

Use `match()` when you want the matched values. Use `search()` when you only need the index of the first match.

See also [`RegExp`](./regexp).

---

### `matchAll()`

Returns an iterator of all regular expression matches. The regular expression must use the `g` flag.

```javascript
const text = "item-1 item-2"
const matches = text.matchAll(/item-(\d)/g)

for (const match of matches) {
  console.log(match[1])
}
// 1
// 2
```

Convert the iterator to an array when you need to inspect all matches at once.

```javascript
const results = Array.from("hello hello".matchAll(/hello/g))

console.log(results.length) // 2
```

---

### `normalize()`

Returns a Unicode-normalized version of the string.

```javascript
const composed = "\u00F1"
const decomposed = "\u006E\u0303"

console.log(composed === decomposed)              // false
console.log(composed === decomposed.normalize())  // true
```

Use `normalize()` when visually identical text may be represented with different Unicode sequences.

---

### `padEnd()`

Pads the end of a string until it reaches a target length. Returns a new string.

```javascript
console.log("42".padEnd(5, "0")) // "42000"
console.log("42".padEnd(5))      // "42   "
```

If the string is already at least the target length, the original string value is returned unchanged.

```javascript
console.log("hello".padEnd(3, ".")) // "hello"
```

---

### `padStart()`

Pads the start of a string until it reaches a target length. Returns a new string.

```javascript
console.log("42".padStart(5, "0")) // "00042"
console.log("42".padStart(5))      // "   42"
```

This is commonly used for fixed-width IDs, times, or numbers displayed as text.

```javascript
const minutes = 7

console.log(String(minutes).padStart(2, "0")) // "07"
```

---

### `repeat()`

Returns a new string containing the original string repeated a specified number of times.

```javascript
console.log("ha".repeat(3)) // "hahaha"
```

The count must be non-negative and finite.

```javascript
// "ha".repeat(-1)       // RangeError
// "ha".repeat(Infinity) // RangeError
```

---

### `replace()`

Replaces the first matching substring or regular expression match and returns a new string.

```javascript
console.log("hello world".replace("world", "JavaScript"))
// hello JavaScript

console.log("hello hello".replace("hello", "hi"))
// hi hello
```

With a regular expression that uses the `g` flag, `replace()` replaces all matches.

```javascript
console.log("hello hello".replace(/hello/g, "hi"))
// hi hi
```

The replacement can also be a callback.

```javascript
const result = "item 1 item 2".replace(/\d/g, number => Number(number) * 10)

console.log(result)
// item 10 item 20
```

---

### `replaceAll()`

Replaces all occurrences of a substring or regular expression match and returns a new string.

```javascript
console.log("hello hello".replaceAll("hello", "hi"))
// hi hi
```

When using a regular expression with `replaceAll()`, the regular expression must have the `g` flag.

```javascript
console.log("a-b-c".replaceAll(/-/g, " "))
// a b c

// "a-b-c".replaceAll(/-/, " ")  // TypeError
```

Use `replaceAll()` when you want all literal occurrences replaced and do not need regular expression behavior.

---

### `search()`

Searches for a regular expression match and returns the index of the first match. Returns `-1` if there is no match.

```javascript
console.log("hello".search(/l/)) // 2
console.log("hello".search(/x/)) // -1
```

Use `indexOf()` for plain substring searches and `search()` for regular expressions.

---

### `slice()`

Extracts part of a string and returns it as a new string. The start index is included, and the end index is excluded.

```javascript
const word = "hello"

console.log(word.slice(1, 4)) // "ell"
console.log(word.slice(1))    // "ello"
console.log(word.slice(-3))   // "llo"
console.log(word)             // "hello"
```

Use `slice()` as the default method for extracting part of a string.

---

### `split()`

Splits a string into an array of substrings.

```javascript
console.log("hello world".split(" "))
// ["hello", "world"]

console.log("a,b,c".split(","))
// ["a", "b", "c"]
```

Use an empty string to split into UTF-16 code units.

```javascript
console.log("hello".split(""))
// ["h", "e", "l", "l", "o"]
```

An optional second argument limits the number of pieces.

```javascript
console.log("a,b,c".split(",", 2))
// ["a", "b"]
```

For structured formats with quoting or escaping rules, such as CSV, use a parser instead of relying only on `split()`.

:::note
`split("")` can break emoji and other characters represented by multiple UTF-16 code units. Use `Array.from(text)` when you need a better approximation of user-visible characters.
:::

```javascript
console.log("😊".split(""))   // ["\ud83d", "\ude0a"]
console.log(Array.from("😊")) // ["😊"]
```

---

### `startsWith()`

Returns `true` if the string starts with the specified substring. Otherwise, returns `false`.

```javascript
const phrase = "to be or not to be"

console.log(phrase.startsWith("to")) // true
console.log(phrase.startsWith("be")) // false
```

An optional second argument sets the position where the check begins.

```javascript
console.log("JavaScript".startsWith("Script", 4)) // true
```

---

### `substring()`

Extracts part of a string and returns it as a new string. Unlike `slice()`, `substring()` treats negative indexes as `0` and swaps the start and end indexes if start is greater than end.

```javascript
console.log("hello".substring(1, 4)) // "ell"
console.log("hello".substring(4, 1)) // "ell"
console.log("hello".substring(-3))   // "hello"
```

Prefer `slice()` in most new code because its negative-index behavior is more useful and predictable.

---

### `substr()` (deprecated)

Extracts part of a string starting at an index for a specified length.

```javascript
console.log("hello".substr(1, 3)) // "ell"
```

:::note
`substr()` is deprecated. Use `slice()` instead.
:::

---

### `toLowerCase()`

Returns a new string converted to lowercase.

```javascript
console.log("HeLlO wOrLd!".toLowerCase())
// hello world!
```

This method is not locale-specific. Use `toLocaleLowerCase()` when locale-specific casing matters.

---

### `toLocaleLowerCase()`

Returns a new string converted to lowercase according to locale-specific case mappings.

```javascript
console.log("İ".toLocaleLowerCase("tr"))
// i
```

Use this when casing depends on a language or locale.

---

### `toUpperCase()`

Returns a new string converted to uppercase.

```javascript
console.log("lowercase".toUpperCase())
// LOWERCASE
```

This method is not locale-specific. Use `toLocaleUpperCase()` when locale-specific casing matters.

---

### `toLocaleUpperCase()`

Returns a new string converted to uppercase according to locale-specific case mappings.

```javascript
console.log("i".toLocaleUpperCase("tr"))
// İ
```

---

### `trim()`

Returns a new string with whitespace removed from both ends.

```javascript
const padded = "   hello there   "

console.log(padded.trim()) // "hello there"
console.log(padded)        // "   hello there   "
```

`trim()` does not remove whitespace inside the string.

---

### `trimEnd()` / `trimRight()`

Returns a new string with trailing whitespace removed.

```javascript
console.log("hello   ".trimEnd())
// hello
```

`trimRight()` is an alias of `trimEnd()`. Prefer `trimEnd()` in new code.

---

### `trimStart()` / `trimLeft()`

Returns a new string with leading whitespace removed.

```javascript
console.log("   hello".trimStart())
// hello
```

`trimLeft()` is an alias of `trimStart()`. Prefer `trimStart()` in new code.

---

### `toString()`

Returns the string representation of a `String` object.

```javascript
const text = new String("hello")

console.log(text.toString()) // "hello"
```

For normal string primitives, `toString()` returns the same string value.

```javascript
console.log("hello".toString()) // "hello"
```

---

### `valueOf()`

Returns the primitive string value of a `String` object.

```javascript
const text = new String("hello")

console.log(text.valueOf()) // "hello"
console.log(typeof text)    // "object"
console.log(typeof text.valueOf()) // "string"
```

Use string primitives directly instead of creating `String` objects.

## String static methods

### `String.fromCharCode()`

Creates a string from one or more UTF-16 code units.

```javascript
console.log(String.fromCharCode(65, 66, 67))
// ABC
```

For code points outside the basic multilingual plane, use `String.fromCodePoint()`.

---

### `String.fromCodePoint()`

Creates a string from one or more Unicode code points.

```javascript
console.log(String.fromCodePoint(128522))
// 😊
```

This handles code points that cannot be represented by a single UTF-16 code unit.

---

### `String.raw()`

Returns a raw string from a template literal, without interpreting escape sequences in the usual way.

```javascript
console.log(String.raw`Line 1\nLine 2`)
// Line 1\nLine 2
```

This is useful when writing strings for paths, regular expressions, or other text where backslashes should stay visible.

## Behavioral notes

### Strings are immutable

String methods return new strings. They do not modify the original string.

```javascript
const text = " hello "

text.trim()
console.log(text) // " hello "

const cleaned = text.trim()
console.log(cleaned) // "hello"
```

### Indexes use UTF-16 code units

String indexes and `length` count UTF-16 code units. Some user-visible characters use more than one code unit.

```javascript
console.log("😊".length) // 2
console.log("😊"[0])     // "\ud83d"
```

Use `Array.from()` when you need to iterate over Unicode code points more safely.

```javascript
console.log(Array.from("😊").length) // 1
```

### String comparison uses code unit order

Operators such as `<` and `>` compare strings by code unit order.

```javascript
console.log("Z" < "a") // true
```

Use `localeCompare()` or `Intl.Collator` for user-facing sorting.

### String objects are not string primitives

`new String()` creates an object wrapper, not a string primitive.

```javascript
const primitive = "hello"
const objectString = new String("hello")

console.log(typeof primitive)     // "string"
console.log(typeof objectString)  // "object"
console.log(primitive === objectString) // false
```

## Best practices

1. **Use string primitives**: Write `"hello"`, not `new String("hello")`.

2. **Use template literals for interpolation**: They are easier to read than long `+` chains.

3. **Remember that strings are immutable**: Store the returned value from methods like `trim()`, `replace()`, and `toLowerCase()`.

4. **Use `includes()` for membership checks**: It is clearer than checking whether `indexOf()` returns `-1`.

5. **Prefer `slice()` for extraction**: It handles negative indexes more predictably than `substring()`.

6. **Use locale-aware methods for user-facing text**: Use `localeCompare()`, `toLocaleLowerCase()`, or `toLocaleUpperCase()` when language rules matter.

7. **Be careful with Unicode**: `length`, indexes, and `split("")` do not always match what users see as individual characters.

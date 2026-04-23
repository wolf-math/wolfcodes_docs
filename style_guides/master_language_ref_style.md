---
title: Master Language Reference Style
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Master language reference style

Use this guide when writing or revising pages in `docs/javascript/language_reference` and `docs/python/language_reference`.

The Python language reference is the quality bar. It has the right overall ambition: detailed enough to be useful as a real reference, beginner-friendly enough to teach, and structured enough that a reader can skim from definition to methods without getting lost. Use this guide especially to bring the JavaScript language reference up to that level.

The language reference pages are not broad tutorials. They are practical lookup pages for core language features: built-in types, built-in functions, keywords, methods, operators, and language constructs. They should still feel beginner-friendly, but their main job is to help a reader quickly answer:

- What is this thing?
- How do I create or use it?
- What does it return?
- What operations, methods, or attributes are available?
- What behavior is surprising?
- When should I use it, avoid it, or choose something else?

When this guide conflicts with a language-specific guide, use this guide for reference pages and the language-specific guide for tutorial pages.

## Upgrade goal

The main goal is to make the JavaScript language reference feel as complete and reliable as the Python language reference.

For JavaScript pages, this usually means adding:

- A fuller `## Definition` that names the core behavior and the common surprise.
- More explicit method, static-method, and property coverage inside the default JavaScript page shape.
- More complete method entries, not just one-line examples.
- Clear notes about return values, mutation, coercion, errors, and edge cases.
- Tables for comparison, method behavior, or category summaries.
- Cross-links to related JavaScript reference pages.
- Best-practice guidance that explains what a beginner should actually write.

Do not make JavaScript pages merely longer. Make them more reference-like: more precise, more consistent, more explicit about behavior, and easier to scan.

## Frontmatter

Use the standard frontmatter on every reference page:

```md
---
title: Concept Name
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
```

For hub pages such as `index.mdx`, include `sidebar_label` when the section already uses it:

```md
---
title: Python Language Reference
sidebar_label: Language Reference
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
```

- `title` should be literal and sidebar-friendly: `Array`, `Promise`, `Dict`, `Built-in Functions`, `Keywords`.
- Match the capitalization style of the language. Use `Array`, `BigInt`, and `WeakMap` for JavaScript; use `list`, `dict`, `int`, and `None` for Python when the language feature is normally lowercase.
- Keep author, license, and source metadata consistent.
- Do not add extra metadata unless the surrounding section already requires it.

## Core voice

Write like a clear reference author who still remembers that the reader may be learning the concept for the first time.

The tone should be:

- Direct, practical, and precise
- Friendly without being chatty
- Focused on observable behavior
- Specific about return values, mutation, errors, and edge cases
- Short enough to scan, but complete enough to trust

Prefer:

```md
`pop()` removes and returns the last item in the list.
```

Avoid:

```md
This method facilitates the extraction of terminal sequence members.
```

## Page types

Most pages fall into one of these shapes.

### Type or object pages

Examples: JavaScript `array.md`, `object.md`, `number.md`; Python `list.md`, `dict.md`, `int.md`.

For JavaScript type pages, use this order:

1. `## Definition`
2. `## Using [concept]`
3. `## Operations on [concept]`
4. `## [Concept] methods`
5. `## [Concept] static methods` or `## [Concept] properties` when needed
6. `## Behavioral notes` only when the type has important edge cases, surprising behavior, or comparison rules
7. `## Limitations` only when there are constraints, deprecated APIs, or runtime caveats
8. `## Best practices` only when there are a few concise recommendations that help readers choose between valid-looking APIs

This is the default JavaScript page shape. Do not add extra top-level sections unless the page truly needs them.

For Python type pages, retain the Python-first pattern:

1. `## Properties`
2. `## Definition`
3. `## Using [concept]`
4. Common access, creation, conversion, or modification sections
5. `## Operations on [concept]`
6. `## Dunder methods` when relevant
7. Method, attribute, or protocol sections
8. `## Behavioral notes`, `## Limitations`, or `## Best practices` when useful

Python keeps `## Properties` because `dir(...)` is a natural and recognizable introspection tool in that reference style. JavaScript should not copy that pattern by default.

Avoid standalone `## Common use cases` sections in dry reference pages. If a practical example is useful, place it inside the relevant method, property, or operation entry. This keeps the page technical and lookup-oriented instead of making it read like a tutorial.

### Built-in function pages

Examples: `built-in.md` in both language reference folders.

Use this order:

1. `## Definition`
2. Optional overview of how the functions are grouped
3. One `###` section per function or global object
4. Short definition
5. Small example
6. Return value, error behavior, and common use when relevant

Keep these pages compact. A built-in page can be long, but each function entry should be easy to scan.

### Keyword pages

Examples: `keywords.md` in both languages.

Use this order:

1. Optional `## Properties` or hidden source list if useful during maintenance
2. `## Definition`
3. A category table
4. `## Keyword definitions`
5. One `###` section per keyword

Each keyword entry should include:

- What the keyword does
- The smallest useful example, unless the keyword is only meaningful as part of another keyword
- A short note for deprecated, reserved, or context-sensitive keywords

### Language construct pages

Examples: `function.md`, `class.md`, `async.md`, `generator.md`, `coroutine.md`, `method.md`, `type.md`.

Use this order:

1. `## Definition`
2. Creation or declaration syntax
3. Runtime behavior and mental model
4. Methods, attributes, or protocol hooks
5. Common patterns
6. Best practices or limitations

These pages can be more explanatory than method catalog pages because constructs often need a mental model.

### Hub pages

Examples: `index.mdx`.

Hub pages should:

- Start with the same frontmatter pattern.
- Import `Link` from `@docusaurus/Link`.
- Reuse `./hub.module.css` when the surrounding page uses it.
- Give a short welcome paragraph.
- Group links under `## Built-in functions`, `## Built-in types`, `## Keywords`, and `## Language constructs`.
- Keep link text literal and matching the page title.
- Avoid long explanations. Hub pages are navigation, not teaching pages.

## Standard section names

Use these names consistently unless the page has a strong reason to be more specific:

- `## Properties`
- `## Definition`
- `## Using [plural concept]`
- `## Operations on [plural concept]`
- `## [Concept] methods`
- `## [Concept] static methods`
- `## [Concept] properties`
- `## Dunder methods`
- `## Behavioral notes`
- `## Limitations`
- `## Best practices`

For JavaScript pages, the default top-level section names should be limited to the eight-section shape above. `## Properties` is a Python exception, not a JavaScript default.

Use sentence-style headings. Capitalize proper nouns and exact API names:

```md
## Using arrays
## Promise methods
## Date formatting
## JSON serialization
## `async`/`await`
### `Promise.all()`
### `toString()`
```

Prefer `###` for individual methods, attributes, functions, keywords, and operations.

Use backticks in headings for exact syntax, method names, attributes, functions, operators, keywords, and literal values:

```md
### `append`
### `map()`
### `None`
### `Symbol.iterator`
### `from_bytes`
### `&&`
```

For JavaScript method headings, include parentheses for callable methods, such as ``### `map()` ``. For Python method headings, the existing reference often omits parentheses, such as ``### `append` ``. Preserve that convention unless revising the page broadly.

## Definitions

Every reference page needs `## Definition` near the top.

A good definition:

- Defines the term in 1-3 sentences.
- Names the syntax or literal form when there is one.
- Says whether the thing is mutable or immutable when that matters.
- Says whether the thing is primitive, object-like, callable, iterable, asynchronous, or a collection when that matters.
- Mentions the most important surprise early.

Examples:

```md
An `Array` is an ordered collection of values defined with square brackets `[]`. Array indexes start at `0`, and arrays can be modified after they are created.
```

```md
A `dict` is a collection of key-value pairs defined with curly braces `{}`. Values are accessed by key instead of by numeric index.
```

When a concept has confusing neighbors, name them in the definition or directly after it:

- JavaScript `null` vs `undefined`
- JavaScript `Map` vs `Object`
- JavaScript `Set` vs `Array`
- Python `list` vs `tuple`
- Python `bytes` vs `bytearray`
- Python `is` vs `==`
- Python `None` vs falsy values

## Examples

Examples are the backbone of the reference.

Use examples that are:

- Small and focused
- Easy to run or mentally evaluate
- Written with simple data such as `name`, `age`, `items`, `scores`, `person`, `user`, `numbers`, and `fruits`
- Close to the text they demonstrate
- Followed by a short explanation when behavior is not obvious

Use language-specific fences:

````md
```javascript
const numbers = [1, 2, 3]
console.log(numbers.length) // 3
```

```python
numbers = [1, 2, 3]
print(len(numbers))  # 3
```

```text
First line
Second line
```
````

Use `text` for output, tracebacks, and generic console output when not using REPL prompts.

## REPL examples

The existing reference often uses REPL-style examples:

```python
>>> len([1, 2, 3])
3
```

```javascript
> Array.isArray([])
true
```

This is allowed and useful for reference pages, especially when showing return values.

Rules for REPL examples:

- Use `>>>` for Python.
- Use `>` for JavaScript console examples.
- Show the returned value on the next line.
- Include `undefined` after JavaScript declarations only when the example is intentionally showing console behavior.
- Do not mix REPL prompts with normal script code in the same code block unless there is a clear reason.
- If the example is meant to be copied into a file, avoid prompts.

Good REPL-style Python:

```python
>>> fruits = ['apple', 'banana']
>>> fruits.append('orange')
>>> fruits
['apple', 'banana', 'orange']
```

Good script-style Python:

```python
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)  # ['apple', 'banana', 'orange']
```

Good REPL-style JavaScript:

```javascript
> typeof []
"object"

> Array.isArray([])
true
```

Good script-style JavaScript:

```javascript
const fruits = ["apple", "banana"]
fruits.push("orange")
console.log(fruits) // ["apple", "banana", "orange"]
```

## Output and return values

Be explicit about what a method returns and whether it mutates the original value.

For every method entry, include the most relevant facts:

- Return value
- Whether the original object changes
- Error behavior
- Important default arguments
- Whether the operation is shallow or deep
- Whether order matters

Use direct wording:

```md
`sort()` modifies the original list and returns `None`.
```

```md
`slice()` returns a new array and does not modify the original array.
```

```md
`dict.get()` returns `None` by default when the key is missing. You can provide a different default as the second argument.
```

When an operation mutates the original value, show the value before and after:

```python
>>> numbers = [3, 1, 2]
>>> numbers.sort()
>>> numbers
[1, 2, 3]
```

When an operation returns a new value, show that the original value is unchanged:

```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map(number => number * 2)

console.log(doubled) // [2, 4, 6]
console.log(numbers) // [1, 2, 3]
```

## Method entries

Method sections should be consistent and scannable.

Use this pattern for most methods:

````md
### `method_name`

One-sentence definition. Mention whether it mutates the original value or returns a new value.

```language
small example
```

Optional note about parameters, errors, or common use.
````

For overloaded or parameter-heavy methods, add a compact parameter list:

```md
**Parameters:**

- `start`: The index where the search begins.
- `end`: The index where the search stops.
```

Only include parameter lists when they make the entry clearer. Do not add a parameter table to every simple method.

Use horizontal rules (`---`) between many method entries when the page is a long catalog. Skip them on short pages where headings are enough.

## Properties and introspection

Python reference pages often start with `## Properties` and a `dir(type)` block. JavaScript pages should usually document methods and properties directly inside the default page shape instead of using a dedicated `## Properties` section.

Guidelines:

- Keep `dir(...)` or `Object.getOwnPropertyNames(...)` output accurate.
- Do not rely on raw introspection output as the only documentation.
- Follow introspection with curated explanations of the important methods.
- If the output is very long, consider keeping it hidden in an HTML comment or omitting it.
- Do not let a massive property block bury the definition on a beginner-facing page unless matching the existing Python reference style.

## Python-specific reference rules

### Python naming and examples

Use:

- `python` code fences
- 4-space indentation
- `lower_snake_case` for variables and functions
- `True`, `False`, and `None`
- `list`, `dict`, `set`, `tuple`, `str`, `int`, and `float` when naming built-in types
- `print()` when script-style output is clearer than REPL output

Python examples may use single quotes or double quotes. Be consistent within a block and prefer the surrounding page's style.

### Python `Properties`

For built-in type pages, use:

````md
## Properties

```python
>>> dir(list)
['__add__', ...]
```
````

Then move to `## Definition`.

### Python dunder methods

Use `## Dunder methods` for protocol behavior that explains operators, built-ins, iteration, equality, hashing, indexing, or conversion.

Prefer a table with these columns:

```md
| Dunder Method | Operation | Example (normal syntax) | Example (dunder call) |
| ------------- | --------- | ----------------------- | --------------------- |
| `__len__` | Length | `len(items)` | `items.__len__()` |
```

Dunder tables should:

- Include only relevant dunder methods, not every method from `dir(...)`.
- Prefer normal syntax first because that is what readers should write.
- Use dunder calls to reveal the protocol, not to recommend calling dunder methods directly.
- Mention when normal syntax is preferred.

### Python mutability

Always call out mutability for collection and numeric pages:

- `list`, `dict`, `set`, `bytearray`: mutable
- `tuple`, `frozenset`, `str`, `bytes`, `int`, `float`, `complex`, `bool`: immutable
- `range`: immutable sequence-like object

When a method mutates, say so plainly:

```md
`append` modifies the original list and returns `None`.
```

When assignment creates another reference, not a copy, use a note:

```md
:::note
`other = items` does not copy the list. It creates another name for the same list.
:::
```

### Python errors

Show common errors when they teach important behavior:

- `IndexError` for missing list indexes
- `KeyError` for missing dictionary keys
- `ValueError` for failed unpacking or conversion
- `TypeError` for unsupported operations
- `SyntaxError` for invalid assignment or syntax

Keep tracebacks short. Include the final error line when the full traceback does not add teaching value.

## JavaScript-specific reference rules

Use this section aggressively when editing `docs/javascript/language_reference`. The JavaScript reference should become as rich as the Python reference, not a shorter companion.

### JavaScript upgrade priorities

When improving an existing JavaScript page, prioritize these changes in order:

1. Fix correctness first: syntax, return values, mutation behavior, type checks, error behavior, and version notes.
2. Expand thin method entries so each one explains what it does, what it returns, and whether it mutates.
3. Add missing static methods, properties, and important prototype methods inside the existing default page shape.
4. Add comparison sections for concepts learners commonly confuse.
5. Add `Behavioral notes`, `Limitations`, and `Best practices` sections where the page needs technical judgment, not just syntax.
6. Improve examples so they show observable results and realistic beginner data.
7. Add cross-links to nearby reference pages.

Do not spend most of the effort polishing prose while behavior remains underdocumented. The most important upgrade is reliable technical substance.

### JavaScript naming and examples

Use:

- `javascript` code fences
- 2-space indentation
- `camelCase` for variables and functions
- `PascalCase` for classes and constructors
- `const` by default
- `let` only when reassignment is shown
- `true`, `false`, `null`, and `undefined`
- `console.log()` when script-style output is clearer than console prompts

Do not use `var` except when explaining old syntax or why to avoid it.

Prefer modern JavaScript, but name version-specific behavior when it matters:

- `at()` is ES2022.
- Private class fields are ES2022.
- `Promise.any()` is newer than the original Promise methods.

### JavaScript `Properties`

Do not add `## Properties` as a default top-level section on JavaScript type pages.

If introspection output is genuinely useful, fold it into the relevant method or property section, or mention it briefly inside `## Using [concept]` or `## [Concept] properties`.

This is different from Python on purpose. JavaScript introspection is less clean and less canonical for beginners than Python's `dir(...)`.

Good candidates for brief introspection examples:

- `Array`
- `String`
- `Number`
- `Object`
- `Map`
- `Set`
- `Promise`
- `Date`
- `RegExp`
- `Function`

Use JavaScript runtime introspection when useful:

```javascript
> Object.getOwnPropertyNames(Array.prototype)
['length', 'constructor', 'at', 'concat', 'copyWithin', 'entries', ...]
```

For constructors and static APIs, show constructor properties separately when helpful:

```javascript
> Object.getOwnPropertyNames(Number)
['length', 'name', 'prototype', 'isFinite', 'isInteger', 'isNaN', ...]
```

Guidelines:

- Do not use introspection output as a replacement for `## Definition`, `## Operations on [concept]`, or the method sections.
- Keep introspection output current enough to be useful, but do not let it replace explanations.
- If output is very long, either show the most relevant entries or follow it with a curated table.
- Explain that inherited, environment-specific, or newer APIs may vary by runtime when that matters.

### JavaScript method entry standard

Every JavaScript method entry should be at least as useful as a good Python method entry.

Use this pattern:

````md
### `methodName()`

Short definition. State whether it returns a new value, mutates the original value, or both.

```javascript
const result = example.methodName()
console.log(result)
```

Mention important parameters, default behavior, errors, coercion, or edge cases when relevant.
````

For common methods, include these details:

- **Arrays**: mutating vs non-mutating, callback arguments, return value, sparse array behavior when relevant.
- **Strings**: returned string, immutability, index behavior, Unicode caveats when relevant.
- **Objects**: own vs inherited properties, enumerable vs non-enumerable properties, shallow copy behavior.
- **Numbers**: `NaN`, `Infinity`, safe integer limits, rounding behavior.
- **Promises**: fulfillment, rejection, short-circuit behavior, result order.
- **Maps/Sets**: insertion order, key equality, object identity.
- **Dates**: local time vs UTC, mutation, parsing caveats.

For methods with callbacks, show the callback shape:

```javascript
array.map((value, index, array) => {
  return value
})
```

Then show the beginner-friendly short form:

```javascript
const doubled = numbers.map(number => number * 2)
```

### JavaScript mutation standard

JavaScript pages must clearly identify mutation because this is one of the main places beginners get hurt.

Use direct labels:

```md
`push()` mutates the original array and returns the new length.
```

```md
`map()` returns a new array and does not mutate the original array.
```

For array pages, include a mutating vs non-mutating table:

```md
| Mutating methods | Non-mutating methods |
| ---------------- | -------------------- |
| `push()`, `pop()`, `sort()` | `map()`, `filter()`, `slice()` |
```

For object pages, call out shallow behavior:

```md
`Object.assign()` copies properties into the target object. It is a shallow copy, so nested objects are still shared.
```

### JavaScript comparison sections

Add comparison sections wherever the Python reference would explain adjacent concepts.

High-value JavaScript comparisons:

- `Array` vs `Set`
- `Object` vs `Map`
- `Map` vs `WeakMap`
- `Set` vs `WeakSet`
- `null` vs `undefined`
- `Number` vs `BigInt`
- Function declarations vs expressions vs arrow functions
- Arrow functions vs regular functions
- `Promise.all()` vs `Promise.allSettled()` vs `Promise.race()` vs `Promise.any()`
- `==` vs `===`
- `for...of` vs `for...in`
- Local time vs UTC for `Date`

Use tables when the comparison is structural, then add a short paragraph of choosing guidance.

### JavaScript behavioral notes and limitations

Each JavaScript page should name the edge cases and behavioral details that matter for that concept. Use dry, technical language. Avoid informal labels such as "gotchas" in final page headings.

Examples:

- `Array`: sparse arrays, `sort()` mutating and sorting as strings by default, `length` truncation.
- `Object`: prototype inheritance, `typeof null`, shallow copying, property order rules when relevant.
- `Number`: floating-point precision, `NaN`, `Infinity`, safe integer limits.
- `String`: immutability, UTF-16 indexing, `slice()` vs `substring()`.
- `Date`: parsing date strings, zero-based months, local vs UTC methods, mutating setters.
- `Promise`: unhandled rejections, sequential vs parallel `await`, `Promise.all()` short-circuit rejection.
- `RegExp`: escaping, global flag state with `test()`, greedy quantifiers.
- `Map` and `Set`: object identity for keys and values.
- `WeakMap` and `WeakSet`: non-iterability and object-only keys/values.

These should appear as `:::note`, `## Behavioral notes`, `## Limitations`, or `## Best practices` depending on page shape.

Prefer `## Behavioral notes` for facts that explain how the feature behaves:

- Immutability
- Indexing rules
- Type coercion
- Equality behavior
- Unicode behavior
- Local time vs UTC
- Iterator consumption

Prefer `## Limitations` for constraints:

- Deprecated APIs
- Unsupported input
- Runtime differences
- Non-iterability
- Object-only keys or values
- Precision limits

Do not add `## Common use cases` to JavaScript reference pages by default. If usage examples are needed, keep them compact and place them near the method or operation they demonstrate.

### JavaScript page acceptance criteria

A JavaScript reference page is ready when it can answer these questions without sending the reader elsewhere:

- What is this feature?
- How do I create or call it?
- What does it return?
- Does it mutate anything?
- What happens when input is missing, invalid, empty, or not found?
- What related feature might I confuse it with?
- What common error or edge case should be documented?
- What usage pattern is recommended by the reference?

If the page cannot answer most of these, keep editing.

### JavaScript object and primitive behavior

Call out JavaScript's common surprises:

- `typeof []` returns `"object"`.
- `typeof null` returns `"object"`.
- Arrays are objects with numeric indexes and a `length` property.
- `null` is intentional absence; `undefined` usually means not assigned, not returned, or not found.
- `const` prevents reassignment, not object or array mutation.
- `NaN` is not equal to itself; prefer `Number.isNaN()`.
- `Map` preserves insertion order and supports non-string keys.
- `Set` stores unique values.
- `WeakMap` and `WeakSet` are not iterable and only hold objects.

Use admonitions for these surprises when they prevent real bugs.

### JavaScript methods, static methods, and properties

Separate method categories when the distinction matters:

- `## Number methods`
- `## Number static methods`
- `## Number properties`
- `## Promise methods`
- `## Object methods`
- `## String methods`

Use callable headings with parentheses:

```md
### `Array.isArray()`
### `Promise.all()`
### `toString()`
```

For properties, omit parentheses:

```md
### `length`
### `Number.MAX_SAFE_INTEGER`
```

### JavaScript async behavior

For `Promise`, `async`, and generator pages:

- Explain states or phases before method catalogs.
- Show error handling close to the first async example.
- Distinguish sequential and parallel execution.
- Say whether a method waits for all work, the first settled promise, or the first fulfilled promise.
- Prefer `async`/`await` in best-practice sections, but include `.then()` and `.catch()` because they are core reference material.

## Admonitions

Use Docusaurus admonitions when the note is important enough to interrupt the flow:

```md
:::note
This explains a surprising behavior or useful context.
:::
```

Recommended uses:

- JavaScript `typeof null`
- JavaScript REPL declarations returning `undefined`
- Python assignment vs copying mutable objects
- Deprecated APIs
- Error behavior that surprises beginners
- Version-specific syntax

Keep admonitions short. Do not use them for ordinary explanation that belongs in the main text.

## Tables

Use tables for compact comparison or protocol information:

- Keyword category tables
- Dunder method tables
- `Map` vs `Object`
- `Set` vs `Array`
- `list` vs `tuple`
- Truthy/falsy summaries
- Method return behavior summaries

Tables should be scan-friendly:

- Keep columns few.
- Keep cell text short.
- Use code formatting for syntax and API names.
- Put longer explanations below the table.

## Cross-links

Cross-link related reference pages when a reader is likely to need the neighbor concept.

Use relative links:

```md
[`float`](./float)
[`Promise`](./promise)
[`None`](./none)
```

Common useful links:

- JavaScript `Array` <-> `Object`, `Map`, `Set`
- JavaScript `null` <-> `undefined`
- JavaScript `Promise` <-> `async`
- JavaScript `Number` <-> `BigInt`
- Python `list` <-> `tuple`
- Python `dict` <-> `set`
- Python `bytes` <-> `bytearray` and `memoryview`
- Python `int` <-> `float`, `complex`, and `bool`
- Python built-ins <-> corresponding type pages

Use links to clarify relationships, not to turn every term into a link.

## Deprecated, dangerous, and discouraged features

Label deprecated or discouraged features directly in headings or the first sentence:

```md
### `substr` (deprecated)
### `with` (deprecated)
```

For dangerous APIs, say why:

```md
`eval()` runs code from a string. Avoid it with untrusted input because it can execute harmful code.
```

When there is a safer alternative, name it.

## Accuracy rules

Reference pages need higher precision than broad guides.

Before adding or revising a fact, verify:

- The type of the returned value
- Whether the method mutates the original object
- Whether an operation raises an error or returns a fallback value
- Whether indexes include or exclude the end position
- Whether a method is static, instance-level, or global
- Whether a feature is language version specific
- Whether an example is valid syntax

Avoid vague claims such as:

```md
This is faster.
```

Prefer specific claims:

```md
Membership checks are usually clearer with a `set` when you only need to know whether a value is present.
```

## Editing checklist

Before publishing a language reference page, check:

- Frontmatter matches the surrounding reference section.
- The page has a clear `## Definition`.
- Examples use the correct language fence.
- Code examples are syntactically valid.
- Method entries say what they return.
- Mutating methods clearly say that they mutate.
- Common errors or missing-value behavior are explained.
- Headings use backticks for exact syntax and API names.
- Cross-links point to existing local pages.
- Deprecated or dangerous APIs are labelled.
- Tables are readable on narrow screens.
- Typos in headings, code fences, and key teaching sentences are fixed.

Common cleanup items in this section:

- Use `python`, not misspelled code fences such as `pyhon`.
- Use `constructor`, `straightforward`, `elements`, `indices`, `subtraction`, `arithmetic`, `refers`, and `emptying`.
- Use the correct assignment syntax in examples, such as `my_dict['fruit'] = 'banana'`.
- Keep heading capitalization consistent within a page.
- Avoid commented-out maintenance blocks unless they are intentionally useful.

## Relationship to tutorial guides

The reference pages can include teaching, but they should not become full tutorials.

Use tutorial-style explanation when:

- The concept is frequently misunderstood.
- A short mental model prevents bugs.
- The page introduces asynchronous behavior, mutation, identity, equality, or protocol methods.

Stay reference-focused when:

- Listing methods.
- Defining keywords.
- Showing built-in function behavior.
- Comparing related types.
- Documenting return values and errors.

The ideal page is a reliable lookup that also teaches enough context for the reader to use the feature correctly.

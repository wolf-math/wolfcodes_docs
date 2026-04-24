---
title: JavaScript Quirks
sidebar_position: 16
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Welcome to the weird part

By this point, you have learned the normal, useful, respectable parts of JavaScript.

Now it is time to meet the raccoons living behind the language.

JavaScript has a few behaviors that surprise almost everyone at first. Some are historical, some come from type coercion, and some are just the natural result of a language growing up in public since the 1990s.

The good news: these quirks are learnable.

The better news: once you know them, you stop being surprised and start being the person who says, "ah, yes, classic JavaScript."

## Quirk 1: `==` tries to be helpful and becomes unhelpful

JavaScript has two equality operators:

- `===` for strict equality
- `==` for loose equality

Strict equality compares both value and type.

```javascript
5 === 5;     // true
5 === "5";   // false
```

Loose equality converts values before comparing them.

```javascript
5 == "5";        // true
0 == false;      // true
"" == false;     // true
null == undefined; // true
```

This is the source of many "why would it do that?" moments.

It helps to think of `==` as JavaScript saying:

"These values are different, but I can change them until they become the same."

That is not always the kind of confidence you want in a program.

Use strict equality by default, especially in [conditionals](./control_flow/conditionals) and validation code.

## Quirk 2: truthy and falsy are everywhere

In JavaScript, conditions do not require actual booleans. Many values are treated as truthy or falsy.

```javascript
if ("wolf") {
  console.log("This runs");
}

if (0) {
  console.log("This does not run");
}
```

Falsy values include:

- `false`
- `0`
- `""`
- `null`
- `undefined`
- `NaN`

Everything else is truthy.

That means this works:

```javascript
const username = "Ada";

if (username) {
  console.log("User exists");
}
```

But it also means this can be a bug:

```javascript
const itemCount = 0;

if (itemCount) {
  console.log("Show item count");
}
```

That block does not run, because `0` is falsy.

If you want to check a specific value, be specific:

```javascript
if (itemCount === 0) {
  console.log("Cart is empty");
}
```

The full idea is covered in the [data types guide](./data_structures/data_types#truthy-and-falsy-values) and shows up constantly in [conditionals](./control_flow/conditionals).

## Quirk 3: numbers are not always great at decimal math

JavaScript uses floating-point numbers for regular numeric values.

That means some decimal calculations look... unsettling.

```javascript
0.1 + 0.2; // 0.30000000000000004
```

No, you did not break math.

No, your laptop is not haunted.

This is a normal floating-point limitation, and JavaScript is not the only language with it.

The important lesson is: do not rely on exact decimal equality for values like money.

```javascript
0.1 + 0.2 === 0.3; // false
```

Use integer cents or another safer approach when precision matters. This comes up in the [data types guide](./data_structures/data_types) and the [numbers guide](./data_structures/number).

## Quirk 4: `typeof null` is `"object"`

This is one of JavaScript's most famous historical oddities:

```javascript
typeof null; // "object"
```

`null` is not actually an object in the way beginners usually mean "object."

It is a long-standing language bug that became too famous to fix without breaking older code.

So if you need to check for `null`, do it directly:

```javascript
const value = null;

if (value === null) {
  console.log("The value is intentionally empty");
}
```

This is one reason the [data types guide](./data_structures/data_types) treats `null` and objects as different ideas, even though `typeof` gets weird here.

## Quirk 5: arrays are objects, but not all objects are arrays

This can be confusing at first:

```javascript
typeof []; // "object"
typeof {}; // "object"
```

Arrays are a special kind of object, which is why they share some object-like behavior.

But this check is not enough:

```javascript
const value = [];

if (typeof value === "object") {
  console.log("Technically true, but not very useful");
}
```

If you want to know whether something is an array, use:

```javascript
Array.isArray(value); // true
```

This becomes much easier once you have both the [arrays](./data_structures/arrays) and [objects](./data_structures/objects) mental models in place.

## Quirk 6: `const` does not make objects immutable

This one gets a lot of beginners.

`const` prevents reassignment of the variable name. It does not freeze the contents of an array or object.

```javascript
const user = { name: "Ada" };

user.name = "Grace";

console.log(user.name); // "Grace"
```

This fails:

```javascript
const user = { name: "Ada" };

// user = { name: "Grace" }; // TypeError
```

But mutating the existing object still works.

This is the difference between reassignment and mutation from the [variables and values guide](./data_structures/variables_and_values#reassignment-vs-mutation).

## Quirk 7: missing values come in two flavors

JavaScript has both `undefined` and `null`.

That can feel like the language looked at "no value" and said, "what if there were two?"

In practice:

- `undefined` often means a value was not set
- `null` often means a value was intentionally set to "no value"

```javascript
let name;
console.log(name); // undefined

const selectedUser = null;
console.log(selectedUser); // null
```

The distinction matters when reading APIs, function results, and object properties. The [data types guide](./data_structures/data_types) covers the mental model in more detail.

## Quirk 8: automatic semicolon insertion exists

JavaScript can insert semicolons for you in many cases. This is called **automatic semicolon insertion**.

That sounds convenient, and often it is.

It is also the sort of convenience that occasionally rearranges your furniture while you sleep.

For example, this code:

```javascript
return
{
  success: true
};
```

does **not** return the object.

JavaScript inserts a semicolon after `return`, so the function returns `undefined`.

Write it like this instead:

```javascript
return {
  success: true
};
```

This is one reason the [introduction guide](./basics/intro#semicolons-optional-but-recommended) recommends explicit semicolons for beginners.

## Quirk 9: scope can surprise you if you use `var`

Modern JavaScript uses `let` and `const` for good reasons.

`var` has function scope, not block scope:

```javascript
if (true) {
  var mystery = "I escaped";
}

console.log(mystery); // "I escaped"
```

That is legal JavaScript.

It is also a wonderful way to create bugs that feel like ghost stories.

This is why the guides recommend `const` and `let`, and why [scope and closures](./functions/scope_and_closures) spends time on block scope.

## A few more classics

The JavaScript internet has been collecting cursed examples for years. A lot of famous ones were popularized by [wtfjs](https://github.com/denysdovhan/wtfjs), which is basically a museum of "please explain this immediately."

Here are a few classics worth knowing.

### `NaN` is not equal to itself

```javascript
NaN === NaN; // false
```

Yes, really.

`NaN` means "not a number," and JavaScript follows floating-point rules here. If you specifically want to check this case, use `Number.isNaN()`:

```javascript
Number.isNaN(NaN); // true
```

This pairs nicely with the earlier reminder that [numbers](./data_structures/number) have some special cases.

### `Object.is()` disagrees with `===` in a few edge cases

```javascript
Object.is(NaN, NaN); // true
NaN === NaN;         // false

Object.is(-0, 0);    // false
-0 === 0;            // true
```

Most of the time `===` is what you want.

But if you ever see `Object.is()`, this is why it exists: it handles a few value-identity edge cases differently.

### The famous `baNaNa`

```javascript
"b" + "a" + +"a" + "a"; // "baNaNa"
```

The trick is `+"a"`, which tries to turn `"a"` into a number and gets `NaN`.

So this becomes:

```javascript
"b" + "a" + NaN + "a"; // "baNaNa"
```

It is silly, but it is also a good reminder that the `+` operator does both number addition and string concatenation depending on the values involved. That behavior starts in the [variables and values guide](./data_structures/variables_and_values) and shows up all over JavaScript.

### `null` compared to `0` is weird in different ways

```javascript
null == 0;  // false
null > 0;   // false
null >= 0;  // true
```

This feels illegal, but it is the result of different comparison rules being used for equality vs relational operators.

This is a strong argument for keeping comparisons simple and explicit, especially in [conditionals](./control_flow/conditionals).

### `Math.min()` and `Math.max()` have dramatic default moods

```javascript
Math.min(); // Infinity
Math.max(); // -Infinity
```

These functions are designed to compare lists of numbers.

If there is no list:

- the minimum starts at `Infinity`
- the maximum starts at `-Infinity`

It looks ridiculous when you first see it, but it actually makes the reduction logic work.

## None of this means JavaScript is bad

JavaScript is unusual, not useless.

In fact, part of becoming comfortable with JavaScript is learning which parts are ordinary and which parts come with historical seasoning.

The quirks stop feeling random once you know the rules behind them:

- Use `===` instead of `==`
- Be careful with truthy and falsy values
- Do not expect perfect decimal math
- Check arrays with `Array.isArray()`
- Remember that `const` prevents reassignment, not mutation
- Prefer `let` and `const` over `var`

## Final advice

When JavaScript does something surprising, do not panic.

Reduce the example.
Log the values.
Check the types.
Ask whether coercion, mutation, or scope is involved.

Usually the language is not being random.

Usually it is being extremely consistent with a rule you did not know existed yet.

Which, admittedly, is a very JavaScript way to be weird.

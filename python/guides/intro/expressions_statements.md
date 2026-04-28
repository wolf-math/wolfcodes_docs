---
title: Expressions vs Statements
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
## What are expressions and statements?

Python code can be divided into two broad categories: **expressions** and **statements**. Understanding the difference helps you understand how Python behaves and why some pieces of code produce values while others simply perform actions.

## Why this matters

This distinction shows up constantly in real Python code.

In the vinyl tracker project, for example:

- a value like `"Blue Train"` is part of an expression
- a line like `print("Blue Train")` is a statement that does something

Knowing the difference will make later topics like variables, functions, and conditionals easier to follow.

## Expressions

**Expressions** are code that **produces a value**. They evaluate to something you can use:

```python
1959 + 10
"Blue " + "Train"
```

Think of expressions as questions Python can answer with a value.

**What happens:**

- `1959 + 10` evaluates to `1969`
- `"Blue " + "Train"` evaluates to `"Blue Train"`

**Key idea:** Expressions have a value. You can use them anywhere you need a value.

:::note
You'll learn more about expressions when you study [operators](../types_variables/operators). For now, just know that expressions produce values.
:::

## Statements

**Statements** are code that **does something** but doesn't produce a value you can use directly:

```python
print("Now spinning: Rumours")
```

Statements:
- Perform actions (like printing, assigning values to variables)
- Don't produce values you can use
- Are the "commands" that make your program do things

**Key idea:** Statements are "commands" that Python executes. They do work but don't give you a value back.

:::note
You'll see more examples of statements when you learn about [variables](../types_variables/variables) and [conditionals](../control_flow/conditionals). For now, just know that statements perform actions.
:::

## Seeing both together

Expressions and statements often appear together:

```python
record_title = "Blue " + "Train"
print(record_title)
```

**What happens:**

1. `"Blue " + "Train"` is an expression that produces the value `"Blue Train"`
2. `record_title = ...` is an assignment statement that stores that value
3. `print(record_title)` is a statement that displays it

## In the vinyl tracker

Even a tiny project snippet can show the difference clearly:

```python
record_title = "Are You Experienced"
artist = "The Jimi Hendrix Experience"
print(artist + " - " + record_title)
```

Here:

- `"Are You Experienced"` is an expression
- `"The Jimi Hendrix Experience"` is an expression
- `artist + " - " + record_title` is an expression that builds a new string
- each assignment line is a statement
- `print(...)` is a statement

This is the kind of small, music-focused code that will later grow into the full record library app.

## Summary

Understanding expressions vs statements helps you understand how Python works:

- **Expressions** produce values
- **Statements** perform actions
- The two often appear together in real code
- Both show up constantly in the record-library project and in everyday Python programs

As you learn more Python, you will see expressions and statements everywhere. Recognizing which is which will help you read code more confidently and write clearer programs.

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
Python code can be divided into two categories: **expressions** and **statements**. In short: **expressions** product a value, **statements** perform an action.

### Expressions

**Expressions** are code that **produces a value**.

```python
5 + 3              # Expression → produces 8
"hello" + "world"  # Expression → produces "helloworld"
```

:::note
You'll learn more about expressions when you study [operators](../types_variables/operators). For now, just know that expressions produce values.
:::

### Statements

**Statements** are code that **does something** but doesn't produce a value you can use directly:

```python
print("Hello")  # Statement → prints something (doesn't give you a value back)
```

Statements:
- Perform actions (like printing, assigning values to variables)
- Don't produce values you can use
- Are the "commands" that make your program do things

:::note
You'll see more examples of statements when you learn about [variables](../types_variables/variables) and [conditionals](../control_flow/conditionals). For now, just know that statements perform actions.
:::

### Why this matters

Understanding expressions vs statements helps you understand:

- **Why some code produces values and some don't:**
  - `5 + 3` is an expression—it produces the value `8`
  - `print("Hello")` is a statement—it does something (prints) but doesn't give you a value

- **The difference between doing something and getting a value:**
  - Expressions give you something you can use
  - Statements just do work

This distinction will become clearer as you learn more about [operators](../types_variables/operators) and other Python features. For now, just remember: expressions produce values, statements perform actions.

## Summary

Understanding expressions vs statements helps you understand how Python works:

- **Expressions** produce values—they're like "questions" that Python answers with a value (e.g., `5 + 3` produces `8`)
- **Statements** perform actions—they're "commands" that do work but don't give you a value back (e.g., `print("Hello")` prints but doesn't return a value)

---
title: Operators
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
## What are operators?

**Operators** are symbols and keywords that perform operations on values.

```python
purchase_price = 18.0
estimated_value = 31.5
profit = estimated_value - purchase_price
```

In this example, `-` is an operator. It takes two values and produces a result.

## Why this matters

Operators are part of almost every useful Python expression.

You use them to:

- do math
- compare values
- update variables
- combine conditions

The vinyl tracker project depends on operators for things like comparing years, calculating profits, checking conditions, and building printed labels.

## Arithmetic operators

Arithmetic operators work with numbers.

| Operator | Name | Example |
|----------|------|---------|
| `+` | addition | `18 + 4` |
| `-` | subtraction | `31.5 - 18.0` |
| `*` | multiplication | `3 * 12` |
| `/` | division | `45 / 2` |
| `//` | floor division | `45 // 2` |
| `%` | modulo | `45 % 2` |
| `**` | exponentiation | `2 ** 3` |

### Basic arithmetic

```python
purchase_price = 18.0
estimated_value = 31.5
profit = estimated_value - purchase_price
```

```python
profit  # 13.5
```

You can also use operators directly:

```python
1959 + 10
24.0 / 2
```

### Floor division and modulo

Floor division rounds down:

```python
45 // 2  # 22
```

Modulo gives the remainder:

```python
45 % 2  # 1
```

These are useful when you want to group values, split quantities, or check patterns like even and odd numbers.

### Exponentiation

`**` raises a value to a power:

```python
2 ** 3  # 8
```

## Comparison operators

Comparison operators compare values and return `True` or `False`.

| Operator | Name | Example |
|----------|------|---------|
| `==` | equal to | `year == 1977` |
| `!=` | not equal to | `genre != "Jazz"` |
| `>` | greater than | `estimated_value > purchase_price` |
| `<` | less than | `year < 1980` |
| `>=` | greater than or equal to | `record_count >= 10` |
| `<=` | less than or equal to | `year <= 1967` |

```python
year = 1977
year == 1977
year < 1980
```

These comparisons are the basis for later conditionals.

:::important
`=` assigns a value.

`==` compares values.

They do different jobs.
:::

## Assignment operators

The `=` operator assigns a value to a variable:

```python
record_count = 3
```

Python also supports augmented assignment:

```python
record_count += 1
estimated_value -= 2.5
```

These are shortcuts for:

```python
record_count = record_count + 1
estimated_value = estimated_value - 2.5
```

They are especially useful when a variable changes over time.

## Logical operators

Logical operators combine conditions.

| Operator | Name | Example |
|----------|------|---------|
| `and` | logical AND | `year >= 1950 and year < 1960` |
| `or` | logical OR | `genre == "Jazz" or genre == "Rock"` |
| `not` | logical NOT | `not is_duplicate_copy` |

```python
year = 1959
genre = "Jazz"

year >= 1950 and year < 1960
genre == "Jazz" or genre == "Rock"
```

These become especially important in conditionals and truthiness checks.

## Operator precedence

When an expression has multiple operators, Python follows an order of operations.

```python
2 + 3 * 4
```

This evaluates to `14`, not `20`, because multiplication happens before addition.

Use parentheses when you want to make the order explicit:

```python
(2 + 3) * 4
```

That evaluates to `20`.

When in doubt, use parentheses for clarity.

## Operations between different types

Some mixed-type operations work, and some do not.

### What works

Strings can be joined:

```python
"Blue " + "Train"
```

Numbers of different numeric types can combine:

```python
18 + 2.5
```

Python will usually promote the result to a float when needed.

### What does not work

This causes an error:

```python
18 + " dollars"
```

Python does not know how to add a number directly to a string.

If you want to combine them, convert the number first:

```python
"Paid: $" + str(18)
```

## Common patterns

### Incrementing a value

```python
record_count = 3
record_count += 1
```

### Calculating totals

```python
purchase_price = 22.5
shipping_cost = 4.0
total_cost = purchase_price + shipping_cost
```

### Comparing values

```python
estimated_value = 35.0
purchase_price = 22.5
estimated_value > purchase_price
```

### Building labels

```python
artist = "Fleetwood Mac"
title = "Rumours"
label = artist + " - " + title
```

## In the vinyl tracker

Operators already let you write useful project logic:

```python
record_title = "Blue Train"
purchase_price = 18.0
sold_price = 31.5
profit = sold_price - purchase_price
is_profitable = sold_price > purchase_price
```

```python
print(record_title)
print(profit)
print(is_profitable)
```

That is a small version of logic the final capstone project really uses: math for values, comparisons for decisions, and string operations for display.

## Best practices

- use parentheses when they make an expression easier to read
- use augmented assignment like `+=` when updating a variable
- be careful when combining different types
- use `==` for comparison and `=` for assignment

## Summary

Operators are the tools Python uses to do work inside expressions.

They let you calculate values, compare data, update variables, and combine conditions. In the record-library project, operators are what turn stored values into useful behavior.

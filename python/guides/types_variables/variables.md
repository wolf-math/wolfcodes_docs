---
title: Variables
sidebar_position: 0
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What are variables?

**Variables** are names that refer to values. They let you store data, reuse it later, and give it a meaningful label.

```python
record_title = "Blue Train"
artist = "John Coltrane"
purchase_price = 18.0
```

In these examples, `record_title`, `artist`, and `purchase_price` are variables. Each one points to a value.

## Why this matters

Without variables, you would have to repeat values all over your code. That makes programs harder to read and harder to change.

Variables make code clearer:

- `record_title` is easier to understand than just seeing `"Blue Train"` everywhere
- changing one variable is easier than editing the same value in many places
- real programs depend on stored values for user input, calculations, and output

The vinyl record library tracker depends on variables constantly. Before you can build records, collections, prices, and menus, you need a way to store basic pieces of information.

## Creating variables

Use `=` to assign a value to a variable:

```python
record_title = "Blue Train"
artist = "John Coltrane"
year = 1957
```

**What happens:**

- `record_title` refers to the string `"Blue Train"`
- `artist` refers to the string `"John Coltrane"`
- `year` refers to the integer `1957`

Python does not require you to declare the type ahead of time. It figures out the type from the value you assign.

## Naming rules and style

Variable names in Python:

- can contain letters, digits, and underscores
- cannot start with a digit
- are case-sensitive
- should use `lower_snake_case`

Good examples:

```python
record_title = "Rumours"
estimated_value = 32.0
is_first_pressing = False
```

Less helpful examples:

```python
x = "Rumours"
y = 32.0
z = False
```

Use names that describe what the value means.

## Assignment and rebinding

Assignment gives a variable a value. Reassignment changes which value that variable refers to.

```python
record_title = "Blue Train"
record_title = "Giant Steps"
```

After the second line runs, `record_title` refers to `"Giant Steps"`.

This is called **rebinding**. The variable name stays the same, but the value it refers to changes.

## Multiple assignment

Python lets you assign multiple variables in one line:

```python
artist, album = "Miles Davis", "Kind of Blue"
```

You can also swap values:

```python
side_a, side_b = "So What", "Freddie Freeloader"
side_a, side_b = side_b, side_a
```

Underscore is often used as a throwaway variable when you do not care about one of the values:

```python
first_track, _, third_track = ["So What", "Freddie Freeloader", "Blue in Green"]
```

## Mutability and rebinding

Some values can be changed in place, while others cannot.

For example, lists are mutable:

```python
favorite_albums = ["Blue Train", "Rumours"]
same_list = favorite_albums
same_list.append("Are You Experienced")

print(favorite_albums)
```

**Output:**

```text
['Blue Train', 'Rumours', 'Are You Experienced']
```

Both names refer to the same list, so changing the list through one name affects the other.

Strings are different. They are immutable:

```python
artist = "Miles"
artist = artist + " Davis"
```

That second line creates a new string and rebinds `artist` to it.

## Identity vs equality

Two values can look the same without being the exact same object.

- `==` checks whether values are equal
- `is` checks whether two names refer to the same object

```python
record_a = ["Blue Train", "Jazz"]
record_b = ["Blue Train", "Jazz"]
record_c = record_a
```

```python
record_a == record_b  # True
record_a is record_b  # False
record_a is record_c  # True
```

Use `==` most of the time. Use `is` mainly when checking for `None`.

## In the vinyl tracker

Variables are the first real building blocks of the project.

```python
record_title = "Are You Experienced"
artist = "The Jimi Hendrix Experience"
genre = "Psychedelic Rock"
purchase_price = 22.5
estimated_value = 35.0
```

Even before you learn lists, dictionaries, or classes, this already gives you a useful mini-model of one record.

You can print that information right away:

```python
print(artist + " - " + record_title)
print("Genre:", genre)
print("Paid:", purchase_price)
```

That is exactly the direction the capstone project grows in. First you store one piece of record data. Later you group many records together and build real features around them.

## Tips for beginners

- Choose descriptive names like `record_title`, `artist`, and `estimated_value`
- Keep one variable focused on one idea
- Avoid reusing the same variable name for unrelated values
- Use `print()` and `type()` when you want to inspect what a variable currently refers to

## Summary

Variables are names that refer to values. They help you store data, reuse it, and make your code easier to read.

In Python, you create variables with `=`, you can reassign them later, and you should choose clear names that match their purpose. In the vinyl tracker project, variables are the first step toward modeling real record data.

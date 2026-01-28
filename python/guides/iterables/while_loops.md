---
title: While Loops
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
While loops repeat code as long as a condition remains true. Unlike [for loops](./for_loops) that iterate over a fixed collection, while loops continue until their condition becomes false, making them perfect for situations where you don't know in advance how many iterations you'll need.

## What are while loops?

A **while loop** repeatedly executes a block of code as long as a condition is truthy. The condition is checked before each iteration, and the loop continues until the condition becomes falsy.

## Why this matters

While loops are essential when you need to repeat code an unknown number of times, continuing until a condition changes. They're perfect for situations where you don't know in advance how many iterations you'll need, like reading input until a valid value is entered, processing data until a certain state is reached, or running game loops until the game ends. While loops give you flexibility that for loops can't provide when the termination condition depends on runtime behavior rather than a fixed sequence. Understanding when to use while loops versus for loops helps you choose the right tool for each situation and write code that handles dynamic, condition-based repetition.

## Basic syntax

The basic form of a while loop looks like this:

```python
while <condition>:
    <code to run>
```

The condition is evaluated before each iteration. If it's truthy, the indented code block runs. After the block executes, Python checks the condition again.

## Simple example

```python
count = 0

while count < 5:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
```

This loop runs as long as `count < 5` is `True`. Inside the loop, we increment `count`, so eventually the condition becomes `False` and the loop stops. 

If we don't increment `count`, the loop can run [infinitely](#infinite-loops).

## While vs for loops

Both loops repeat code, but they're used in different situations:

- **[For loops](./for_loops)**: When you know what you're iterating over ([lists](./lists), [ranges](./ranges), etc.) or how many times to repeat
- **While loops**: When you need to repeat until a condition changes, and you don't know the exact number of iterations

```python
# For loop: iterate over a known sequence
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# While loop: repeat until a condition is met
count = 0
while count < 5:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
```

Both achieve the same result, but for loops are generally preferred when you know the iteration count.

## Common patterns

### Counting

Use a counter variable to control the loop:

```python
count = 0
while count < 10:
    print(count)
    count += 1  # Increment the counter

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

### User input validation

Continue until valid input is received:

```python
age = None

while age is None:
    user_input = input("Enter your age: ")
    if user_input.isdigit():
        age = int(user_input)
    else:
        print("Please enter a valid number")

# Example interaction:
# Enter your age: abc
# Please enter a valid number
# Enter your age: 25
# (loop exits, age is now 25)
```

The [`isdigit`](../../language_reference/string#isdigit) method checks if a string can be cast into a number. If `user_input.isdigit()` returns `True`, then the user input a number, otherwise the loop repeats. 

### Processing until a value changes

Loop until a condition is met:

```python
total = 0
number = 1

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    total += number

print(f"Total: {total}")

# Example interaction:
# Enter a number (0 to stop): 5
# Enter a number (0 to stop): 10
# Enter a number (0 to stop): 3
# Enter a number (0 to stop): 0
# Total: 18
```

### Menu systems

Create interactive menus:

```python
choice = ""

while choice != "quit":
    print("1. Option 1")
    print("2. Option 2")
    print("Type 'quit' to exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("You chose option 1")
    elif choice == "2":
        print("You chose option 2")

# Example interaction:
# 1. Option 1
# 2. Option 2
# Type 'quit' to exit

# Enter choice: 1

# You chose option 1
# 1. Option 1
# 2. Option 2
# Type 'quit' to exit

# Enter choice: quit

# (loop exits)
```

## Infinite loops

An **infinite loop** is a loop that never stops because its condition never becomes false. These are usually bugs, but sometimes intentional.

### Unintentional infinite loops

```python
# BUG: This runs forever!
count = 0
while count < 5:
    print(count)
    # Forgot to increment count!

# Output (runs infinitely):
# 0
# 0
# 0
# ... (continues forever)
```

The condition `count < 5` is always `True` because `count` never changes.

:::note
To stop an infinite loop type `ctrl + c` in the terminal. On Mac it's still `ctrl`, not `command`. 
:::

### Intentional infinite loops

Sometimes you want an infinite loop (often with a `break` statement):

```python
while True:  # Infinite loop
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break  # Exit the loop
    print(f"You entered: {user_input}")

# Example interaction:

# Enter 'quit' to exit: hello
# You entered: hello

# Enter 'quit' to exit: world
# You entered: world

# Enter 'quit' to exit: quit
# (loop exits)
```

### Breaking out of infinite loops

Use `break` to exit when needed:

```python
while True:
    number = int(input("Enter a number (negative to stop): "))
    if number < 0:
        break
    print(f"Square: {number ** 2}")

# Example interaction:
# Enter a number (negative to stop): 3
# Square: 9
# Enter a number (negative to stop): 5
# Square: 25
# Enter a number (negative to stop): -1
# (loop exits)
```

## Loop control: break and continue

### `break`

Exit the loop immediately:

```python
count = 0
while count < 10:
    if count == 5:
        break  # Exit the loop
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
```

### `continue`

Skip to the next iteration:

```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)

# Output:
# 1
# 3
# 5
# 7
# 9
```

:::warning
Be careful with `continue` in while loops. Make sure you update any loop variables before using `continue`, or you might create an infinite loop!
:::

## The `else` clause

A `while` loop can have an `else` clause that runs if the loop completes normally (without a `break`):

```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed normally")

# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed normally

# With break
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("This won't print")

# Output:
# 0
# 1
# 2
```

The `else` clause is useful for checking if a loop found what it was looking for:

```python
numbers = [1, 3, 5, 7, 9]
target = 4
index = 0

while index < len(numbers):
    if numbers[index] == target:
        print(f"Found {target} at index {index}")
        break
    index += 1
else:
    print(f"{target} not found in list")

# Output:
# 4 not found in list
```

## Nested while loops

While loops can be nested, just like for loops:

```python
row = 0
while row < 3:
    col = 0
    while col < 3:
        print(f"({row}, {col})", end=" ")
        col += 1
    print()  # New line
    row += 1

# Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)
```

## Converting between for and while loops

Many for loops can be rewritten as while loops, and vice versa:

### For loop to while loop

```python
# For loop
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Equivalent while loop
i = 0
while i < 5:
    print(i)
    i += 1

# Output:
# 0
# 1
# 2
# 3
# 4
```

### While loop to for loop

```python
# While loop
items = ['apple', 'banana', 'orange']
count = 0
while count < len(items):
    print(items[count])
    count += 1

# Output:
# apple
# banana
# orange

# Equivalent for loop
for item in items:
    print(item)

# Output:
# apple
# banana
# orange
```

**Generally, use `for loops` when possible** because they're more Pythonic and less error-prone.

## Common use cases

### Input validation

Continue asking until valid input:

```python
while True:
    age = input("Enter your age: ")
    if age.isdigit() and 0 <= int(age) <= 120:
        age = int(age)
        break
    print("Invalid age. Please try again.")

# Example interaction:
# Enter your age: -5
# Invalid age. Please try again.
# Enter your age: 150
# Invalid age. Please try again.
# Enter your age: 25
# (loop exits, age is now 25)
```

### Game loops

Many games use while loops:

```python
game_running = True
score = 0

while game_running:
    # Game logic here
    action = input("What do you do? ")
    
    if action == "quit":
        game_running = False
    elif action == "score":
        print(f"Score: {score}")
    else:
        score += 1

# Example interaction:
# What do you do? move
# What do you do? jump
# What do you do? score
# Score: 2
# What do you do? quit
# (loop exits)
```

### Processing data until a condition

```python
numbers = []
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num == "done":
        break
    numbers.append(int(num))

print(f"Sum: {sum(numbers)}")

# Example interaction:
# Enter a number (or 'done' to finish): 5
# Enter a number (or 'done' to finish): 10
# Enter a number (or 'done' to finish): 3
# Enter a number (or 'done' to finish): done
# Sum: 18
```

### Retry logic

```python
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        result = risky_operation()
        break  # Success!
    except Exception:
        attempts += 1
        print(f"Attempt {attempts} failed. Retrying...")
else:
    print("All attempts failed")

# Example output (if all attempts fail):
# Attempt 1 failed. Retrying...
# Attempt 2 failed. Retrying...
# Attempt 3 failed. Retrying...
# All attempts failed
```

## Best practices

- **Prefer `for loops` when possible**: They're more readable and less error-prone
- **Always update loop variables**: Make sure the condition can become false, or you'll have an infinite loop
- **Use descriptive variable names**: `count`, `running`, `done` are better than `x`, `y`, `z`
- **Consider using `break` for infinite loops**: `while True:` with `break` can be clearer than complex conditions
- **Initialize variables before the loop**: Make sure loop variables exist before the loop starts
- **Think about edge cases**: What happens if the condition is false from the start?

```python
# Good: Clear condition and proper initialization
count = 0
while count < 10:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Good: Using break for clearer control
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    process(user_input)

# Avoid: Forgetting to update the loop variable
count = 0
while count < 10:
    print(count)
    # Missing: count += 1  (infinite loop!)
    # Output: prints 0 forever

# Better: Use a for loop when you know the iteration count
for i in range(10):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

## Summary

While loops repeat code as long as a condition is true:
- Use when you don't know the exact number of iterations
- Continue until a condition becomes false
- Support `break` and `continue` for control flow
- Can have `else` clauses like for loops
- Be careful to avoid infinite loops

While loops are powerful but require careful attention to ensure they terminate. Use them when you need to repeat code until a condition changes, and prefer for loops when iterating over known sequences.


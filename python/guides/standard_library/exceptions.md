---
title: Exception Handling
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What is exception handling?

**Exception handling** is how Python programs deal with errors gracefully. Instead of crashing when something goes wrong, you can catch exceptions, handle them, and continue running. The `try` and `except` keywords let you write code that anticipates and responds to errors.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
    result = None
```

## Why this matters

Errors happen in real programs. Sometimes files don't exist, networks fail, users enter invalid data, calculations go wrong. Without exception handling, your program would crash every time it encounters an error. Exception handling lets you:

- **Prevent crashes**: Catch errors and handle them gracefully
- **Provide better feedback**: Show users meaningful error messages instead of cryptic tracebacks
- **Continue execution**: Recover from errors and keep your program running
- **Clean up resources**: Ensure files are closed, connections are terminated, etc., even when errors occur

Understanding `try`/`except` is essential for writing robust Python programs that work reliably in the real world.

## Basic `try`/`except` syntax

The simplest form catches any exception:

```python
try:
    # Code that might raise an exception
    risky_operation()
except:
    # What to do if an exception occurs
    print("Something went wrong!")
```

However, catching all exceptions is usually too broad. It's better to catch specific exceptions.

## Catching specific exceptions

Python has many built-in exception types. Catch the ones you expect:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

### Common built-in exceptions

| Exception | When it's raised |
|-----------|------------------|
| `ValueError` | Wrong type of value (e.g., `int("abc")`) |
| `TypeError` | Wrong type used in operation (e.g., `"5" + 3`) |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key doesn't exist |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Object doesn't have the attribute |
| `NameError` | Variable name not found |

### Example: Handling multiple exceptions

```python
try:
    data = {"name": "Alice", "age": 30}
    print(data["email"])  # KeyError
    result = 10 / 0       # ZeroDivisionError
except KeyError:
    print("Key not found in dictionary")
except ZeroDivisionError:
    print("Division by zero error")
```

## Getting exception information

You can capture the exception object to get more details:

```python
try:
    result = int("not a number")
except ValueError as e:
    print(f"Error: {e}")  # Error: invalid literal for int() with base 10: 'not a number'
    print(f"Exception type: {type(e).__name__}")
```

The `as e` syntax binds the exception object to the variable `e`, which you can then inspect or log.

## The `else` clause

Use `else` to run code only if no exception occurred:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {number}")
    # This only runs if int() succeeded
```

The `else` block runs after the `try` block completes successfully, but before any `finally` block.

## The `finally` clause

Use `finally` to run cleanup code that **always** executes, whether an exception occurred or not:

```python
file = None
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    if file:
        file.close()  # Always closes, even if an error occurred
```

`finally` is perfect for:
- Closing files
- Releasing resources
- Cleaning up connections
- Resetting state

## Complete `try`/`except`/`else`/`finally` structure

You can combine all four clauses:

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except SpecificError:
    # Handle specific exception
    handle_error()
else:
    # Run if no exception occurred
    process_result(result)
finally:
    # Always run cleanup
    cleanup()
```

The order is always: `try` → `except` → `else` → `finally`.

## Practical examples

### Reading a file safely

```python
try:
    with open("config.json", "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("Config file not found. Using defaults.")
    data = "{}"
except PermissionError:
    print("Permission denied. Can't read config file.")
    data = "{}"
```

### Converting user input

```python
def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative")
            return age
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
```

### Accessing dictionary keys

```python
user_data = {"name": "Alice", "email": "alice@example.com"}

try:
    phone = user_data["phone"]
except KeyError:
    phone = "Not provided"
    print("Phone number not found, using default.")

print(f"Phone: {phone}")
```

## Raising exceptions

You can raise exceptions yourself using the `raise` keyword:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

### Re-raising exceptions

Sometimes you want to catch an exception, do something, then let it propagate:

```python
try:
    process_data()
except ValueError:
    log_error("Data processing failed")
    raise  # Re-raise the same exception
```

## Exception hierarchy

Python exceptions form a hierarchy. Catching a base exception will also catch its subclasses:

```python
try:
    risky_operation()
except Exception:  # Catches all exceptions
    print("Something went wrong")
except ValueError:  # More specific (but won't run if Exception catches it first)
    print("Value error")
```

**Important**: Put more specific exceptions first, then more general ones:

```python
try:
    operation()
except ValueError:      # Specific first
    handle_value_error()
except Exception:        # General last
    handle_any_error()
```

## Best practices

**1. Be specific**

Don't catch everything unless you have a good reason:

```python
# Bad: too broad
try:
    do_something()
except:
    pass

# Good: specific
try:
    do_something()
except ValueError:
    handle_value_error()
```

**2. Don't suppress errors silently**

At minimum, log the error:

```python
# Bad: silent failure
try:
    process_data()
except Exception:
    pass

# Good: log the error
try:
    process_data()
except Exception as e:
    logger.error(f"Failed to process data: {e}")
```

**3. Use finally for cleanup**

```python
# Good: ensures cleanup
resource = acquire_resource()
try:
    use_resource(resource)
finally:
    release_resource(resource)
```

**4. Let exceptions propagate when appropriate**

Not every error needs to be caught. Sometimes it's better to let the exception bubble up:

```python
def calculate_total(items):
    # Don't catch errors here - let caller handle them
    return sum(item.price for item in items)
```

## Common patterns

### Retry logic

```python
import time

def fetch_data_with_retry(max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return fetch_from_api()
        except ConnectionError:
            if attempt < max_attempts - 1:
                time.sleep(1)  # Wait before retry
            else:
                raise  # Give up after max attempts
```

### Default values

```python
def get_config_value(key, default=None):
    try:
        return config[key]
    except KeyError:
        return default
```

### Validation

```python
def validate_age(age):
    try:
        age = int(age)
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
        return age
    except (ValueError, TypeError):
        raise ValueError("Age must be a valid number")
```

## Summary

Exception handling with `try`/`except` is essential for writing robust Python programs:

- **`try`**: Code that might raise an exception
- **`except`**: Handle specific exceptions
- **`else`**: Run code when no exception occurs
- **`finally`**: Always run cleanup code
- **`raise`**: Create your own exceptions

**Use exception handling to:**
- Prevent crashes
- Provide better error messages
- Clean up resources
- Handle expected errors gracefully

**Remember:** catch specific exceptions, don't suppress errors silently, and use `finally` for cleanup. With these tools, you can write programs that handle errors gracefully and continue running even when things go wrong.


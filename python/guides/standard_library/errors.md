---
title: Errors and Exceptions
sidebar_position: 0.5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What are errors and exceptions?

**Errors** (also called **exceptions**) are Python's way of signaling that something went wrong during program execution. When Python encounters a problem it can't handle, it **raises** an exception, which stops normal execution and can crash your program if not handled.

```python
>>> 10 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> int("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'
```

In Python, "error" and "exception" are often used interchangeably. Technically, exceptions are a type of error that can be caught and handled, while some errors (like syntax errors) happen before the program runs and can't be caught.

## Why this matters

Understanding errors is crucial because:

- **Debugging**: Knowing what different error types mean helps you fix bugs faster
- **Error handling**: You can catch specific errors and handle them appropriately
- **Code quality**: Raising meaningful errors makes your code more maintainable
- **User experience**: Custom errors provide clearer feedback than generic ones
- **API design**: Well-designed error hierarchies make your code easier to use

Errors aren't just problems to avoid, they're a communication mechanism. When used well, they tell you (and other developers) exactly what went wrong and why.

## Common built-in exception types

Python has many built-in exception types. Here are the most common ones you'll encounter:

### `TypeError`

Raised when an operation is performed on an object of inappropriate type:

```python
>>> "hello" + 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> len(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
```

### `ValueError`

Raised when a function receives an argument of correct type but inappropriate value:

```python
>>> int("abc")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'abc'

>>> [1, 2, 3].index(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 5 is not in list
```

### `IndexError`

Raised when trying to access an index that doesn't exist:

```python
>>> numbers = [1, 2, 3]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

### `KeyError`

Raised when trying to access a dictionary key that doesn't exist:

```python
>>> data = {"name": "Alice", "age": 30}
>>> data["email"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'email'
```

### `AttributeError`

Raised when trying to access an attribute or method that doesn't exist:

```python
>>> text = "hello"
>>> text.append("world")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'
```

### `NameError`

Raised when a variable name is not found:

```python
>>> print(undefined_variable)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'undefined_variable' is not defined
```

### `ZeroDivisionError`

Raised when trying to divide by zero:

```python
>>> 10 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

### `FileNotFoundError`

Raised when trying to open a file that doesn't exist:

```python
>>> open("nonexistent.txt")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'
```

## Raising exceptions

You can raise exceptions in your own code using the `raise` statement. This is useful for:

- Validating input
- Signaling error conditions
- Stopping execution when something goes wrong

### Basic raise syntax

```python
raise ExceptionType("Error message")
```

### Raising built-in exceptions

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

divide(10, 0)  # Raises ZeroDivisionError: Cannot divide by zero
```

### Raising with a message

Always include a helpful error message:

```python
def get_age():
    age = input("Enter your age: ")
    if not age.isdigit():
        raise ValueError(f"'{age}' is not a valid age. Please enter a number.")
    return int(age)
```

### Exception propagation

When you raise an exception, it propagates up through the call stack until it's caught or the program crashes. This means exceptions raised in a function will bubble up to the caller:

```python
def inner_function():
    raise ValueError("Error in inner function")

def outer_function():
    inner_function()  # Exception propagates from here
    print("This won't execute")

outer_function()  # Exception propagates here and crashes the program
```

When you learn about exception handling, you'll see how to catch exceptions at different levels and optionally re-raise them to let them continue propagating.

## Exception hierarchy

Python exceptions are organized in a hierarchy. All exceptions inherit from `BaseException`, but most user-defined exceptions should inherit from `Exception`:

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── StopAsyncIteration
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    ├── ReferenceError
    ├── RuntimeError
    ├── SyntaxError
    ├── SystemError
    ├── TypeError
    └── ValueError
```

Understanding this hierarchy is important because:

- **Related exceptions share a base class**: `IndexError` and `KeyError` both inherit from `LookupError`
- **You can create custom exceptions**: Inherit from appropriate base classes to fit into the hierarchy
- **Exception handling benefits**: When you learn about catching exceptions, you can catch a base class to handle all related exceptions

For example, `LookupError` is the parent of both `IndexError` and `KeyError`, so catching `LookupError` would catch both types of errors. This is covered in detail in the exception handling guide.

## Creating custom exceptions

You can create your own exception types by inheriting from `Exception` or one of its subclasses. This is useful for:

- Making errors more specific to your domain
- Providing clearer error messages
- Creating error hierarchies for your codebase
- Making it easier for users of your code to catch specific errors

### Basic custom exception

A custom exception is a **named error** that inherits from Python’s built-in `Exception` class.

```python
class InvalidEmailError(Exception):
    pass
```

Most of the time, `pass` is enough. The exception already knows how to behave because it inherits from `Exception`.

You only add more code if you want the error to **store extra information** or **change how it’s displayed**. For example:

```python
class InvalidEmailError(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(f"Invalid email address: {email}")
```

Now the exception remembers which email caused the problem.

For beginners, using `pass` is the normal and recommended approach.


### Custom exception with additional data

You can add attributes to store additional information:

```python
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds. Balance: ${balance}, Required: ${amount}"
        super().__init__(message)

def withdraw(account_balance, amount):
    if amount > account_balance:
        raise InsufficientFundsError(account_balance, amount)
    return account_balance - amount

# When withdrawal exceeds balance, raises exception with additional data
withdraw(100, 200)
# Raises: InsufficientFundsError: Insufficient funds. Balance: $100, Required: $200

# The exception object contains the additional information
# When caught, you can access: e.balance and e.amount
```

The exception stores both the balance and amount as attributes, making it easy to access this information when the exception is caught and handled.

### Exception hierarchies

Create related exceptions by inheriting from a base exception:

```python
class DatabaseError(Exception):
    """Base exception for database-related errors."""
    pass

class ConnectionError(DatabaseError):
    """Raised when database connection fails."""
    pass

class QueryError(DatabaseError):
    """Raised when a database query fails."""
    pass

# You can raise any of these exceptions
raise ConnectionError("Failed to connect to database")
# Raises: ConnectionError: Failed to connect to database

raise QueryError("Invalid SQL query")
# Raises: QueryError: Invalid SQL query

# Because ConnectionError and QueryError inherit from DatabaseError,
# they are both instances of DatabaseError
error = ConnectionError("Connection failed")
isinstance(error, DatabaseError)  # True
```

This hierarchy allows you to catch all database-related errors by catching `DatabaseError`, or catch specific errors like `ConnectionError` individually. Exception handling is covered in detail in the next guide.

### When to create custom exceptions

Create custom exceptions when:

1. **You need specific error handling**: Different code paths for different error types
2. **Built-in exceptions don't fit**: Your error doesn't match any standard exception
3. **You're building a library**: Users need to catch specific errors from your code
4. **You want clearer error messages**: Custom exceptions can provide domain-specific context

```python
# Good: Custom exception for domain-specific error
class UserNotFoundError(Exception):
    """Raised when a user cannot be found."""
    pass

def get_user(user_id):
    user = database.find_user(user_id)
    if not user:
        raise UserNotFoundError(f"User with ID {user_id} not found")
    return user

# When user doesn't exist, raises specific exception
get_user(999)
# Raises: UserNotFoundError: User with ID 999 not found

# When user exists, returns normally
user = get_user(123)
# Returns: user object
```

Custom exceptions make it clear what went wrong. When you learn about exception handling, you'll be able to catch `UserNotFoundError` specifically and provide appropriate feedback, or catch `DatabaseError` to handle database connection issues separately.

## Best practices

1. **Use specific exception types**

```python
# Good: Specific exception
if age < 0:
    raise ValueError("Age cannot be negative")

# Less ideal: Generic exception
if age < 0:
    raise Exception("Age cannot be negative")
```

2. **Include helpful error messages**

```python
# Good: Descriptive message
raise ValueError(f"Expected positive number, got {value}")

# Less helpful: Generic message
raise ValueError("Invalid value")
```

3. **Don't raise generic Exception**

```python
# Avoid this
raise Exception("Something went wrong")

# Prefer specific exceptions
raise ValueError("Invalid input")
raise TypeError("Expected string, got int")
```

4. **Document your exceptions**

```python
class PaymentError(Exception):
    """Base exception for payment processing errors.
    
    Attributes:
        amount: The payment amount that caused the error
        reason: Human-readable reason for the failure
    """
    def __init__(self, amount, reason):
        self.amount = amount
        self.reason = reason
        super().__init__(f"Payment of ${amount} failed: {reason}")
```

5. **Use exception chaining**

When you catch one exception and raise another, you can use `from` to preserve the original exception. This creates a chain that shows both the original error and the new error:

```python
# Example of exception chaining (you'll learn to catch exceptions in the next guide)
# When FileNotFoundError is caught, you can raise a new exception while preserving the original:

# raise ConfigurationError("Failed to load configuration") from original_exception
```

This preserves the original exception in the `__cause__` attribute, making debugging easier by showing the full chain of errors. Exception chaining is covered in detail when you learn about exception handling.

## Common patterns

### Validation functions

```python
def validate_positive_number(value):
    """Validate that value is a positive number."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected number, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"Expected positive number, got {value}")
    return value
```

### Assertion-style checks

```python
def process_order(order):
    if not order.items:
        raise ValueError("Order must contain at least one item")
    if order.total < 0:
        raise ValueError("Order total cannot be negative")
    # Process order...
```

### Resource availability

```python
class ResourceUnavailableError(Exception):
    """Raised when a required resource is unavailable."""
    pass

def connect_to_service():
    if not is_service_available():
        raise ResourceUnavailableError("Service is currently unavailable")
    # Connect...
```

## Summary

Understanding errors and exceptions is essential for writing robust Python code:

- **Built-in exceptions**: Python provides many exception types for common error conditions
- **Raising exceptions**: Use `raise` to signal errors in your code
- **Custom exceptions**: Create domain-specific exceptions for clearer error handling
- **Exception hierarchy**: Understand how exceptions relate to catch related errors
- **Best practices**: Use specific exceptions, helpful messages, and proper documentation

Errors aren't failures, they communicate problems clearly to the user. Well designed error handling makes your code more maintainable, debuggable, and user friendly.


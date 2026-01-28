---
title: Modules
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
## What are modules?

A **module** is a file containing Python code that can be imported and used in other Python programs. Think of modules as reusable libraries of code that let you organize your code into separate files, reuse functionality across projects, and tap into Python's vast standard library and third-party packages.

```python
import math

result = math.sqrt(16)  # 4.0
print(math.pi)          # 3.141592653589793
```

## Why this matters

Modules are the foundation of code organization in Python. They let you:

- **Organize code**: Split large programs into manageable, logical files
- **Reuse code**: Write functions once and use them in multiple programs
- **Use the standard library**: Access Python's built-in modules for common tasks (file handling, dates, math, etc.)
- **Share code**: Create modules that others can import and use
- **Avoid naming conflicts**: Keep code in separate namespaces

Without modules, you'd have to copy and paste code everywhere, leading to maintenance nightmares. Understanding modules is essential for writing clean, maintainable Python programs.

## Importing modules

The `import` statement loads a module and makes its contents available in your program.

### Basic import

```python
import math

print(math.sqrt(25))    # 5.0
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045
```

When you import a module, you access its contents using dot notation: `module_name.function_name()`.

### Import with alias

You can give a module a shorter name using `as`:

```python
import math as m

print(m.sqrt(25))       # 5.0
print(m.pi)             # 3.141592653589793
```

This is especially useful for modules with long names:

```python
import datetime as dt

now = dt.datetime.now()
```

### Import specific items

You can import specific functions, classes, or variables from a module:

```python
from math import sqrt, pi

print(sqrt(25))         # 5.0
print(pi)               # 3.141592653589793
```

When you import specific items, you don't need to use dot notation. The items available directly:

```python
from datetime import datetime

now = datetime.now()  # No need for datetime.datetime
```

### Import everything (not recommended)

You can import all items from a module using `*`:

```python
from math import *

print(sqrt(25))         # 5.0
print(pi)               # 3.141592653589793
```

:::warning
**This is usually not recommended**: It pollutes your namespace and can lead to naming conflicts. If you import `sqrt` from multiple modules, the last one wins, and you might not realize which `sqrt` you're using.
:::

### Combining import styles

You can mix different import styles:

```python
import math
from datetime import datetime, timedelta
import os as operating_system

print(math.sqrt(16))                    # 4.0
print(datetime.now())                  # Current datetime
print(operating_system.getcwd())       # Current directory
```

## Python standard library modules

Python comes with a comprehensive standard library, which is a collection of modules that are available in every Python installation. Here's a list of some of the most commonly used standard library modules:

### Text processing

- `re` - Regular expressions
- `string` - String constants and utilities

### Data types

- `datetime` - Date and time handling
- `collections` - Specialized container datatypes
- `copy` - Shallow and deep copy operations
- `pprint` - Data pretty printer

### Numeric and mathematical

- `math` - Mathematical functions
- `random` - Generate pseudo-random numbers
- `decimal` - Decimal fixed point and floating point arithmetic
- `statistics` - Statistical functions

### File and directory access

- `os.path` - Common pathname manipulations
- `pathlib` - Object-oriented filesystem paths

### Data persistence

- `json` - JSON encoder and decoder
- `pickle` - Python object serialization
- `sqlite3` - DB-API 2.0 interface for SQLite databases


### Cryptographic services

- `hashlib` - Secure hashes and message digests
- `secrets` - Generate secure random numbers for managing secrets

### Operating system interface

- `os` - Miscellaneous operating system interfaces
- `sys` - System-specific parameters and functions
- `io` - Core tools for working with streams

### Concurrent execution

- `threading` - Thread-based parallelism
- `multiprocessing` - Process-based parallelism
- `asyncio` - Asynchronous I/O


### Internet data handling

- `json` - JSON encoder and decoder
- `email` - Email and MIME handling package
- `base64` - Base16, Base32, Base64, Base85 Data Encodings

### Software packaging and distribution

- `venv` - Creation of virtual environments


You can explore any of these by importing them and checking their documentation with `help(module_name)` or by visiting the [official Python documentation](https://docs.python.org/3/library/).

## Creating your own modules

Any Python file can be a module. Just create a `.py` file and import it!

### Simple module example

Create a file called `greetings.py`:

```python
# greetings.py
def hello(name):
    """Say hello to someone."""
    return f"Hello, {name}!"

def goodbye(name):
    """Say goodbye to someone."""
    return f"Goodbye, {name}!"

PI = 3.14159
```

Now you can import and use it:

```python
import greetings

print(greetings.hello("Alice"))    # Hello, Alice!
print(greetings.goodbye("Bob"))    # Goodbye, Bob!
print(greetings.PI)                # 3.14159
```

Or import specific items:

```python
from greetings import hello, goodbye

print(hello("Alice"))              # Hello, Alice!
print(goodbye("Bob"))              # Goodbye, Bob!
```

### Module initialization

When a module is first imported, Python executes all the code in the module file. This is useful for initialization:

```python
# config.py
DATABASE_URL = "postgresql://localhost/mydb"
DEBUG = True

# This runs when the module is imported
print("Config module loaded!")
```

```python
import config
# Output: Config module loaded!

print(config.DATABASE_URL)  # postgresql://localhost/mydb
```

## The `__name__` variable

Every Python file has a special variable called `__name__` that tells you how the file is being used:

- If the file is run directly: `__name__ == "__main__"`
- If the file is imported: `__name__ == "module_name"`

### Using `__name__ == "__main__"`

This pattern lets you write code that runs when the file is executed directly, but not when it's imported:

```python
# calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# This code only runs when the file is executed directly
if __name__ == "__main__":
    print("Running calculator tests...")
    print(add(2, 3))        # 5
    print(multiply(4, 5))   # 20
```

When you run `python calculator.py` directly, the test code runs. But when you `import calculator` in another file, the test code doesn't run—only the functions are available.

This is perfect for:
- **Testing**: Run tests when the file is executed directly
- **CLI tools**: Make a module that can be both imported and run as a script
- **Examples**: Include example usage that doesn't run on import

## Module search path

When you import a module, Python searches for it in several locations:

1. **Current directory**: The directory containing your script
2. **PYTHONPATH**: Directories listed in the `PYTHONPATH` environment variable
3. **Standard library**: Python's built-in modules
4. **Site-packages**: Third-party packages (usually in `site-packages`)

You can see the search path:

```python
import sys

print(sys.path)
# ['/current/directory', '/usr/lib/python3.10', ...]
```

### Adding to the search path

You can add directories to the search path programmatically:

```python
import sys
sys.path.append('/path/to/my/modules')

import my_custom_module
```

However, it's usually better to structure your project properly or use proper package management.

## Packages: Organizing multiple modules

A **package** is a directory containing multiple modules. Packages help organize related modules together.

### Simple package structure

```
my_package/
    __init__.py
    module1.py
    module2.py
```

The `__init__.py` file (which can be empty) tells Python that the directory is a package.

### Using packages

```python
from my_package import module1, module2

module1.function1()
module2.function2()
```

Or import from subpackages:

```python
from my_package.subpackage import module3
```

## Common patterns

### Conditional imports

Sometimes you want to import a module only if it's available:

```python
try:
    import optional_module
except ImportError:
    optional_module = None

if optional_module:
    optional_module.do_something()
```

### Lazy imports

Import modules inside functions to reduce startup time:

```python
def process_data():
    import heavy_module  # Only imported when function is called
    return heavy_module.process()
```

### Module-level constants

Define constants at the module level:

```python
# constants.py
MAX_SIZE = 1000
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"
```

```python
from constants import MAX_SIZE, DEFAULT_TIMEOUT

if size > MAX_SIZE:
    raise ValueError("Size too large")
```

## Best practices

1. **Use descriptive module names**: `user_utils.py` is better than `utils.py`
2. **Keep modules focused**: Each module should have a clear, single purpose
3. **Document your modules**: Add docstrings at the top of module files:

   ```python
   """User management utilities.
   
   This module provides functions for creating, updating,
   and deleting user accounts.
   """
   ```

4. **Avoid circular imports**: Don't have module A import module B while module B imports module A
5. **Use `__all__` to control exports**: Explicitly define what should be imported with `from module import *`:

   ```python
   # my_module.py
   __all__ = ['public_function', 'PublicClass']
   
   def public_function():
       pass
   
   def _private_function():  # Not in __all__
       pass
   ```

6. **Prefer explicit imports**: `from module import specific_item` is clearer than `from module import *`

Modules are one of Python's most powerful features for code organization. Master them, and you'll write cleaner, more maintainable code!


---
title: Generator
sidebar_position: 25
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## Properties

```python
>>> def gen():
...     yield 1
...     yield 2
>>> g = gen()
>>> [name for name in dir(g) if not name.startswith("__")]
['close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
```

## Definition

A **generator** is an iterator created by a function that uses the `yield` keyword. Each `yield` pauses execution and produces a value; execution resumes from that point on the next iteration. Generators are single-use and lazy: values are produced on demand.

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)   # 1 2 3
```

## Creating generators

- **Generator function**: any function containing `yield`.
- **Generator expression**: `(expr for item in iterable if condition)`.

```python
# generator expression
>>> squares = (x*x for x in range(3))
>>> list(squares)
[0, 1, 4]
```

## Using generators

Generators implement the iterator protocol and can be consumed with `for`, `next`, `list()`, or any function that takes an iterable.

```python
g = count_up_to(2)
next(g)  # 1
next(g)  # 2
next(g)  # StopIteration
```

### Sending values in

`send` can inject a value into the generator, resuming it at the next `yield` expression.

```python
def echo():
    received = yield "ready"
    yield received

g = echo()
next(g)         # 'ready'
g.send("hi")    # 'hi'
```

### Throwing and closing

- `throw` raises an exception inside the generator.
- `close` raises `GeneratorExit` to stop the generator.

```python
g = count_up_to(10)
next(g)      # 1
g.close()    # stops the generator
```

## Dunder methods

| Dunder Method | Operation          | Example (normal syntax) | Example (dunder call)      |
| ------------- | ------------------ | ----------------------- | -------------------------- |
| `__next__`    | Get next value     | `next(gen)`             | `gen.__next__()`           |
| `__iter__`    | Iterator protocol  | `for x in gen`          | `gen.__iter__()`           |
| `__send__`    | Send a value in    | `gen.send(10)`          | `gen.__send__(10)`         |
| `__throw__`   | Raise in generator | `gen.throw(Exception)`  | `gen.__throw__(Exception)` |
| `__close__`   | Stop generator     | `gen.close()`           | `gen.__close__()`          |

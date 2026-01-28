---
title: Coroutine
sidebar_position: 24
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
>>> import inspect
>>> async def demo(): return 1
>>> coro = demo()
>>> [name for name in dir(coro) if not name.startswith("__")]
['close', 'cr_await', 'cr_code', 'cr_frame', 'cr_origin', 'cr_running', 'cr_suspended', 'send', 'throw']
```

## Definition

A **coroutine** is an awaitable object produced by calling an `async def` function. It represents work that will complete in the future and must be awaited, scheduled (e.g., via `asyncio.create_task`), or run in an event loop. Coroutine objects are single-use: once awaited to completion, they cannot be awaited again.

```python
import asyncio

async def fetch():
    return "done"

async def main():
    result = await fetch()   # await the coroutine
    print(result)

asyncio.run(main())
```

## Creating coroutines

```python
async def add(a, b):
    return a + b

coro = add(1, 2)  # calling an async function creates a coroutine object
```

Coroutines cannot be executed with a normal function call; they must be awaited or scheduled in an event loop:

```python
import asyncio

async def main():
    value = await add(1, 2)
    print(value)  # 3

asyncio.run(main())
```

## Running coroutines

- `await coro` — run inside another coroutine.
- `asyncio.run(coro)` — run from synchronous code (creates and manages the event loop).
- `asyncio.create_task(coro)` — schedule concurrently; returns a Task.

```python
import asyncio

async def work(name, delay):
    await asyncio.sleep(delay)
    return name

async def main():
    t1 = asyncio.create_task(work("a", 1))
    t2 = asyncio.create_task(work("b", 0.5))
    results = await asyncio.gather(t1, t2)
    print(results)  # ['a', 'b']

asyncio.run(main())
```

## Coroutine methods and attributes

### `send(value)`

Resumes the coroutine, sending a value into it (advanced; rarely used directly—mostly for generator-based coroutines).

```python
>>> async def consumer():
...     x = await asyncio.sleep(0, result=1)
...     return x
```

### `throw(exc)`

Raises the given exception inside the coroutine.

### `close()`

Stops the coroutine, raising `GeneratorExit` inside it.

### Attributes

- `cr_await` — current object being awaited (or `None`).
- `cr_running` — `True` while executing.
- `cr_frame` / `cr_code` — frame and code object (debugging).
- `cr_origin` / `cr_suspended` — metadata for where it was created / if suspended.

## Dunder methods

| Dunder Method | Operation                   | Example (normal syntax) | Example (dunder call) |
| --- | --- | --- | --- |
| `__await__`   | Make coroutine awaitable    | `await coro`            | `coro.__await__()`    |
| `__iter__`    | Await protocol (internal)   | `await coro`            | `coro.__iter__()`     |
| `__next__`    | Iteration step (internal)   | *(implicit during await)* | `coro.__next__()`  |

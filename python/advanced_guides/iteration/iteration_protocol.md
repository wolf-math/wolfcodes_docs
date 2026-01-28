---
title: The Iteration Protocol
sidebar_position: 1
description: Understand how iterables, iterators, and the iteration protocol power for-loops, generators, and streaming-style code.
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Why the iteration protocol matters

When you write:

```python
for item in things:
    ...
```

it’s tempting to think “Python is looping over the container `things`.”  
What actually happens is more precise:

- Python first asks `things` for **an iterator**.
- Then it repeatedly asks that iterator for the **next value** until the iterator says “I’m done.”

That idea that *“loops iterate over an iterator, not directly over the container”* is the **core** of the iteration protocol.

Understanding it helps you:

- **Design your own iterable types** cleanly (custom collections, tree walks, etc.).
- **Distinguish** generators, iterators, and plain sequences.
- **Debug weird behavior**, like “Why did this thing work once and then become empty?”
- **Build streaming, memory‑efficient pipelines** instead of materializing huge lists.

## The protocol in one paragraph

At the heart of Python’s iteration are two ideas and two “hooks”:

- **Iterable**: something you can call `iter(x)` on to get an iterator.
- **Iterator**: an object that:
  - has a `__next__()` method that returns the next value, and
  - eventually raises `StopIteration` when there are no more values.

The core hooks are:

- `__iter__(self)` → should **return an iterator**.
- `__next__(self)` → on the iterator object, **returns the next item** or **raises `StopIteration`** when finished.

If you remember just one thing, remember:

> **Iterable** = “can produce an iterator”  
> **Iterator** = “is the thing being advanced with `next()`”



## There is no such thing as a `for` loop

Whenever you write:

```python
for x in obj:
    body(x)
```

Python conceptually does something like:

```python
it = iter(obj)          # get an iterator from obj
while True:
    try:
        x = next(it)    # ask for the next item
    except StopIteration:
        break           # no more items, exit loop
    body(x)
```

This pattern – **get an iterator, repeatedly call `next()`, stop on `StopIteration`** – is what we mean by “the iteration protocol.”

The same idea powers:

- **Comprehensions**: list/set/dict comprehensions, generator expressions.
- **Built‑ins**: `sum`, `any`, `all`, `sorted`, `min`, `max`, `tuple`, `list`, etc.
- **Unpacking**: `a, b, *rest = some_iterable`.
- Many library functions that “consume” data.

Once you see `for` as “`while` + `next` + `StopIteration`,” many behaviors make more sense.



## `iter()` and `next()` as your mental model

Two built‑ins give you direct access to the protocol:

- `iter(x)` → **ask `x` for an iterator**.
- `next(it)` → **ask iterator `it` for the next value**.

Under the hood, these map onto the dunder methods:

- `iter(x)` typically does `x.__iter__()`.
- `next(it)` calls `it.__next__()`.

You can experiment in a REPL:

```python
data = [10, 20, 30]
it = iter(data)        # calls data.__iter__()

next(it)               # calls it.__next__(), returns 10
next(it)               # returns 20
next(it)               # returns 30
next(it)               # raises StopIteration
```

Thinking in terms of `iter()` and `next()` is the cleanest way to “see” what your code is really doing.



## Iterable vs iterator (and the exhaustion gotcha)

Let’s make the distinction explicit:

- **Iterable**: “can **produce** iterators.”
  - Examples: `list`, `tuple`, `dict`, `set`, `range`, many custom containers.
  - You can usually call `iter(x)` multiple times and get **independent** iterators.
- **Iterator**: “is the thing being **advanced**.”
  - Examples: `list_iterator`, `dict_keys` iterator, file objects, generator objects, many tools from `itertools`.

Most iterators are **single‑pass**:

- Once they have yielded all their values and raised `StopIteration`, they are said to be **exhausted**.
- Calling `next()` again will just raise `StopIteration` immediately.

### A very common bug

```python
it = iter([1, 2, 3])

for x in it:
    print(x)

for x in it:
    print("second loop:", x)
```

Output:

```text
1
2
3
```

…and then **nothing** from the second loop. Why?  
Because `it` is an **iterator**, not an iterable; it was exhausted by the first loop.

Typical fixes:

- **Recreate the iterator**:

  ```python
  data = [1, 2, 3]
  for x in data:
      ...
  for x in data:   # new iterator from the same iterable
      ...
  ```

- **Materialize to a list** if it’s cheap and you really need multiple passes:

  ```python
  items = list(it)  # consume once
  ```

- **Redesign your API** so that callers get a *fresh iterable* each time instead of a pre‑constructed iterator that may already be half used.



## Two common design patterns

When you design your own types, there are two popular approaches.

### A) Container is iterable; iterator is a separate object

Here, your collection produces **new iterators** on demand:

```python
class MyCollection:
    def __init__(self, items):
        self._items = list(items)

    def __iter__(self):
        return MyIterator(self._items)


class MyIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self   # iterators are their own iterables

    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        value = self._items[self._index]
        self._index += 1
        return value
```

**Benefits:**

- You can do multiple independent passes:

  ```python
  c = MyCollection([1, 2, 3])
  it1 = iter(c)
  it2 = iter(c)
  ```

- Clear separation between “data holder” (`MyCollection`) and “cursor” (`MyIterator`).

This is how many of Python’s built‑in containers work.

### B) Object is its own iterator

Sometimes you don’t need a separate iterator class.  
Instead, the object both **holds state** and **implements the iterator protocol**:

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self        # the object is its own iterator

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
```

**Benefits:**

- Very simple, especially for “single shot” processes.

**Cost:**

- It’s naturally **stateful and single‑pass**:

  ```python
  cd = CountDown(3)
  list(cd)      # [3, 2, 1]
  list(cd)      # [] — already exhausted
  ```

Be explicit in your docs if you choose this pattern: let callers know it’s single‑use.



## The sequence fallback protocol

What if an object doesn’t implement `__iter__` at all?

Python has an older, “sequence protocol” fallback:

- If `__iter__` is missing, `iter(x)` may try:
  - call `x.__len__()` (if present), and
  - repeatedly call `x.__getitem__(index)` starting at 0, increasing the index until it raises `IndexError`.

That means:

- Some “sequence‑like” objects will **still work in a `for` loop** even though they don’t define `__iter__`.
- This is mostly for **backwards compatibility**.

In modern code, it’s better to:

- **Implement `__iter__` explicitly** on your iterable types.
- Avoid depending on the `__len__`/`__getitem__` fallback except when wrapping truly legacy code.

Practical implication:

- If you see “It works in a `for` loop even though I can’t find `__iter__`,” it might be using this sequence protocol behind the scenes.



## Iterator helpers you should know

Python’s standard library includes many helpers that **produce or transform iterators**.

Some of the most useful built‑ins:

- `enumerate(iterable)` – yields `(index, value)` pairs.
- `zip(a, b, ...)` – walks multiple iterables in lockstep, yielding tuples.
- `reversed(seq)` – yields items from a sequence‑like object in reverse (needs either a `__reversed__` method or the sequence protocol).

A more advanced but very powerful pattern:

- `iter(callable, sentinel)` – wraps a *callable* into an iterator that:
  - calls the function each time you ask for `next()`,
  - stops when the callable returns the `sentinel` value.

Example: read lines from a file until an empty string:

```python
with open("data.txt") as f:
    for line in iter(f.readline, ""):
        process(line)
```

This is a neat way to turn “call this until it returns X” into a clean iterator.

Finally, the `itertools` module is a **treasure chest** of iterator tools:

- Infinite streams (`count`, `cycle`, `repeat`).
- Combinators (`chain`, `islice`, `takewhile`, `dropwhile`, `tee`, …).
- Useful for building **streaming pipelines** without creating intermediate lists.

You don’t need to memorize them all: just remember that “`itertools` is where the iterator power tools live.”



## `StopIteration` and why it’s special

`StopIteration` looks like an error, but in the context of iteration it means:

> “This iterator is finished. There are no more values.”

It plays several roles:

- Iterator objects’ `__next__` methods **raise `StopIteration`** to signal completion.
- Generator objects (from `def` with `yield`) **automatically raise `StopIteration`**:
  - when the function body runs off the end, or
  - when you use `return some_value` inside a generator; that value becomes the `.value` attribute of the `StopIteration` exception.

Normally, you *don’t* catch `StopIteration` yourself:

- The `for` loop, comprehensions, and most consumers handle it for you.

### One big pitfall: `StopIteration` leaking out of generators

Historically, if a generator **explicitly raised `StopIteration`** inside its body (instead of just ending), that exception could “leak out” and **silently stop** an outer loop.  
This turned out to be confusing and error‑prone.

Modern Python treats `StopIteration` inside a generator specially:

- If a `StopIteration` escapes from a generator’s body, it’s wrapped in a `RuntimeError`.
- This helps you see **“I accidentally raised `StopIteration` myself”** instead of silently terminating iteration.

The takeaway: let generators finish naturally; don’t raise `StopIteration` by hand inside them.



## Generators and generator objects in protocol terms

Consider a generator function:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

When you call `countdown(3)`, you don’t run the body right away. Instead, you get a **generator object**:

- That generator object is an **iterator**:
  - it has `__iter__` (returns itself),
  - and `__next__` (advance to the next `yield`).

So everything we’ve said about iterators applies directly:

```python
gen = countdown(3)
next(gen)     # 3
next(gen)     # 2
next(gen)     # 1
next(gen)     # raises StopIteration
```

Comparing styles:

- **Class‑based iterators**:
  - You write `__iter__` and `__next__` manually.
  - Often clearer when you need complex state, multiple methods, or a lot of control.
- **Generators**:
  - You write a normal‑looking function with `yield` statements.
  - Python builds the iterator machinery for you.

Conceptually they’re the same: both **implement the iteration protocol**.



## Iteration protocol vs async iteration protocol

Python also supports **asynchronous iteration**, which follows the same idea but adds `await`.

The async protocol uses:

- `__aiter__(self)` → returns an **asynchronous iterator**.
- `__anext__(self)` → returns an awaitable that eventually yields a value or raises `StopAsyncIteration`.

An `async for` loop conceptually does:

```python
ait = obj.__aiter__()
while True:
    try:
        item = await ait.__anext__()
    except StopAsyncIteration:
        break
    ...
```

If you’re comfortable with the **regular** iteration protocol, async iteration is the same pattern plus `await`.  
For a deeper dive, see the separate **Async Iteration** guide in this section.



## Testing and debugging iteration behavior

When something “iterates weirdly,” you can probe it directly in a REPL.

Quick checklist:

- **Does `iter(x)` work?**

  ```python
  it = iter(x)
  ```

- **Does `next(iter(x))` work?**

  ```python
  it = iter(x)
  first = next(it)
  ```

- **Are two iterators independent?**

  ```python
  it1 = iter(x)
  it2 = iter(x)
  next(it1)
  next(it2)    # does this still start from the beginning?
  ```

If `it1` and `it2` interfere with each other, you probably don’t have a true **re‑iterable** container; you might be working with a single shared iterator instead.

Here is a small “probe” snippet you can adapt:

```python
def inspect_iterable(x, n=3):
    print("type:", type(x))

    it1 = iter(x)
    print("first iterator next calls:")
    for _ in range(n):
        try:
            print("  ", next(it1))
        except StopIteration:
            print("  <exhausted>")
            break

    it2 = iter(x)
    print("second iterator first value (if any):")
    try:
        print("  ", next(it2))
    except StopIteration:
        print("  <exhausted immediately>")
```



## Common misconceptions

- **“Is an iterator the item inside the list?”**  
  No. Think of an iterator as a **cursor object** that walks over items.  
  The list holds the data; the iterator knows “where you are” in that data.

- **“Are all iterables re‑iterable?”**  
  No. Some iterables are effectively **single‑pass** (for example, a file object).  
  Calling `iter(x)` again might give you the same exhausted iterator instead of a new one, depending on how the object is implemented.

- **“Is `for` basically a `while` loop?”**  
  Conceptually yes: it’s a `while` loop that keeps calling `next()` on an iterator and stops when it sees `StopIteration`.

- **“Why do some things print as `<list_iterator object at 0x...>`?”**  
  That’s just the standard representation for iterator objects.  
  It’s Python telling you “this is an iterator (a cursor), not the underlying list itself.”



## Suggested layout blocks you can reuse

- **Concept box: Iterable vs Iterator**

  - *Iterable*: “can produce iterators” (works with `iter(x)`).
  - *Iterator*: “is being advanced” (works with `next(it)` and eventually raises `StopIteration`).

- **Under the hood: What `for` does**

  ```python
  it = iter(obj)
  while True:
      try:
          item = next(it)
      except StopIteration:
          break
      # loop body
  ```

- **Pitfall alert: Iterator exhaustion**

  - Most iterators are **single‑use**.
  - If you loop over an iterator once, it’s usually **empty the second time**.
  - To loop again, recreate the iterator or iterate over the original iterable instead.


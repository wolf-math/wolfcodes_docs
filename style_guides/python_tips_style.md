---
title: Python Tips Style
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Python tips style

Use this guide when writing or revising pages in `docs/python/tips`.

The Python tips section is not a beginner sequence like `docs/python/guides`, and it is not a reference catalog like `docs/python/language_reference`. It sits between them: practical, skimmable, high-value lessons that save readers time, prevent bugs, and reveal parts of Python they may not discover on their own.

Every page in this section should answer some version of:

- What useful Python lesson is being taught here?
- Why does it matter in real code?
- What behavior or tool should the reader remember?
- What mistake or hidden cost should they avoid?
- What is the simplest reliable pattern to use instead?

The goal is not to be exhaustive. The goal is to make the reader more effective.

## Frontmatter

Use the standard frontmatter on every tips page:

```md
---
title: Concept Name
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
```

- `title` should be literal, specific, and easy to scan in the sidebar.
- `sidebar_position` controls ordering within the tips section.
- Keep author, license, and source metadata consistent.
- Do not add extra metadata unless the surrounding section already uses it.

For a tips hub page such as `index.mdx`, use `sidebar_label` only if the section needs it for navigation consistency.

## Core voice

Write like an experienced Python developer giving careful, practical advice to a curious reader.

The tone should be:

- Friendly and confident
- Concrete rather than abstract
- Practical rather than clever
- Clear about tradeoffs
- Focused on behavior the reader will actually encounter

Prefer:

```md
Use `pathlib` when working with file paths. It is easier to read than joining path strings by hand and works across operating systems.
```

Avoid:

```md
One could theoretically leverage object-oriented path abstractions to improve ergonomics.
```

The section should feel approachable, but it should not be chatty. Keep momentum high and explanations tight.

## What belongs in the tips section

Good tip topics usually fit one or more of these categories:

- Code structure and organization
- Python gotchas and surprising behavior
- Standard library gems
- Readability and maintainability habits
- Debugging and reliability techniques
- Performance guidance with clear practical payoff
- Useful language patterns that many readers miss

Examples:

- Mutable default arguments
- `is` vs `==`
- Why `sorted()` and `list.sort()` are different
- Using `enumerate()` instead of manual counters
- Replacing string path manipulation with `pathlib`
- Using `collections.Counter` for frequency counting
- Using `contextlib` for cleanup patterns
- Using `math.isclose()` for float comparison

Topics that do not belong here:

- Broad beginner tutorials that should live in `docs/python/guides`
- Deep internals that belong in `docs/python/advanced_guides`
- Exhaustive API catalogs that belong in `docs/python/language_reference`
- Pure style opinions without practical payoff

## Core principle

Each tip should teach one memorable lesson.

A reader should be able to skim a page, understand the behavior, see the fix or recommended pattern, and walk away with a usable rule of thumb.

Prefer a strong lesson over full coverage. It is better for a tips page to teach five memorable ideas clearly than fifteen ideas shallowly.

## Page types

Most pages in `docs/python/tips` should fit one of these shapes.

### Theme sections

A theme section groups several related tips under one practical topic.

Examples:

- `gotchas/`
- `stdlib_gems/`
- `debugging/`
- `code_structure/`

Use this shape for files within each section:

1. Short opening paragraph defining the theme
2. `## Why this matters` when the value is not immediately obvious
3. One `##` section per major tip area, or one `###` section per tip when the page has a single top-level concept
4. Short examples and recommendations for each tip
5. Optional `## Rules of thumb` or `## Summary` at the end

### Single-focus tip pages

A single-focus tip page centers one concept or trap.

Examples:

- Mutable default arguments
- Late binding in closures
- Shallow vs deep copies

Use this shape:

1. `## What is happening?` or another direct opening heading
2. `## Why this surprises people` or `## Why this matters`
3. A small failing or surprising example
4. `## Prefer this instead` or a similarly direct recommendation section
5. Optional `## Rule of thumb`
6. Optional `## Related reading`

### Standard library spotlight pages

These pages introduce useful modules or tools without becoming full references.

Examples:

- `pathlib`
- `itertools`
- `collections`
- `functools`

Use this shape:

1. `## What is [module/tool]?`
2. `## Why it is useful`
3. A few high-value patterns
4. Notes on when not to use it or when to choose alternatives
5. Short recap or rules of thumb

Do not try to document every function in the module. This section is about practical leverage, not complete coverage.

## Default structure

There is no rigid template, but most tip pages should roughly follow this order:

1. Short definition or framing
2. Real-world value
3. Small example showing the behavior
4. Explanation of what is happening
5. Recommended pattern
6. Rule of thumb or best-practice takeaway
7. Link to deeper guides or reference pages when relevant

Always move from observation to explanation to recommendation.

## Headings

Use sentence-style headings that sound practical and direct.

Good headings:

```md
## Why this matters
## Mutable default arguments
## Prefer this instead
## Using `pathlib`
## When `is` is the right choice
## Rules of thumb
```

Less effective headings:

```md
## Miscellaneous notes
## Additional information
## Example 1
## Syntax variations
```

Use backticks in headings for exact Python syntax, built-ins, module names, operators, methods, and sentinel values:

```md
## `is` vs `==`
## `pathlib`
## `sorted()` vs `sort()`
### `Counter`
### `math.isclose()`
```

Prefer specific task- or behavior-based headings over vague category labels.

## Openings

Most pages should start with a short paragraph that does three things:

- Names the Python behavior or tool
- Explains why it is worth learning
- Signals whether the page is about a best practice, a gotcha, or a hidden gem

Example shape:

````md
`pathlib` is a standard library module for working with file system paths. It usually leads to clearer, safer code than building paths with raw strings, especially when code needs to run across operating systems.
````

For gotcha pages, it is often effective to lead with the surprise:

````md
Mutable default arguments can keep state between function calls. This behavior surprises many Python learners because the default value is created once, not each time the function runs.
````

## Examples

Examples are the center of the tips style. Every important claim should be backed by a small example.

Good examples are:

- Short enough to understand quickly
- Realistic enough to resemble actual Python code
- Focused on one lesson
- Paired with an explanation of the observed behavior
- Followed by a clearer or safer alternative when appropriate

Use language-specific fences:

````md
```python
from pathlib import Path

config_path = Path("config") / "settings.json"
```
````

When output matters, show it:

````md
```python
print([[]] * 3)
```

**Output:**

```text
[[], [], []]
```
````

If the important detail is mutation, aliasing, or returned values, explain it right after the code.

## Teaching surprising behavior

Many tips pages will revolve around behavior that feels counterintuitive. In those cases:

- Show the surprising example early
- State clearly what the reader might expect
- Explain what Python is actually doing
- Give the safer or more explicit pattern

Useful labels:

```md
**What you might expect:** Each call gets a fresh list.

**What actually happens:** The same list object is reused across calls.

**Why:** Default argument values are evaluated once when the function is defined.

**Prefer this instead:** Use `None` as the default and create a new list inside the function.
```

These labels make gotchas easier to scan and remember.

## Recommendations and tradeoffs

A tip should not only describe behavior. It should help the reader choose what to do.

Good recommendation language:

- Prefer `pathlib` for most filesystem work.
- Use `is None` when checking for `None`.
- Reach for `Counter` when the real task is frequency counting.
- Use `math.isclose()` when float equality is conceptually approximate.

When advice has tradeoffs, say so:

- A comprehension is concise, but a loop may be clearer when the logic is complex.
- `deepcopy()` is safer for nested mutable structures, but it can be expensive and should not be used blindly.
- `lru_cache` can be powerful, but it only helps when repeated calls use the same inputs.

Avoid absolute rules unless the rule is truly hard and widely accepted.

## Admonitions

Use admonitions sparingly and only when they improve comprehension.

Recommended usage:

- `:::warning` for bug-prone behavior or patterns likely to cause confusion
- `:::note` for nuance, caveats, or extra context
- `:::tip` only when a short recommendation genuinely benefits from being highlighted

Examples:

```md
:::warning
Avoid using a mutable object such as `[]` or `{}` as a default argument value.
:::
```

```md
:::note
`dict.get()` is useful for missing keys, but it does not distinguish between a missing key and a stored value of `None`.
:::
```

Do not overuse admonitions. If every section is highlighted, none of them stand out.

## Code style inside examples

Python examples in this section should be:

- Modern and idiomatic
- Readable to someone with basic Python knowledge
- Small enough to scan quickly
- Written with simple variable names unless domain-specific names make the example clearer

Prefer names like:

- `items`
- `user`
- `config`
- `path`
- `scores`
- `value`
- `result`

Avoid examples that are:

- Artificially clever
- Too domain-heavy
- Too long to fit on screen comfortably
- Dependent on hidden context

If an example needs setup, keep it minimal and visible in the same code block.

## Scope control

This section should stay selective.

Do not let a tips page turn into:

- A full tutorial
- A complete module reference
- A style-war page
- A long catalog of disconnected trivia

If a topic starts expanding too much, either:

- Split it into multiple focused tips pages
- Move foundational teaching into `docs/python/guides`
- Move exhaustive API coverage into `docs/python/language_reference`

## Cross-linking

Tips pages should often point readers to deeper material.

Cross-link when:

- A tip relies on a broader concept already covered elsewhere
- A standard library gem deserves a fuller guide or reference lookup
- A gotcha connects naturally to an advanced explanation

Examples:

- Link from `is` vs `==` to object identity and mutability material
- Link from `pathlib` tips to standard library modules material
- Link from closure binding tips to function or execution-model guides

Keep the tip page self-contained enough to be useful on its own, but do not duplicate deeper explanations unnecessarily.

## Ending sections

For substantial pages, end with one of these:

- `## Rules of thumb`
- `## Best practices`
- `## Summary`

This closing section should be short and memorable. It should help the reader retain the lesson.

Good ending content:

- Use `is` for `None`, and `==` for value comparisons.
- Prefer `sorted()` when you need a new list and `sort()` when you intentionally want in-place mutation.
- Reach for `pathlib` before manual path-string manipulation.

## Quality bar

A strong Python tips page should:

- Teach something useful quickly
- Include at least one small, runnable example
- Explain the behavior, not just show it
- Offer a practical recommendation
- Leave the reader with a memorable rule of thumb

If a page is accurate but forgettable, it needs stronger examples or clearer takeaways.

If a page is clever but not actionable, it is not ready yet.


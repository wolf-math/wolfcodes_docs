---
title: Master Guide Style
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

# Master guide style

Use this guide as the default style for future educational docs. It combines the best shared patterns from the Python and JavaScript guide styles: friendly explanations, concrete examples, progressive structure, clear mental models, and practical guidance that helps beginners write real code.

Language-specific guides such as `py_guides_style.md` and `js_guides_style.md` should still win when they give a more precise rule for that language. This master guide is the shared baseline.

## Frontmatter

Use the standard frontmatter on every guide:

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

- `title` should be literal, clear, and easy to scan in the sidebar.
- `sidebar_position` controls ordering within the section.
- Keep author, license, and source metadata consistent.
- Do not add extra metadata unless the surrounding docs section already uses it.

## Core principle

Write like a patient teacher explaining one useful idea at a time.

The reader should always know:

- What the concept is
- Why it exists or when they will use it
- What the smallest working example looks like
- What behavior to expect
- What common mistake to avoid
- What pattern or habit to use in real code

Prefer clarity over completeness. A guide should make the learner more capable, not prove that the author knows every edge case.

## Overall structure

Most concept guides should follow this shape:

1. `## What is/are [concept]?`
2. `## Why this matters` when motivation needs its own section
3. Basic syntax, creation, or first practical use
4. Common operations, variations, or related tools
5. Important behavior, mental models, and gotchas
6. Common patterns or real-world workflows
7. Best practices, choosing guidance, or performance notes
8. `## Summary` for substantial guides

This is a pattern, not a rigid template. Shorter pages can skip sections. Longer practical pages can use task-based headings such as `## Reading files`, `## Error handling`, `## Loading states`, or `## Debugging checklist`.

Always move from simple to specific: definition, smallest example, variations, nuance, patterns, then advice.

## Headings

Use sentence-style headings and concrete task names:

```md
## What are lists?
## Creating arrays
## Reading JSON from a file
## Error handling
## Common patterns
## Best practices
## Summary
```

Use backticks in headings for exact syntax, keywords, methods, functions, commands, or API names:

```md
## `if` / `else`
### `append()`
### `Promise.all()`
### The `self` parameter
```

Prefer specific headings over generic template language:

- Use `## Creating dictionaries`, not `## Basic syntax or core form`.
- Use `## Reassignment vs mutation`, not `## Default behavior`.
- Use `## Choosing the right loop`, not `## Variations`.
- Use `### Missing file`, not `### Error case 1`.

Avoid numbered headings unless the whole page is intentionally a checklist or troubleshooting guide.

## Opening definition

Start most guides with `## What is [concept]?` or `## What are [concepts]?`.

The opening should:

- Define the concept in 1-3 plain-language sentences.
- Bold the concept name on first use when it helps the reader identify the term.
- Explain what the concept lets the reader do.
- Include a small example early.
- Name the environment when it matters, such as browser, Node.js, terminal, standard library, or framework.

Example shape:

````md
## What are functions?

**Functions** are reusable blocks of code that perform a specific task. They let you organize code, avoid repetition, and give a clear name to a piece of behavior.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # "Hello, Alice!"
```
````

For broad overview pages, use a short characteristic list:

```md
Functions are:
- **Reusable**: Write once, use many times
- **Named**: Give behavior a meaningful label
- **Parameterized**: Accept inputs to customize behavior
```

## Why this matters

Use `## Why this matters` when the learner needs context before syntax.

This section should explain:

- What problem the concept solves
- Where it appears in real programs
- How it makes code easier to read, maintain, organize, or debug
- How it connects to concepts the reader will learn next

Keep this practical. Avoid history, trivia, and abstract language unless it directly helps the reader understand behavior.

For narrow API pages, you can fold the motivation into the opening paragraph and move straight into usage.

## Examples

Examples are the center of the guide style.

Good examples are:

- Small enough to read at a glance
- Complete enough to run or understand without hidden context
- Focused on one idea
- Written with beginner-readable names such as `name`, `age`, `items`, `scores`, `config`, and `user`
- Followed by a short explanation

Use language-specific code fences:

````md
```python
print("Hello")
```

```javascript
console.log("Hello");
```

```bash
python --version
```

```json
{ "debug": true }
```
````

When a guide needs HTML, SQL, terminal output, or a file tree, use the matching fence.

Show output when behavior matters. Use inline comments for short output:

```javascript
const result = add(5, 3); // 8
```

Use a separate output block or labelled comment for multi-line output:

```python
print("First")
print("Second")
```

**Output:**

```text
First
Second
```

## Explaining behavior

Explain important behavior immediately after the example that demonstrates it.

Useful explanation labels:

```md
**What happens:**
1. The first line runs.
2. The value is stored.
3. The result is printed.
```

```md
**How it works:**
- The file is opened in text mode.
- The parser converts the text into language values.
```

```md
**Important:** This changes the original list.
```

```md
**Rule of thumb:** Use the simpler form unless you need the more advanced behavior.
```

Use these labels to make sequences, gotchas, and recommendations easy to scan.

## Mental models

Teach the mental model, not just the syntax.

A good mental model explains what the runtime, tool, or API is doing in terms the learner can reason about:

- Names refer to values.
- Blocks group code.
- Functions package behavior.
- Collections hold multiple values.
- Errors stop normal execution unless handled.
- Async operations produce values later.
- Files, modules, and packages organize code.
- Browser APIs connect JavaScript to the page.

Give important mental models their own sections:

```md
## Top to bottom execution
## Reassignment vs mutation
## Live vs static collections
## Identity vs equality
## The DOM is dynamic
```

When a behavior is surprising, say so directly and show the safer pattern.

## Tone and voice

Use a clear, warm teaching voice:

- Use direct second person when helpful: "You can...", "You'll use...", "If you try..."
- Use contractions naturally: "don't", "you'll", "it's".
- Prefer plain words over formal phrasing.
- Explain jargon immediately.
- Keep encouragement light and specific.
- Use humor rarely and only when it clarifies or softens a tricky point.

Good:

```md
This is why order matters. You can't use a variable before it's created.
```

Good:

```md
Use this for quick tests and experimentation.
```

Avoid:

```md
This construct provides an abstraction by which execution may be conditionally altered.
```

## Code style

Follow the idioms of the language or tool being taught.

General rules:

- Keep examples short and readable.
- Use meaningful names.
- Use comments to label output, errors, or non-obvious intent.
- Avoid clever one-liners when a simple version teaches better.
- Show realistic values without adding unrelated business logic.
- Do not mix too many new concepts in one example.

Language-specific defaults:

- Python: 4-space indentation, `lower_snake_case`, `print()`, simple built-ins, docstrings when teaching reusable functions.
- JavaScript: 2-space indentation, `const` by default, `let` for reassignment, semicolons, `camelCase`, `console.log()`, `===` / `!==`, modern syntax.
- Browser JavaScript: include the relevant HTML when needed, select elements clearly, check for missing elements when appropriate.
- Command line: use realistic commands and explain arguments or flags when they matter.

When showing code that would error, keep it safe:

```python
# This would cause an error:
# print(unknown_name)  # NameError
```

```javascript
// This would cause an error:
// missingFunction(); // ReferenceError
```

## Comparisons and choices

When there are multiple valid tools, teach the choice.

Use sections like:

```md
## Choosing the right loop
## Lists vs tuples
## Arrays vs objects
## When to use a virtual environment
## When storage is appropriate
```

Write recommendations directly:

```md
- **Use this** when you need a changing collection.
- **Use that** when the values should stay fixed.
- **Avoid this** unless you need the older behavior.
```

Beginners benefit from a clear default. Mention alternatives, but do not leave every choice equally weighted.

## Gotchas and pitfalls

Call out common mistakes close to the relevant concept.

A good pitfall section includes:

- The mistake
- Why it happens
- The safer pattern
- A small example

Example shape:

```javascript
// Bad: assumes element exists
const button = document.querySelector("#save");
button.addEventListener("click", save);

// Good: check first
const button = document.querySelector("#save");
if (button) {
  button.addEventListener("click", save);
}
```

Do not overload a beginner with every edge case. Focus on mistakes they are likely to make soon.

## Callouts

Use Docusaurus callouts for important reminders, warnings, and advanced notes.

```md
:::tip
Use the shorter literal syntax when it is clearer and idiomatic.
:::
```

```md
:::warning
This changes the original object. Make a copy first if you need to keep the original unchanged.
:::
```

```md
:::important
Indentation, braces, or block structure determine which code belongs together.
:::
```

```md
:::note
This is a more advanced feature. You can come back to it later.
:::
```

Use callouts sparingly. Many recommendations work better as normal prose with a bold `Important`, `Recommendation`, or `Rule of thumb` label.

## Lists and tables

Use bullets for characteristics, options, and practical uses:

```md
Arrays are:
- **Ordered**: Items have a specific position
- **Mutable**: Items can be changed
- **Indexed**: Positions start at 0
```

Use numbered lists for sequences:

```md
**What happens:**
1. The program checks the first condition.
2. If it is true, that block runs.
3. If it is false, the next condition is checked.
```

Use tables for compact comparisons:

```md
| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `true` |
| `!=` | Not equal to | `5 != 3` | `true` |
```

Keep tables compact. If a table needs long explanations, use subsections instead.

## Links

Link related concepts when the link helps the learner continue:

- Link prerequisite concepts the reader may need.
- Link follow-up guides for deeper topics.
- Link official docs for standard-library, language-reference, or browser APIs.
- Prefer relative links within the docs when practical.

Do not over-link common words. A few useful links are better than a paragraph full of exits.

## Common patterns

Use `## Common patterns`, `## Common operations`, or a more specific equivalent when the concept has recognizable real-world uses.

Each pattern should have:

- A concrete `###` heading
- One focused example
- A short explanation or recommendation

Good pattern headings:

```md
### Building a list incrementally
### Filtering items
### Early returns
### Reading a file safely
### Reusable fetch function
### Event delegation
```

Patterns should reinforce the current concept. Do not use them to introduce unrelated advanced topics.

## Best practices

Use `## Best practices`, `## Performance considerations`, `## Choosing the right...`, or `## Debugging checklist` when there is concrete guidance.

Write actionable bullets:

```md
- **Use descriptive names**: Names should explain what the value represents.
- **Keep functions focused**: One function should do one clear job.
- **Handle errors where you can respond**: Do not catch errors just to ignore them.
```

Use bad/good examples when the contrast teaches a common mistake:

```javascript
// Bad: unclear
console.log(data);

// Good: descriptive
console.log("Loaded user:", user);
```

Keep best practices tied to the guide. Do not add a generic advice dump at the end.

## Summary

End substantial guides with `## Summary`.

The summary should:

- Restate the core idea
- Reinforce the main mental model
- Mention the safest default or most important caution
- Avoid introducing new information

Use either a short paragraph or compact bullets:

```md
## Summary

- Promises represent values that will be available later.
- Use success handlers for resolved values and error handlers for failures.
- Chain async steps to keep the flow readable.
```

The summary should leave the reader knowing what the concept is for and how to start using it.

## Final checklist

Before publishing a guide, check:

- The opening defines the concept plainly.
- The first example appears early.
- Examples are small, focused, and runnable.
- Output is shown when behavior matters.
- Headings describe real tasks or concepts.
- Gotchas are explained near the relevant code.
- Recommendations give a clear beginner default.
- Links point to useful prerequisites or next steps.
- The ending reinforces the main idea without adding new material.
- Language-specific style rules from the relevant style guide are followed.

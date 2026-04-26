---
title: Debugging Frontend JavaScript
sidebar_position: 14
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What this page is about

Debugging frontend JavaScript is the process of finding out what your code is actually doing, comparing that to what you expected, and narrowing down where the mismatch starts.

This page focuses on practical debugging habits for browser-based JavaScript.

## Why debugging can feel confusing

Frontend bugs often involve several moving parts at once:

- JavaScript logic
- DOM state
- Event timing
- Network requests
- Browser rendering

That is why good debugging usually works best as a step-by-step process rather than random guessing.

## Start with the simplest question

When something breaks, ask:

1. Is there an error message?
2. Is the code running at all?
3. Is the data what I think it is?
4. Is the DOM what I think it is?
5. Is the browser waiting on an event or request?

That basic sequence catches many issues faster than jumping straight into large rewrites.

## Read error messages carefully

Error messages usually tell you both the kind of problem and where to start looking.

### Common error types

```javascript
// ReferenceError
console.log(undefinedVariable);
```

```javascript
// TypeError
const value = null;
value.someMethod();
```

```javascript
// SyntaxError
const value = ;
```

### What these usually mean

- **ReferenceError**: a variable or function name does not exist in this scope
- **TypeError**: a value exists, but it is not the kind of value your code expects
- **SyntaxError**: the browser could not even parse the file

### Use the stack trace

```javascript
function level1() {
  level2();
}

function level2() {
  level3();
}

function level3() {
  console.log(undefinedVariable);
}
```

**Example stack trace:**

```text
ReferenceError: undefinedVariable is not defined
    at level3 (app.js:10:5)
    at level2 (app.js:6:5)
    at level1 (app.js:2:5)
```

The stack trace shows the call path. Start with the first place where your code actually failed, then work outward.

## Use breakpoints, not just logs

Logs are useful, but breakpoints are often faster when you need to inspect the exact state at one moment.

### Basic DevTools flow

1. Open DevTools
2. Go to the Sources tab
3. Open the file you want
4. Click a line number to set a breakpoint
5. Trigger the code path

### What to inspect when paused

- Current variable values
- The call stack
- The scope panel
- Watched expressions

### Basic stepping tools

- **Step over**: run the current line without entering called functions
- **Step into**: go into the function call
- **Step out**: finish the current function and return
- **Resume**: continue until the next breakpoint

## Log strategically

`console.log()` is still one of the fastest debugging tools when used well.

### Use descriptive logs

```javascript
// Hard to interpret later
console.log(data);
```

```javascript
// Easier to understand
console.log("User data:", userData);
console.log("Form validation result:", isValid);
console.log("API response:", response);
```

### Use more than `console.log()`

```javascript
console.warn("Warning message");
console.error("Error message");
console.table(users);
```

```javascript
console.group("User login");
console.log("Username:", username);
console.log("Timestamp:", new Date());
console.groupEnd();
```

### Add temporary logs around transitions

```javascript
function complexFunction(data) {
  console.log("Input:", data);

  const firstStep = processStep1(data);
  console.log("After step1:", firstStep);

  const secondStep = processStep2(firstStep);
  console.log("After step2:", secondStep);

  return secondStep;
}
```

This is often better than logging everywhere at random.

## Debug async code carefully

Async bugs feel confusing because the failure often happens later than the code that started the work.

### `fetch()` and async functions

```javascript
async function fetchUser() {
  const response = await fetch("/api/user");
  const user = await response.json();
  return user.name;
}

fetchUser().then(name => {
  console.log(name.toUpperCase());
});
```

If `name` is not what you expected, the bug might be:

- the request failed
- the response shape is different
- `user.name` is missing
- later code assumed too much

### Set breakpoints inside async code

```javascript
async function processData() {
  const response = await fetch("/api/data");
  const data = await response.json();
  return data;
}
```

Breakpoints after each `await` are often useful because that is where the program picks back up with new data.

### Use `try` / `catch`

```javascript
async function fetchData() {
  try {
    const response = await fetch("/api/data");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Fetch error:", error);
    throw error;
  }
}
```

This gives you a good place to inspect failures directly.

## Common frontend mistakes

### Accessing elements before they exist

```javascript
const button = document.querySelector("button");
console.log(button);
```

If this logs `null`, the issue may be timing, selector accuracy, or missing HTML.

### Forgetting null checks

```javascript
const button = document.querySelector("button");
button.addEventListener("click", handleClick);
```

```javascript
const button = document.querySelector("button");

if (button) {
  button.addEventListener("click", handleClick);
}
```

### Typos and naming mismatches

```javascript
const userName = "Alice";
console.log(usernam);
```

This kind of bug is a strong reason to use a linter.

### Wrong data types

```javascript
const count = "5";
const total = count + 10;
```

```javascript
const count = "5";
const total = Number.parseInt(count, 10) + 10;
```

### Passing a function call instead of a function reference

```javascript
button.addEventListener("click", handleClick());
```

```javascript
button.addEventListener("click", handleClick);
```

### State and DOM are out of sync

If the UI looks wrong, ask whether the bug is in:

- the state update
- the render logic
- the event that should trigger re-rendering

## A practical debugging workflow

### Isolate the problem

Try to narrow the failing area before you fix anything:

```javascript
function processData(data) {
  // const result = step1(data);
  // const result2 = step2(result);
  const result3 = step3(data);
  return result3;
}
```

This is not the final solution, but it helps you locate the first broken step.

### Use `debugger`

```javascript
function buggyFunction() {
  const value = 10;
  debugger;
  return value * 2;
}
```

When DevTools is open, `debugger` pauses execution exactly there.

### Test with known input

```javascript
function myFunction(data) {
  return processData(data);
}
```

Try calling the function with a small, known input in the console. If it fails there too, the bug is easier to reason about.

## Debugging checklist

When something does not work:

1. Check the browser console first
2. Read the exact error message and stack trace
3. Confirm the code path is actually running
4. Inspect the values you are working with
5. Check whether the DOM elements exist
6. Verify events are attached and firing
7. Check the Network tab for failed requests
8. Use breakpoints when logs stop being enough
9. Isolate one failing step at a time
10. Fix the root cause, not just the symptom

## Summary

- Good debugging starts by narrowing the problem, not guessing.
- Error messages, logs, breakpoints, and DevTools each help with different kinds of bugs.
- Many frontend issues come from missing elements, wrong assumptions about data, async timing, or state/DOM mismatch.
- A consistent debugging process is usually more valuable than any single trick.

## Next steps

Once debugging feels clearer, the next step is applying the same kind of discipline to performance work. Continue with [Performance & Best Practices](./performance_best_practices).

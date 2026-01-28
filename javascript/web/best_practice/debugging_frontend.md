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

## Reading error messages

Error messages tell you what went wrong. Learning to read them is the first step to fixing bugs.

### Common error types

```javascript
// ReferenceError - variable doesn't exist
console.log(undefinedVariable);
// ReferenceError: undefinedVariable is not defined

// TypeError - wrong type or method doesn't exist
const x = null;
x.someMethod();
// TypeError: Cannot read property 'someMethod' of null

// SyntaxError - invalid JavaScript
const x = ;
// SyntaxError: Unexpected token ';'
```

### Understanding stack traces

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

**Stack trace:**
```
ReferenceError: undefinedVariable is not defined
    at level3 (app.js:10:5)
    at level2 (app.js:6:5)
    at level1 (app.js:2:5)
```

The stack trace shows the call chain—start from the bottom to trace where the error originated.

## Using breakpoints

**Breakpoints** pause code execution so you can inspect variables and step through code.

### Setting breakpoints in DevTools

1. Open DevTools (F12)
2. Go to Sources tab
3. Find your JavaScript file
4. Click the line number to set a breakpoint
5. When that line executes, code pauses

### Inspecting variables

When paused:
- Hover over variables to see their values
- Check the "Scope" panel to see all variables
- Use the "Watch" panel to monitor specific expressions

### Stepping through code

- **Step Over** (F10) — execute current line, don't go into functions
- **Step Into** (F11) — go into function calls
- **Step Out** (Shift+F11) — finish current function
- **Resume** (F8) — continue execution

## Logging strategically

`console.log` is powerful, but use it strategically:

### Use descriptive messages

```javascript
// Bad: unclear
console.log(x);
console.log(data);

// Good: descriptive
console.log('User data:', userData);
console.log('Form validation result:', isValid);
console.log('API response:', response);
```

### Use console methods

```javascript
// Different log levels
console.log('Info message');
console.warn('Warning message');
console.error('Error message');

// Table view for arrays/objects
console.table(users);

// Group related logs
console.group('User login');
console.log('Username:', username);
console.log('Timestamp:', new Date());
console.groupEnd();
```

### Conditional logging

```javascript
// Only log in development
const DEBUG = true;

if (DEBUG) {
  console.log('Debug info:', data);
}

// Or remove logs in production
// Use a build tool to strip console.log in production
```

## Debugging async code

Async code has unique debugging challenges.

### Async stack traces

```javascript
async function fetchUser() {
  const response = await fetch('/api/user');
  const user = await response.json();
  return user.name;  // Error here
}

fetchUser().then(name => {
  console.log(name.toUpperCase());  // Error: name might be undefined
});
```

**Enable async stack traces** in DevTools:
- Chrome: Settings → Preferences → Console → "Async stack traces"

### Debugging promises

```javascript
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Fetch error:', error);
    // Set breakpoint here to inspect error
    throw error;
  }
}
```

### Using breakpoints with async

You can set breakpoints inside async functions:

```javascript
async function processData() {
  const data = await fetch('/api/data');  // Breakpoint here
  const processed = data.map(/* ... */);  // Or here
  return processed;
}
```

## Common beginner mistakes

### 1. Accessing elements before DOM loads

```javascript
// Error: element doesn't exist yet
const button = document.querySelector('button');  // null!

// Fix: wait for DOM
document.addEventListener('DOMContentLoaded', function() {
  const button = document.querySelector('button');  // Works!
});
```

### 2. Forgetting to check for null

```javascript
// Error: button might be null
const button = document.querySelector('button');
button.addEventListener('click', handler);  // TypeError if null

// Fix: check first
const button = document.querySelector('button');
if (button) {
  button.addEventListener('click', handler);
}
```

### 3. Typos in variable names

```javascript
const userName = 'Alice';
console.log(userName);  // Works
console.log(usernam);   // ReferenceError: usernam is not defined
```

Use a linter to catch these automatically.

### 4. Wrong data types

```javascript
const count = '5';
const total = count + 10;  // '510' (string concatenation, not math!)

// Fix: convert to number
const total = parseInt(count) + 10;  // 15
```

### 5. Scope issues

```javascript
function setupButton() {
  const button = document.querySelector('button');
  button.addEventListener('click', function() {
    // button is accessible here
  });
}
// button is NOT accessible here
```

### 6. Event listener bugs

```javascript
// Wrong: calling function immediately
button.addEventListener('click', handleClick());  // () calls it now!

// Right: pass function reference
button.addEventListener('click', handleClick);  // Pass function
```

## Debugging techniques

### 1. Isolate the problem

```javascript
// Comment out code to find the issue
function processData(data) {
  // const result = step1(data);
  // const result2 = step2(result);
  const result3 = step3(data);  // Test if step3 works alone
  return result3;
}
```

### 2. Add temporary logs

```javascript
function complexFunction(data) {
  console.log('Input:', data);
  const step1 = processStep1(data);
  console.log('After step1:', step1);
  const step2 = processStep2(step1);
  console.log('After step2:', step2);
  return step2;
}
```

### 3. Use the debugger statement

```javascript
function buggyFunction() {
  const x = 10;
  debugger;  // Execution pauses here if DevTools is open
  const y = x * 2;
  return y;
}
```

### 4. Check browser console

Always check the console for errors:
- Red errors — JavaScript errors
- Yellow warnings — potential issues
- Network tab — failed requests

### 5. Test in isolation

```javascript
// Test function in console
function myFunction(data) {
  // Complex logic
}

// Test in console
myFunction(testData);  // See if it works with known input
```

## Debugging checklist

When something doesn't work:

1. Check browser console for errors
2. Read error messages carefully
3. Check if elements exist (use `console.log` or breakpoints)
4. Verify data types are what you expect
5. Add logs to trace execution flow
6. Use breakpoints to inspect state
7. Test in isolation (comment out other code)
8. Check network tab for failed requests
9. Verify event listeners are attached
10. Check if state and DOM are in sync

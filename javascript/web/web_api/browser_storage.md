---
title: Web Storage
sidebar_position: 13
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is web storage?

**Web storage** lets your JavaScript save small amounts of data in the browser. The two main APIs are `localStorage` and `sessionStorage`.

### Smallest working example

```javascript
localStorage.setItem("theme", "dark");

const theme = localStorage.getItem("theme");
console.log(theme); // "dark"
```

## Why this matters

Web storage is useful when your page needs to remember something:

- User preferences like theme or language
- Draft form values
- Small pieces of UI state
- Data that should survive a refresh

## `localStorage`

`localStorage` stores data that stays available after the browser is closed and reopened.

### Basic usage

```javascript
localStorage.setItem("username", "Alice");
localStorage.setItem("theme", "dark");

const username = localStorage.getItem("username");
console.log(username); // "Alice"

localStorage.removeItem("username");
localStorage.clear();
```

### Storing objects

`localStorage` only stores strings, so objects need JSON:

```javascript
const user = {
  name: "Alice",
  email: "alice@example.com",
  preferences: {
    theme: "dark"
  }
};

localStorage.setItem("user", JSON.stringify(user));

const rawUser = localStorage.getItem("user");
if (rawUser) {
  const savedUser = JSON.parse(rawUser);
  console.log(savedUser.name);
}
```

### Checking whether a key exists

```javascript
const username = localStorage.getItem("username");

if (username !== null) {
  console.log("Username:", username);
} else {
  console.log("No username stored");
}
```

## `sessionStorage`

`sessionStorage` uses the same API as `localStorage`, but its data lasts only for the current browser tab session.

```javascript
sessionStorage.setItem("tempData", "value");

const data = sessionStorage.getItem("tempData");
console.log(data);

sessionStorage.removeItem("tempData");
```

## Choosing the right storage

- **Use `localStorage`** when the data should still be there after the browser closes
- **Use `sessionStorage`** when the data should belong only to the current tab session
- **Use plain JavaScript variables** when the data only needs to exist while the page is open
- **Use IndexedDB** when the data is larger, more structured, or more complex than simple key-value storage

:::tip
Rule of thumb: if you only need to store a few strings or small JSON objects, `localStorage` is often enough. If you start storing lots of records or more complex app data, Web Storage is probably the wrong tool.
:::

## When storage is appropriate

Good fits for Web Storage:

- User preferences
- Draft form data
- Small persisted app state
- Shopping cart state for simple apps

Poor fits for Web Storage:

- Large datasets
- Sensitive information like passwords
- Frequently changing high-volume data
- Complex relational or offline-first application data

## Persisting application state

```javascript
function saveState(todos, currentTheme) {
  const state = {
    items: todos.items,
    filter: todos.filter,
    theme: currentTheme
  };

  localStorage.setItem("appState", JSON.stringify(state));
}

function loadState() {
  const saved = localStorage.getItem("appState");
  if (!saved) {
    return null;
  }

  return JSON.parse(saved);
}
```

### Example: save a form draft

```javascript
const form = document.querySelector("#contact-form");

if (form) {
  form.addEventListener("input", () => {
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    localStorage.setItem("formDraft", JSON.stringify(data));
  });

  const draft = localStorage.getItem("formDraft");
  if (draft) {
    const data = JSON.parse(draft);

    Object.keys(data).forEach(key => {
      const input = form.querySelector(`[name="${key}"]`);
      if (input) {
        input.value = data[key];
      }
    });
  }

  form.addEventListener("submit", () => {
    localStorage.removeItem("formDraft");
  });
}
```

## Storage events

The browser can tell other tabs when storage changed:

```javascript
window.addEventListener("storage", event => {
  console.log("Storage changed:", event.key);
  console.log("Old value:", event.oldValue);
  console.log("New value:", event.newValue);
});
```

:::note
The `storage` event fires in other tabs or windows, not in the same tab that made the change.
:::

## Limitations and errors

### Size limits

Web Storage is intentionally small:

- `localStorage` / `sessionStorage` are usually around 5-10 MB per origin
- Limits vary by browser
- Going over the limit throws a `QuotaExceededError`

### Handling storage failures

```javascript
try {
  localStorage.setItem("largeData", largeString);
} catch (error) {
  if (error.name === "QuotaExceededError") {
    console.error("Storage quota exceeded");
  }
}
```

### Checking availability

Some environments or privacy modes may restrict storage:

```javascript
function isStorageAvailable() {
  try {
    localStorage.setItem("test", "test");
    localStorage.removeItem("test");
    return true;
  } catch (error) {
    return false;
  }
}
```

## Best practices

### Wrap storage access in helpers

```javascript
const storage = {
  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (error) {
      console.error("Storage error:", error);
      return false;
    }
  },

  get(key) {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : null;
    } catch (error) {
      console.error("Storage error:", error);
      return null;
    }
  },

  remove(key) {
    localStorage.removeItem(key);
  }
};
```

### Do not store sensitive data

```javascript
// Bad
localStorage.setItem("password", password);
```

```javascript
// Better
localStorage.setItem("username", username);
```

### Expect stale or missing data

```javascript
const settings = storage.get("settings");

if (settings) {
  applySettings(settings);
} else {
  applyDefaultSettings();
}
```

## Summary

- Web Storage gives you simple browser-side key-value storage.
- Use `localStorage` for data that should survive browser restarts and `sessionStorage` for tab-scoped data.
- Store objects as JSON strings and parse them when reading.
- Web Storage is best for small, simple data, not large or sensitive information.

## Next up

- [Fetch API](./networking)
- [Application State in the Browser](../state/application_state)
- [Forms and User Input](../events/forms_input)

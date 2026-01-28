---
title: Browser Storage
sidebar_position: 11
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Localstorage

`localStorage` stores data in the browser that persists even after the browser is closed.

### Basic usage

```javascript
// Save data
localStorage.setItem('username', 'Alice');
localStorage.setItem('theme', 'dark');

// Read data
const username = localStorage.getItem('username');
console.log(username);  // "Alice"

// Remove data
localStorage.removeItem('username');

// Clear all
localStorage.clear();
```

### Storing objects

`localStorage` only stores strings. Store objects as JSON:

```javascript
const user = {
  name: 'Alice',
  email: 'alice@example.com',
  preferences: { theme: 'dark' }
};

// Save (convert to JSON)
localStorage.setItem('user', JSON.stringify(user));

// Read (parse JSON)
const savedUser = JSON.parse(localStorage.getItem('user'));
console.log(savedUser.name);  // "Alice"
```

### Checking if key exists

```javascript
const username = localStorage.getItem('username');
if (username) {
  console.log('Username:', username);
} else {
  console.log('No username stored');
}

// Or check if null
if (localStorage.getItem('username') !== null) {
  // Key exists
}
```

## Sessionstorage

`sessionStorage` works like `localStorage`, but data only lasts for the browser tab session (cleared when tab closes).

### Usage

```javascript
// Same API as localStorage
sessionStorage.setItem('tempData', 'value');
const data = sessionStorage.getItem('tempData');
sessionStorage.removeItem('tempData');
```

### When to use sessionStorage

- Temporary data that shouldn't persist
- Data specific to one tab/session
- Sensitive data (automatically cleared when tab closes)

## When storage is appropriate

### Good use cases

✅ **User preferences** — theme, language, settings  
✅ **Form drafts** — save progress before submission  
✅ **Shopping cart** — persist cart between sessions  
✅ **Authentication tokens** — remember login (though be careful with security)  
✅ **Application state** — save UI state (scroll position, filters)

### Not appropriate

❌ **Large data** — localStorage has size limits (~5-10MB)  
❌ **Sensitive data** — passwords, credit cards (use secure server storage)  
❌ **Temporary data** — use variables or sessionStorage  
❌ **Frequently changing data** — can be slow

## Persisting application state

Save and restore application state:

```javascript
// Save state
function saveState() {
  const state = {
    todos: todos.items,
    filter: todos.filter,
    theme: currentTheme
  };
  localStorage.setItem('appState', JSON.stringify(state));
}

// Load state
function loadState() {
  const saved = localStorage.getItem('appState');
  if (saved) {
    const state = JSON.parse(saved);
    todos.items = state.todos || [];
    todos.filter = state.filter || 'all';
    currentTheme = state.theme || 'light';
    renderTodos();
  }
}

// Save on every change
function addTodo(text) {
  todos.items.push({ id: Date.now(), text, completed: false });
  renderTodos();
  saveState();  // Persist to localStorage
}

// Load on page load
window.addEventListener('DOMContentLoaded', loadState);
```

### Example: Save form drafts

```javascript
const form = document.querySelector('#contact-form');

// Save form data as user types
form.addEventListener('input', function() {
  const formData = new FormData(form);
  const data = Object.fromEntries(formData);
  localStorage.setItem('formDraft', JSON.stringify(data));
});

// Load saved draft
const draft = localStorage.getItem('formDraft');
if (draft) {
  const data = JSON.parse(draft);
  Object.keys(data).forEach(key => {
    const input = form.querySelector(`[name="${key}"]`);
    if (input) input.value = data[key];
  });
}

// Clear draft on submit
form.addEventListener('submit', function() {
  localStorage.removeItem('formDraft');
});
```

## Storage events

Listen for storage changes (useful for syncing between tabs):

```javascript
window.addEventListener('storage', function(e) {
  console.log('Storage changed:', e.key);
  console.log('Old value:', e.oldValue);
  console.log('New value:', e.newValue);
  
  // Update UI if key changed
  if (e.key === 'theme') {
    updateTheme(e.newValue);
  }
});
```

**Note:** Storage events only fire in **other tabs/windows**, not the one that made the change.

## Storage limitations

### Size limits

- **localStorage/sessionStorage**: ~5-10MB per origin (varies by browser)
- **Exceeding limit**: throws `QuotaExceededError`

### Handling quota errors

```javascript
try {
  localStorage.setItem('largeData', largeString);
} catch (e) {
  if (e.name === 'QuotaExceededError') {
    console.error('Storage quota exceeded');
    // Handle: clear old data, compress, etc.
  }
}
```

### Privacy mode

Some browsers disable localStorage in private/incognito mode:

```javascript
function isStorageAvailable() {
  try {
    localStorage.setItem('test', 'test');
    localStorage.removeItem('test');
    return true;
  } catch (e) {
    return false;
  }
}

if (isStorageAvailable()) {
  // Use localStorage
} else {
  // Fallback to sessionStorage or memory
}
```

## Best practices

### 1. Use `try`/`catch`

```javascript
try {
  localStorage.setItem('key', 'value');
} catch (e) {
  console.error('Failed to save:', e);
}
```

### 2. Check before reading

```javascript
const data = localStorage.getItem('key');
if (data) {
  const parsed = JSON.parse(data);
  // Use parsed data
}
```

### 3. Don't store sensitive data

```javascript
// Bad: storing passwords
localStorage.setItem('password', password);  // DON'T DO THIS!

// Good: store only what's necessary
localStorage.setItem('username', username);
// Password handled by server
```

### 4. Clean up old data

```javascript
function cleanupOldData() {
  const keys = Object.keys(localStorage);
  keys.forEach(key => {
    const data = localStorage.getItem(key);
    // Check if data is old/stale
    if (isStale(data)) {
      localStorage.removeItem(key);
    }
  });
}
```

### 5. Use helper functions

```javascript
const storage = {
  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (e) {
      console.error('Storage error:', e);
      return false;
    }
  },
  
  get(key) {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : null;
    } catch (e) {
      console.error('Storage error:', e);
      return null;
    }
  },
  
  remove(key) {
    localStorage.removeItem(key);
  },
  
  clear() {
    localStorage.clear();
  }
};

// Usage
storage.set('user', { name: 'Alice' });
const user = storage.get('user');
```

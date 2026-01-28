---
title: Structuring Frontend JavaScript
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

## Organizing files

As your project grows, organizing code into files becomes essential.

### Basic structure

```
my-app/
  ├── index.html
  ├── css/
  │   └── styles.css
  ├── js/
  │   ├── app.js
  │   ├── utils.js
  │   └── components/
  │       ├── todo.js
  │       └── user.js
  └── assets/
      └── images/
```

### Separation of concerns

```
js/
  ├── app.js          # Main application logic
  ├── state.js        # State management
  ├── dom.js          # DOM manipulation
  ├── api.js          # API calls
  └── utils.js        # Utility functions
```

## Using es modules in the browser

ES modules let you split code across files and import what you need.

### Setting up modules

In your HTML:

```html
<script type="module" src="js/app.js"></script>
```

### Module structure

```javascript
// utils.js
export function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(amount);
}

export function debounce(func, delay) {
  let timeoutId;
  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
}

// app.js
import { formatCurrency, debounce } from './utils.js';

const price = formatCurrency(100);
```

### Organizing by feature

```
js/
  ├── app.js
  ├── todo/
  │   ├── todo.js
  │   ├── todo-state.js
  │   └── todo-ui.js
  ├── user/
  │   ├── user.js
  │   └── user-api.js
  └── utils/
      └── helpers.js
```

## Separating concerns

Keep different responsibilities separate:

### Logic vs DOM updates

```javascript
// state.js - manages data
export const todos = {
  items: [],
  add(text) {
    this.items.push({ id: Date.now(), text, completed: false });
  },
  toggle(id) {
    const todo = this.items.find(t => t.id === id);
    if (todo) todo.completed = !todo.completed;
  }
};

// ui.js - handles DOM updates
import { todos } from './state.js';

export function renderTodos() {
  const list = document.querySelector('#todo-list');
  list.innerHTML = '';
  todos.items.forEach(todo => {
    const li = document.createElement('li');
    li.textContent = todo.text;
    if (todo.completed) li.classList.add('completed');
    list.appendChild(li);
  });
}

// app.js - wires everything together
import { todos } from './state.js';
import { renderTodos } from './ui.js';

document.querySelector('#add-btn').addEventListener('click', () => {
  todos.add('New todo');
  renderTodos();
});
```

### Events vs logic

```javascript
// events.js - event handlers
import { todos } from './state.js';
import { renderTodos } from './ui.js';

export function setupEventListeners() {
  document.querySelector('#add-btn').addEventListener('click', () => {
    const input = document.querySelector('#todo-input');
    todos.add(input.value);
    input.value = '';
    renderTodos();
  });
  
  document.querySelector('#todo-list').addEventListener('click', (e) => {
    if (e.target.classList.contains('delete')) {
      const id = parseInt(e.target.dataset.id);
      todos.remove(id);
      renderTodos();
    }
  });
}

// app.js - initialization
import { setupEventListeners } from './events.js';
import { renderTodos } from './ui.js';

setupEventListeners();
renderTodos();
```

## Progressive enhancement mindset

**Progressive enhancement** means building a functional base that works everywhere, then adding JavaScript enhancements.

### HTML first

```html
<!-- Works without JavaScript -->
<form action="/api/submit" method="POST">
  <input type="text" name="username" required />
  <button type="submit">Submit</button>
</form>
```

### Enhance with JavaScript

```javascript
// Enhance form with JavaScript
const form = document.querySelector('form');

form.addEventListener('submit', function(e) {
  e.preventDefault();
  
  // Enhanced behavior: show loading, handle errors, etc.
  submitFormWithFeedback(this);
});
```

**Benefits:**
- Works even if JavaScript fails
- Better for SEO
- Faster initial load
- More accessible

## Common patterns

### App initialization pattern

```javascript
// app.js
class App {
  constructor() {
    this.state = {};
    this.components = {};
  }
  
  init() {
    this.loadState();
    this.initComponents();
    this.setupEvents();
    this.render();
  }
  
  loadState() {
    // Load from localStorage, API, etc.
  }
  
  initComponents() {
    // Initialize components
  }
  
  setupEvents() {
    // Setup event listeners
  }
  
  render() {
    // Initial render
  }
}

// Start app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  const app = new App();
  app.init();
});
```

### Component pattern

```javascript
// components/todo-list.js
export class TodoList {
  constructor(container, todos) {
    this.container = container;
    this.todos = todos;
  }
  
  render() {
    this.container.innerHTML = '';
    this.todos.forEach(todo => {
      const item = this.createTodoItem(todo);
      this.container.appendChild(item);
    });
  }
  
  createTodoItem(todo) {
    const li = document.createElement('li');
    li.textContent = todo.text;
    if (todo.completed) li.classList.add('completed');
    return li;
  }
}

// app.js
import { TodoList } from './components/todo-list.js';

const todoList = new TodoList(
  document.querySelector('#todo-list'),
  todos.items
);
todoList.render();
```

### Service pattern

```javascript
// services/api.js
export class ApiService {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }
  
  async get(endpoint) {
    const response = await fetch(`${this.baseUrl}${endpoint}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  }
  
  async post(endpoint, data) {
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  }
}

// app.js
import { ApiService } from './services/api.js';

const api = new ApiService('https://api.example.com');
const users = await api.get('/users');
```

## Best practices

### 1. One responsibility per file

```javascript
// Good: focused file
// utils/formatting.js
export function formatCurrency() { }
export function formatDate() { }

// Bad: everything in one file
// utils.js
export function formatCurrency() { }
export function formatDate() { }
export function apiCall() { }
export function domManipulation() { }
```

### 2. Use descriptive file names

```
// Good
todo-manager.js
user-service.js
form-validator.js

// Bad
stuff.js
helpers.js
utils.js
```

### 3. Export what's needed

```javascript
// Good: explicit exports
export function publicFunction() { }
export const publicConstant = 123;

function privateFunction() { }  // Not exported

// Bad: everything exported
export function everything() { }
export function isPublic() { }
```

### 4. Keep dependencies clear

```javascript
// Good: clear dependencies
import { formatCurrency } from './utils/formatting.js';
import { ApiService } from './services/api.js';

// Bad: unclear where things come from
import * from './utils.js';
```

### 5. Document structure

```javascript
/**
 * Manages todo items state and operations
 * @module todo/state
 */

/**
 * Adds a new todo item
 * @param {string} text - Todo text
 */
export function addTodo(text) {
  // ...
}
```

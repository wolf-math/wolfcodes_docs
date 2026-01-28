---
title: Application State in the Browser
sidebar_position: 8
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What "state" means

**State** is the data that represents your application's current condition. It's what your app "remembers" and what changes as users interact with it.

Examples of state:
- User's shopping cart items
- Current page number in a list
- Whether a modal is open or closed
- Form input values before submission
- User authentication status

## State vs DOM

This is a crucial distinction:

- **State** — data in JavaScript (variables, objects, arrays)
- **DOM** — the HTML elements users see

**The DOM should reflect the state, not be the source of truth.**

### The wrong way

```javascript
// Bad: reading from DOM
function getCartItems() {
  const items = [];
  document.querySelectorAll('.cart-item').forEach(item => {
    items.push(item.textContent);
  });
  return items;
}
```

The problem: If you need to know what's in the cart, you're reading from the DOM. This is fragile and error-prone.

### The right way

```javascript
// Good: state is source of truth
let cartState = [];

function addToCart(item) {
  cartState.push(item);  // Update state
  updateCartUI();        // Then update DOM
}

function updateCartUI() {
  const cartList = document.querySelector('#cart');
  cartList.innerHTML = '';
  cartState.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    cartList.appendChild(li);
  });
}
```

**State drives the DOM, not the other way around.**

## Keeping state in JavaScript

Store state in JavaScript variables:

```javascript
// Simple state
let count = 0;
let isModalOpen = false;
let currentUser = null;

// Complex state (object)
const appState = {
  user: {
    name: 'Alice',
    isLoggedIn: true
  },
  cart: {
    items: [],
    total: 0
  },
  settings: {
    theme: 'light',
    language: 'en'
  }
};
```

### State object pattern

Organize related state in objects:

```javascript
const state = {
  todos: [],
  filter: 'all',  // 'all', 'active', 'completed'
  inputValue: ''
};

// Update state
function addTodo(text) {
  state.todos.push({
    id: Date.now(),
    text: text,
    completed: false
  });
}

function toggleTodo(id) {
  const todo = state.todos.find(t => t.id === id);
  if (todo) {
    todo.completed = !todo.completed;
  }
}
```

## Syncing state to the DOM

When state changes, update the DOM to reflect it:

```javascript
// State
let count = 0;

// Update state
function increment() {
  count++;
  render();  // Update DOM after state change
}

// Render function updates DOM based on state
function render() {
  document.querySelector('#counter').textContent = count;
  
  // Update button state based on count
  const button = document.querySelector('#increment-btn');
  button.disabled = count >= 10;
}
```

### Single source of truth

Always update state first, then render:

```javascript
function addItem(name) {
  // 1. Update state
  items.push(name);
  
  // 2. Update DOM to match state
  renderItems();
}

function renderItems() {
  const list = document.querySelector('#items');
  list.innerHTML = '';
  items.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    list.appendChild(li);
  });
}
```

## Common state bugs

### Bug 1: State and DOM out of sync

```javascript
// Bad: directly manipulating DOM without updating state
function addItem() {
  const li = document.createElement('li');
  li.textContent = 'New item';
  document.querySelector('#list').appendChild(li);
  // State not updated! Now state and DOM don't match
}

// Good: update state, then render
function addItem() {
  items.push('New item');  // Update state
  renderItems();           // Update DOM
}
```

### Bug 2: Reading from DOM instead of state

```javascript
// Bad: reading from DOM
function getItemCount() {
  return document.querySelectorAll('.item').length;  // What if DOM is wrong?
}

// Good: read from state
function getItemCount() {
  return items.length;  // Always accurate
}
```

### Bug 3: Multiple sources of truth

```javascript
// Bad: state scattered everywhere
let count1 = 0;  // One counter
let count2 = 0;  // Another counter
// Which one is correct?

// Good: single source of truth
const state = {
  counter: 0
};
```

### Bug 4: Forgetting to re-render

```javascript
// Bad: state updated but DOM not refreshed
function updateCount() {
  count = 10;  // State updated
  // DOM still shows old value!
}

// Good: always render after state change
function updateCount() {
  count = 10;
  render();  // Update DOM
}
```

## State management patterns

### Pattern 1: Simple state + render

For small apps:

```javascript
let state = {
  todos: [],
  filter: 'all'
};

function render() {
  // Clear and rebuild DOM based on state
  const todos = state.filter === 'all' 
    ? state.todos 
    : state.todos.filter(t => 
        state.filter === 'active' ? !t.completed : t.completed
      );
  
  const list = document.querySelector('#todo-list');
  list.innerHTML = '';
  todos.forEach(todo => {
    const li = document.createElement('li');
    li.textContent = todo.text;
    if (todo.completed) li.classList.add('completed');
    list.appendChild(li);
  });
}

// All state changes trigger render
function addTodo(text) {
  state.todos.push({ id: Date.now(), text, completed: false });
  render();
}

function toggleTodo(id) {
  const todo = state.todos.find(t => t.id === id);
  if (todo) {
    todo.completed = !todo.completed;
    render();
  }
}
```

### Pattern 2: Event-driven updates

Separate concerns:

```javascript
// State
const app = {
  state: {
    count: 0
  },
  
  // Methods that update state
  increment() {
    this.state.count++;
    this.render();
  },
  
  decrement() {
    this.state.count--;
    this.render();
  },
  
  // Render method
  render() {
    document.querySelector('#count').textContent = this.state.count;
  }
};

// Event listeners call app methods
document.querySelector('#increment').addEventListener('click', () => {
  app.increment();
});
```

## Example: todo app state

Here's how state works in a complete todo app:

```javascript
// State
const todos = {
  items: [],
  nextId: 1
};

// Add todo
function addTodo(text) {
  todos.items.push({
    id: todos.nextId++,
    text: text,
    completed: false
  });
  renderTodos();
}

// Toggle todo
function toggleTodo(id) {
  const todo = todos.items.find(t => t.id === id);
  if (todo) {
    todo.completed = !todo.completed;
    renderTodos();
  }
}

// Delete todo
function deleteTodo(id) {
  todos.items = todos.items.filter(t => t.id !== id);
  renderTodos();
}

// Render todos based on state
function renderTodos() {
  const list = document.querySelector('#todo-list');
  list.innerHTML = '';
  
  todos.items.forEach(todo => {
    const li = document.createElement('li');
    li.innerHTML = `
      <input type="checkbox" ${todo.completed ? 'checked' : ''} 
             onchange="toggleTodo(${todo.id})" />
      <span class="${todo.completed ? 'completed' : ''}">${todo.text}</span>
      <button onclick="deleteTodo(${todo.id})">Delete</button>
    `;
    list.appendChild(li);
  });
  
  // Update count
  const count = todos.items.filter(t => !t.completed).length;
  document.querySelector('#count').textContent = 
    `${count} item${count !== 1 ? 's' : ''} remaining`;
}
```

**Key principle:** State is the source of truth. DOM reflects state.

## When to use external state management

For simple apps, JavaScript variables are enough. For complex apps, consider:

- **LocalStorage** — persist state across page refreshes (covered in [browser storage guide](../browser_api/browser_storage))
- **State management libraries** — Redux, Zustand (beyond this guide's scope)
- **Frameworks** — React, Vue (they manage state automatically)

But understanding how to manage state in vanilla JavaScript is essential before using these tools.

---
title: Putting It Together
sidebar_position: 15
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Congratulations!

You've learned the fundamentals of JavaScript! This guide shows you how to combine everything you've learned to write real JavaScript programs.

## Reading real JavaScript code

Let's look at a complete example that combines multiple concepts:

```javascript
// userService.js
export class UserService {
  constructor(apiUrl) {
    this.apiUrl = apiUrl;
    this.users = [];
  }

  async fetchUsers() {
    try {
      const response = await fetch(`${this.apiUrl}/users`);
      const data = await response.json();
      this.users = data;
      return this.users;
    } catch (error) {
      console.error("Failed to fetch users:", error);
      throw error;
    }
  }

  findUserById(id) {
    return this.users.find(user => user.id === id);
  }

  getActiveUsers() {
    return this.users.filter(user => user.isActive);
  }
}

// main.js
import { UserService } from './userService.js';

async function main() {
  const userService = new UserService("https://api.example.com");
  
  try {
    const users = await userService.fetchUsers();
    console.log(`Loaded ${users.length} users`);
    
    const activeUsers = userService.getActiveUsers();
    console.log(`Found ${activeUsers.length} active users`);
    
    const user = userService.findUserById(1);
    if (user) {
      console.log(`User: ${user.name}`);
    }
  } catch (error) {
    console.error("Error in main:", error);
  }
}

main();
```

**What's happening here?**

1. **Classes** — `UserService` is a class with methods and instance data
2. **Modules** — code split across files with `export`/`import`
3. **Async/await** — handling asynchronous API calls
4. **Arrays** — using `find()` and `filter()` methods
5. **Error handling** — `try/catch` blocks
6. **Functions** — `main()` function to organize code

This is what real JavaScript code looks like—combining many concepts together.

## Combining functions, objects, and async

Here's another example showing how different concepts work together:

```javascript
// utils.js
export function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(amount);
}

export function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// cart.js
import { formatCurrency, calculateTotal } from './utils.js';

export class ShoppingCart {
  constructor() {
    this.items = [];
  }

  addItem(item) {
    this.items.push(item);
  }

  removeItem(itemId) {
    this.items = this.items.filter(item => item.id !== itemId);
  }

  getTotal() {
    return calculateTotal(this.items);
  }

  getFormattedTotal() {
    return formatCurrency(this.getTotal());
  }

  async checkout() {
    try {
      const total = this.getTotal();
      const response = await fetch('/api/checkout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          items: this.items,
          total: total
        })
      });
      
      if (!response.ok) {
        throw new Error('Checkout failed');
      }
      
      const result = await response.json();
      this.items = []; // Clear cart
      return result;
    } catch (error) {
      console.error('Checkout error:', error);
      throw error;
    }
  }
}

// main.js
import { ShoppingCart } from './cart.js';

const cart = new ShoppingCart();
cart.addItem({ id: 1, name: 'Laptop', price: 999.99 });
cart.addItem({ id: 2, name: 'Mouse', price: 29.99 });

console.log(`Total: ${cart.getFormattedTotal()}`);

cart.checkout()
  .then(result => {
    console.log('Order placed:', result);
  })
  .catch(error => {
    console.error('Failed to checkout:', error);
  });
```

**Key concepts demonstrated:**

- **Functions** — `formatCurrency`, `calculateTotal` as utility functions
- **Objects/Classes** — `ShoppingCart` class with state and methods
- **Arrays** — `push`, `filter`, `reduce` methods
- **Modules** — organized code across files
- **Async/await** — handling checkout API call
- **Error handling** — try/catch and promise rejection handling

## Writing small scripts confidently

You can now write scripts to solve real problems:

### Example: Data processing script

```javascript
// processData.js
const rawData = [
  { name: "Alice", age: 30, active: true },
  { name: "Bob", age: 25, active: false },
  { name: "Charlie", age: 35, active: true }
];

function processUsers(users) {
  // Filter active users
  const activeUsers = users.filter(user => user.active);
  
  // Calculate average age
  const totalAge = activeUsers.reduce((sum, user) => sum + user.age, 0);
  const avgAge = totalAge / activeUsers.length;
  
  // Format results
  return {
    activeCount: activeUsers.length,
    averageAge: Math.round(avgAge),
    activeUsers: activeUsers.map(user => user.name)
  };
}

const result = processUsers(rawData);
console.log(result);
// { activeCount: 2, averageAge: 33, activeUsers: ['Alice', 'Charlie'] }
```

### Example: Configuration management

```javascript
// config.js
class Config {
  constructor() {
    this.settings = {
      apiUrl: process.env.API_URL || 'https://api.example.com',
      timeout: 5000,
      retries: 3
    };
  }

  get(key) {
    return this.settings[key];
  }

  set(key, value) {
    this.settings[key] = value;
  }

  validate() {
    const required = ['apiUrl'];
    const missing = required.filter(key => !this.settings[key]);
    
    if (missing.length > 0) {
      throw new Error(`Missing required settings: ${missing.join(', ')}`);
    }
    
    return true;
  }
}

const config = new Config();
config.validate();
console.log(config.get('apiUrl'));
```

## What to learn next

Now that you understand core JavaScript, here's what to explore next:

### Web Development (DOM & Browser APIs)

JavaScript in the browser has access to powerful APIs:

- **DOM manipulation** — changing HTML elements, handling events
- **Fetch API** — making HTTP requests (you've seen this, but there's more to learn)
- **Local Storage** — storing data in the browser
- **Web APIs** — Geolocation, Canvas, WebSockets, and more

### Node.js

JavaScript on the server with Node.js:

- **File system** — reading/writing files
- **HTTP servers** — building web servers
- **Streams** — handling large amounts of data efficiently
- **npm** — package management and the JavaScript ecosystem

### Frameworks and libraries

Modern JavaScript development often uses frameworks:

- **React** — building user interfaces
- **Vue** — another popular UI framework
- **Express** — web server framework for Node.js
- **TypeScript** — JavaScript with static typing

**Note:** These are built on JavaScript, so your foundation is solid. Learning them will be much easier now.

### Advanced JavaScript topics

Once you're comfortable, explore:

- **Closures and advanced scope** — deeper understanding
- **Prototypes** — JavaScript's inheritance system under the hood
- **Event loop** — how JavaScript handles async operations
- **Performance optimization** — making your code faster
- **Testing** — writing tests for your JavaScript code

## Tips for continued learning

1. **Write code regularly** — practice is essential
2. **Read other people's code** — see how others solve problems
3. **Build projects** — apply what you've learned
4. **Use documentation** — MDN Web Docs is your friend
5. **Don't try to learn everything at once** — focus on one topic at a time
6. **Ask questions** — the JavaScript community is welcoming

## Final thoughts

You've learned:

- ✅ Variables, types, and operators
- ✅ Strings, arrays, and objects
- ✅ Control flow (conditionals and loops)
- ✅ Functions and scope
- ✅ Error handling
- ✅ Modules and code organization
- ✅ Object-oriented programming
- ✅ Asynchronous programming

This is a **solid foundation**. JavaScript is a large language with many features, but you now understand the core concepts that make everything else possible.

The best way to continue learning is to **build things**. Start small, write code, make mistakes, and learn from them. Every expert was once a beginner.

Good luck on your JavaScript journey! 🚀

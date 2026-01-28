---
title: Networking
sidebar_position: 10
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## The `fetch` API

The **Fetch API** is the modern way to make HTTP requests in the browser. It uses [promises](/docs/javascript/guides/async/promises), making it clean and easy to work with.

```javascript
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
```

## Making get requests

The simplest use of `fetch` is getting data:

```javascript
fetch('https://api.example.com/users')
  .then(response => response.json())
  .then(users => {
    console.log(users);
    // Display users in UI
  });
```

### Handling the response

The `fetch` promise resolves with a `Response` object:

```javascript
fetch('https://api.example.com/data')
  .then(response => {
    console.log(response.status);    // 200, 404, etc.
    console.log(response.ok);        // true if status 200-299
    console.log(response.headers);   // Response headers
    
    return response.json();  // Parse as JSON
  })
  .then(data => {
    console.log(data);
  });
```

### Checking for errors

`fetch` only rejects on network errors, not HTTP errors:

```javascript
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

## Handling JSON

Most APIs return JSON. Parse it with `.json()`:

```javascript
fetch('https://api.example.com/users')
  .then(response => response.json())  // Parse JSON
  .then(data => {
    // data is a JavaScript object
    data.forEach(user => {
      console.log(user.name);
    });
  });
```

### Other response types

```javascript
// Text
fetch('/api/data.txt')
  .then(response => response.text())
  .then(text => console.log(text));

// Blob (for images, files)
fetch('/api/image.jpg')
  .then(response => response.blob())
  .then(blob => {
    const imageUrl = URL.createObjectURL(blob);
    img.src = imageUrl;
  });
```

## Error handling

Always handle errors:

```javascript
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    // Handle success
    displayData(data);
  })
  .catch(error => {
    // Handle errors
    console.error('Fetch failed:', error);
    showError('Failed to load data');
  });
```

### Using async/await

`fetch` works great with [async/await](/docs/javascript/guides/async/async_await):

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    
    const data = await response.json();
    displayData(data);
  } catch (error) {
    console.error('Error:', error);
    showError('Failed to load data');
  }
}
```

## Loading states

Show loading indicators while fetching:

```javascript
async function loadUsers() {
  const loadingDiv = document.querySelector('#loading');
  const errorDiv = document.querySelector('#error');
  const usersDiv = document.querySelector('#users');
  
  // Show loading
  loadingDiv.style.display = 'block';
  errorDiv.style.display = 'none';
  usersDiv.innerHTML = '';
  
  try {
    const response = await fetch('/api/users');
    if (!response.ok) throw new Error('Failed to load');
    
    const users = await response.json();
    
    // Hide loading, show data
    loadingDiv.style.display = 'none';
    displayUsers(users);
  } catch (error) {
    // Hide loading, show error
    loadingDiv.style.display = 'none';
    errorDiv.style.display = 'block';
    errorDiv.textContent = 'Failed to load users';
  }
}
```

## Post requests

Send data to the server:

```javascript
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'Alice',
    email: 'alice@example.com'
  })
})
  .then(response => response.json())
  .then(data => {
    console.log('User created:', data);
  });
```

### Sending form data

Learn more about [form handling](/docs/javascript/web/events/forms_input) in the events guide.

```javascript
const form = document.querySelector('form');

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  
  const formData = new FormData(form);
  
  const response = await fetch('/api/submit', {
    method: 'POST',
    body: formData  // FormData works directly
  });
  
  const result = await response.json();
  console.log('Submitted:', result);
});
```

## Other HTTP methods

```javascript
// PUT - update
fetch('/api/users/123', {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Bob' })
});

// DELETE
fetch('/api/users/123', {
  method: 'DELETE'
});

// PATCH - partial update
fetch('/api/users/123', {
  method: 'PATCH',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Charlie' })
});
```

## Basic security considerations

### CORS (Cross-Origin Resource Sharing)

Browsers block requests to different origins (different domain, port, or protocol) unless the server allows it:

```javascript
// This will fail if api.example.com doesn't allow CORS
fetch('https://api.example.com/data')
  .catch(error => {
    console.error('CORS error:', error);
  });
```

**Solutions:**
- Server must send CORS headers
- Use a proxy server
- Make requests to the same origin

### Same-origin policy

Requests to the same origin work without CORS:

```javascript
// Same origin - works fine
fetch('/api/data')  // Same domain, protocol, port
  .then(response => response.json());
```

### Avoiding XSS

Never trust data from APIs without validation:

```javascript
// Dangerous: directly inserting API data
fetch('/api/comments')
  .then(response => response.json())
  .then(comments => {
    comments.forEach(comment => {
      div.innerHTML += `<p>${comment.text}</p>`;  // XSS risk!
    });
  });

// Safe: use textContent
fetch('/api/comments')
  .then(response => response.json())
  .then(comments => {
    comments.forEach(comment => {
      const p = document.createElement('p');
      p.textContent = comment.text;  // Safe
      div.appendChild(p);
    });
  });
```

## Common patterns

### Reusable fetch function

```javascript
async function apiRequest(url, options = {}) {
  try {
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      }
    });
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API request failed:', error);
    throw error;
  }
}

// Usage
const users = await apiRequest('/api/users');
const user = await apiRequest('/api/users/123', {
  method: 'PUT',
  body: JSON.stringify({ name: 'Alice' })
});
```

### Handling multiple requests

```javascript
// Sequential
const user = await fetch('/api/user/123').then(r => r.json());
const posts = await fetch('/api/user/123/posts').then(r => r.json());

// Parallel (faster)
const [user, posts] = await Promise.all([
  fetch('/api/user/123').then(r => r.json()),
  fetch('/api/user/123/posts').then(r => r.json())
]);
```

Learn more about [`Promise.all()`](/docs/javascript/guides/async/promises#promiseall--wait-for-all-promises) in the promises guide.
```

### Retry logic

```javascript
async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const response = await fetch(url);
      if (response.ok) {
        return await response.json();
      }
    } catch (error) {
      if (i === retries - 1) throw error;
      await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
    }
  }
}
```


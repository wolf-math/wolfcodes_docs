---
title: Fetch API
sidebar_position: 12
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is the `fetch()` API?

The **`fetch()` API** is the standard way to make HTTP requests in the browser. It lets your JavaScript load data from a server, send form data, and react to responses without reloading the page.

### Smallest working example

```javascript
fetch("/api/users")
  .then(response => response.json())
  .then(users => {
    console.log(users);
  });
```

## Why this matters

Most modern web apps need to load or send data:

- Load a list of users, posts, or products
- Submit a form without a full page refresh
- Save changes to the server
- Poll for updates in the background

## Making a basic request

The simplest use of `fetch()` is a `GET` request:

```javascript
fetch("/api/users")
  .then(response => response.json())
  .then(users => {
    console.log(users);
  });
```

### Understanding the response

`fetch()` resolves to a `Response` object:

```javascript
fetch("/api/users")
  .then(response => {
    console.log(response.status); // 200, 404, 500, and so on
    console.log(response.ok); // true for 200-299
    console.log(response.headers);

    return response.json();
  })
  .then(data => {
    console.log(data);
  });
```

## Handling JSON

Most browser-to-server APIs use JSON:

```javascript
fetch("/api/users")
  .then(response => response.json())
  .then(users => {
    users.forEach(user => {
      console.log(user.name);
    });
  });
```

### Other response types

```javascript
fetch("/api/data.txt")
  .then(response => response.text())
  .then(text => {
    console.log(text);
  });
```

```javascript
const image = document.querySelector("#avatar");

fetch("/api/image.jpg")
  .then(response => response.blob())
  .then(blob => {
    if (image) {
      image.src = URL.createObjectURL(blob);
    }
  });
```

## Handling errors

One important detail: `fetch()` only rejects for network-level problems. HTTP errors like `404` and `500` still give you a resolved `Response`.

```javascript
fetch("/api/users")
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    return response.json();
  })
  .then(users => {
    console.log(users);
  })
  .catch(error => {
    console.error("Fetch failed:", error);
  });
```

:::warning
Do not assume `fetch()` succeeded just because the promise resolved. Check `response.ok` before treating the request as successful.
:::

## Using `async` / `await`

`fetch()` often reads more clearly with `async` / `await`:

```javascript
async function loadUsers() {
  try {
    const response = await fetch("/api/users");

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const users = await response.json();
    console.log(users);
  } catch (error) {
    console.error("Failed to load users:", error);
  }
}
```

## Showing loading and error states

Good UI usually shows what is happening while data loads:

```javascript
async function loadUsers() {
  const loadingElement = document.querySelector("#loading");
  const errorElement = document.querySelector("#error");
  const usersElement = document.querySelector("#users");

  if (loadingElement) {
    loadingElement.hidden = false;
  }

  if (errorElement) {
    errorElement.hidden = true;
    errorElement.textContent = "";
  }

  if (usersElement) {
    usersElement.innerHTML = "";
  }

  try {
    const response = await fetch("/api/users");
    if (!response.ok) {
      throw new Error("Failed to load users");
    }

    const users = await response.json();

    if (usersElement) {
      users.forEach(user => {
        const listItem = document.createElement("li");
        listItem.textContent = user.name;
        usersElement.appendChild(listItem);
      });
    }
  } catch (error) {
    if (errorElement) {
      errorElement.hidden = false;
      errorElement.textContent = "Failed to load users";
    }
  } finally {
    if (loadingElement) {
      loadingElement.hidden = true;
    }
  }
}
```

## Sending data with `fetch()`

### Sending JSON

```javascript
fetch("/api/users", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    name: "Alice",
    email: "alice@example.com"
  })
})
  .then(response => response.json())
  .then(data => {
    console.log("User created:", data);
  });
```

### Sending form data

Learn more about [forms and user input](../events/forms_input) in the events section.

```javascript
const form = document.querySelector("form");

if (form) {
  form.addEventListener("submit", async event => {
    event.preventDefault();

    const formData = new FormData(form);

    const response = await fetch("/api/submit", {
      method: "POST",
      body: formData
    });

    const result = await response.json();
    console.log("Submitted:", result);
  });
}
```

### Other HTTP methods

```javascript
fetch("/api/users/123", {
  method: "PUT",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ name: "Bob" })
});
```

```javascript
fetch("/api/users/123", {
  method: "DELETE"
});
```

```javascript
fetch("/api/users/123", {
  method: "PATCH",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ name: "Charlie" })
});
```

## Common patterns

### Reusable request helper

```javascript
async function apiRequest(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers
    }
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  return response.json();
}
```

### Parallel requests

```javascript
const [user, posts] = await Promise.all([
  fetch("/api/user/123").then(response => response.json()),
  fetch("/api/user/123/posts").then(response => response.json())
]);
```

Learn more about [`Promise.all()`](/docs/javascript/guides/async/promises#promiseall--wait-for-all-promises).

### Polling for updates

If your page needs to check for new data regularly, `fetch()` is often paired with a timer:

```javascript
function updateUI(data) {
  console.log("Update UI with:", data);
}

async function pollForUpdates() {
  try {
    const response = await fetch("/api/updates");
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const data = await response.json();
    updateUI(data);
  } catch (error) {
    console.error("Polling failed:", error);
  }
}

const pollIntervalId = setInterval(pollForUpdates, 5000);

function stopPolling() {
  clearInterval(pollIntervalId);
}
```

## Security and browser rules

### CORS

Browsers block many cross-origin requests unless the server allows them:

```javascript
fetch("https://api.example.com/data")
  .catch(error => {
    console.error("CORS or network error:", error);
  });
```

### Same-origin requests

Requests to the same origin are the simplest case:

```javascript
fetch("/api/data")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
```

### Avoid unsafe HTML insertion

```javascript
const commentsContainer = document.querySelector("#comments");

fetch("/api/comments")
  .then(response => response.json())
  .then(comments => {
    if (!commentsContainer) {
      return;
    }

    comments.forEach(comment => {
      const paragraph = document.createElement("p");
      paragraph.textContent = comment.text;
      commentsContainer.appendChild(paragraph);
    });
  });
```

## Summary

- `fetch()` is the standard browser API for loading and sending data.
- Always check `response.ok` before treating a response as successful.
- Use loading states and error states so the UI stays understandable while requests are in flight.
- `fetch()` works well with `async` / `await`, `FormData`, and patterns like polling.

## Next up

- [Web Storage](./browser_storage)
- [Timers, Scheduling, and Animation](./async_browser_apis)
- [Forms and User Input](../events/forms_input)

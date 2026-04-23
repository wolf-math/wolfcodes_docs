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

## What does "putting it together" mean?

Learning JavaScript one concept at a time is useful.

Writing real JavaScript means combining those concepts:

- Variables hold values.
- Objects group related data.
- Arrays hold lists.
- Functions name reusable behavior.
- Conditionals make decisions.
- Loops and array methods repeat work.
- Classes model stateful things.
- Modules organize code across files.
- Async code handles work that finishes later.
- Errors help you deal with failure.

This guide shows how those pieces fit together in normal programs.

## Why this matters

Most real code is not "just arrays" or "just functions."

You might use an array of objects, pass it into a function, validate it with a conditional, transform it with `map`, and handle an error if something goes wrong.

The goal is not to use every feature at once.

The goal is to choose the pieces that make the code clear.

## A small data-processing program

Start with a simple list of users.

```javascript
const users = [
  { id: 1, name: "Dirk", active: true, points: 42 },
  { id: 2, name: "Nia", active: false, points: 18 },
  { id: 3, name: "Ari", active: true, points: 31 },
];
```

This uses an array to hold multiple users.

Each user is an object with related data.

Now add a function that answers one question.

```javascript
function getActiveUsers(users) {
  return users.filter((user) => user.active);
}

const activeUsers = getActiveUsers(users);

console.log(activeUsers);
```

`filter` creates a new array containing only the users where `user.active` is `true`.

## Adding a derived value

Programs often need to turn raw data into a useful result.

```javascript
function getTotalPoints(users) {
  return users.reduce((total, user) => total + user.points, 0);
}

const totalPoints = getTotalPoints(activeUsers);

console.log(totalPoints);
```

`reduce` combines the array into one value.

In this case, it adds up the `points` values for all active users.

## Formatting output

A separate function can handle presentation.

```javascript
function formatUserSummary(users) {
  const activeUsers = getActiveUsers(users);
  const totalPoints = getTotalPoints(activeUsers);

  return `${activeUsers.length} active users have ${totalPoints} total points.`;
}

console.log(formatUserSummary(users));
```

This function combines other functions instead of doing all the work itself.

That is a common pattern in JavaScript: write small functions, then compose them into larger behavior.

## Adding decisions

Use conditionals when the program needs to branch.

```javascript
function getStatusMessage(user) {
  if (!user.active) {
    return `${user.name} is inactive.`;
  }

  if (user.points >= 40) {
    return `${user.name} is a top contributor.`;
  }

  return `${user.name} is active.`;
}

for (const user of users) {
  console.log(getStatusMessage(user));
}
```

The `for...of` loop reads each user.

The function decides which message to return.

## Grouping behavior with a class

A class is useful when data and behavior belong together.

```javascript
class Scoreboard {
  constructor(users) {
    this.users = users;
  }

  getActiveUsers() {
    return this.users.filter((user) => user.active);
  }

  getTotalPoints() {
    return this.getActiveUsers().reduce((total, user) => {
      return total + user.points;
    }, 0);
  }

  getSummary() {
    return `${this.getActiveUsers().length} active users have ${this.getTotalPoints()} total points.`;
  }
}

const scoreboard = new Scoreboard(users);

console.log(scoreboard.getSummary());
```

The `Scoreboard` class owns the list of users.

Its methods describe the operations that belong to that list.

## Organizing code with modules

As a program grows, split related code into files.

```javascript
// scoreboard.js
export class Scoreboard {
  constructor(users) {
    this.users = users;
  }

  getActiveUsers() {
    return this.users.filter((user) => user.active);
  }

  getTotalPoints() {
    return this.getActiveUsers().reduce((total, user) => {
      return total + user.points;
    }, 0);
  }
}
```

```javascript
// main.js
import { Scoreboard } from "./scoreboard.js";

const users = [
  { id: 1, name: "Dirk", active: true, points: 42 },
  { id: 2, name: "Nia", active: false, points: 18 },
  { id: 3, name: "Ari", active: true, points: 31 },
];

const scoreboard = new Scoreboard(users);

console.log(scoreboard.getTotalPoints());
```

Modules help you keep each file focused.

They also make code easier to reuse and test.

## Handling async work

Some work finishes later, such as reading from a database or calling an API.

This example uses a promise to imitate loading data.

```javascript
function loadUsers() {
  return Promise.resolve([
    { id: 1, name: "Dirk", active: true, points: 42 },
    { id: 2, name: "Nia", active: false, points: 18 },
    { id: 3, name: "Ari", active: true, points: 31 },
  ]);
}

function getTotalPoints(users) {
  return users.reduce((total, user) => total + user.points, 0);
}

async function main() {
  const users = await loadUsers();

  console.log(getTotalPoints(users));
}

main();
```

`await` pauses the `main` function until the promise resolves.

Then the rest of the code can use the loaded users like normal data.

## Handling errors

Real programs need to handle failure.

```javascript
function loadUsers() {
  return Promise.reject(new Error("Could not load users"));
}

function getTotalPoints(users) {
  return users.reduce((total, user) => total + user.points, 0);
}

async function main() {
  try {
    const users = await loadUsers();

    console.log(getTotalPoints(users));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```

The `try` block contains the work that might fail.

The `catch` block decides what to do with the error.

## A complete example

Here is a small program that combines the same ideas.

```javascript
class TodoList {
  constructor(todos) {
    this.todos = todos;
  }

  addTodo(text) {
    this.todos.push({
      id: this.todos.length + 1,
      text,
      completed: false,
    });
  }

  completeTodo(id) {
    const todo = this.todos.find((todo) => todo.id === id);

    if (!todo) {
      throw new Error("Todo not found");
    }

    todo.completed = true;
  }

  getOpenTodos() {
    return this.todos.filter((todo) => !todo.completed);
  }

  getSummary() {
    const openCount = this.getOpenTodos().length;
    return `${openCount} todos left.`;
  }
}

function loadTodos() {
  return Promise.resolve([
    { id: 1, text: "Review arrays", completed: true },
    { id: 2, text: "Practice functions", completed: false },
  ]);
}

async function main() {
  try {
    const todos = await loadTodos();
    const todoList = new TodoList(todos);

    todoList.addTodo("Build a small project");
    todoList.completeTodo(2);

    console.log(todoList.getSummary());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```

This program uses:

- **Objects** to represent todos
- **An array** to store the todo list
- **A class** to group state and behavior
- **Methods** to change and read state
- **A conditional** to handle a missing todo
- **Array methods** such as `push`, `find`, and `filter`
- **A promise** to represent async loading
- **`async` / `await`** to read async code clearly
- **`try` / `catch`** to handle errors

## Choosing the right pieces

Use variables for values you need to name.

Use objects when values belong together.

Use arrays when you have a list.

Use functions when you can give a useful name to a reusable action.

Use classes when state and behavior naturally belong together.

Use modules when a file is doing too many jobs.

Use async code when the result arrives later.

Use errors when something cannot continue normally.

## What to learn next

After the JavaScript fundamentals, choose a direction based on what you want to build.

For browser projects, learn:

- DOM selection and updates
- Events
- Forms
- Fetch requests
- Local storage

For Node.js projects, learn:

- Reading and writing files
- Working with packages from npm
- Environment variables
- HTTP servers
- Command-line scripts

For larger applications, learn:

- Testing
- TypeScript
- Frameworks such as React, Vue, Express, or Next.js
- Debugging tools
- Performance basics

## Best practices

Build small programs that combine two or three concepts at a time.

Read your own code out loud and ask whether each name explains its job.

Keep functions focused.

Keep classes focused.

Move repeated logic into functions or methods.

Split files when one file becomes hard to scan.

Expect mistakes. Debugging is part of learning to write real programs.

## Summary

JavaScript programs are built by combining simple pieces.

Data structures hold information. Functions and methods organize behavior. Control flow makes decisions. Modules separate responsibilities. Async code handles work that finishes later.

The best way to keep improving is to build small projects, notice what gets messy, and use these tools to make the code clearer.

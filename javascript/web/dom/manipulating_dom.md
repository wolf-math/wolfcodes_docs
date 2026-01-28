---
title: Manipulating the DOM
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Reading and updating text

Once you've [selected an element](/docs/javascript/web/dom/selecting_elements), you can read and modify its text content.

### `textContent`

`textContent` gets or sets the **plain text** content of an element:

```javascript
const paragraph = document.querySelector('p');

// Read text
console.log(paragraph.textContent);  // "Hello World"

// Update text
paragraph.textContent = 'New text';

// textContent ignores HTML tags
paragraph.textContent = '<strong>Bold</strong>';  // Displays as text, not HTML
// Result: "<strong>Bold</strong>" (shown as text, not rendered as HTML)
```

**Use `textContent` when:** You want plain text only (safer, prevents XSS attacks).

### `innerHTML`

`innerHTML` gets or sets the **HTML content** of an element:

```javascript
const div = document.querySelector('div');

// Read HTML
console.log(div.innerHTML);  // "<p>Hello</p>"

// Update HTML
div.innerHTML = '<p>New paragraph</p>';

// innerHTML renders HTML
div.innerHTML = '<strong>Bold</strong>';  // Renders as bold text
```

**Use `innerHTML` when:** You need to insert HTML (but be careful with user input—see safety notes below).

### Safety with `innerHTML`

**Warning:** Using `innerHTML` with user input can lead to **XSS (Cross-Site Scripting)** attacks:

```javascript
// DANGEROUS: User input directly in innerHTML
const userInput = '<img src=x onerror="alert(\'XSS\')">';
element.innerHTML = userInput;  // Executes malicious code!

// Safe: Use textContent or sanitize input
element.textContent = userInput;  // Safe: displays as text
```

**Best practice:** Use `textContent` unless you specifically need HTML. If you must use `innerHTML` with user input, sanitize it first.

## Attributes

HTML elements have attributes (`id`, `class`, `src`, `href`, etc.). You can read and modify them:

### Reading attributes

```javascript
const link = document.querySelector('a');

link.id;              // Get ID
link.className;       // Get class attribute
link.href;            // Get href (full URL)
link.getAttribute('href');  // Get href (as written in HTML)

// For custom attributes (data-*)
link.dataset.userId;  // Get data-user-id="123"
link.getAttribute('data-user-id');  // Alternative
```

### Setting attributes

```javascript
const img = document.querySelector('img');

// Direct property (for standard attributes)
img.src = 'new-image.jpg';
img.alt = 'New alt text';
img.id = 'myImage';

// Using setAttribute (works for any attribute)
img.setAttribute('src', 'new-image.jpg');
img.setAttribute('data-id', '123');
img.setAttribute('aria-label', 'Description');
```

### Removing attributes

```javascript
const element = document.querySelector('div');

element.removeAttribute('id');
element.removeAttribute('data-custom');
```

### Data attributes

HTML5 data attributes (`data-*`) are commonly used to store custom data:

```html
<div data-user-id="123" data-status="active">User</div>
```

```javascript
const div = document.querySelector('div');

// Access via dataset (converts kebab-case to camelCase)
div.dataset.userId;    // "123"
div.dataset.status;    // "active"

// Or use getAttribute
div.getAttribute('data-user-id');  // "123"
```

## Classes

Managing CSS classes is a common task. The `classList` property makes this easy:

### `classList.add()`

Add one or more classes:

```javascript
const element = document.querySelector('div');

element.classList.add('active');
element.classList.add('highlighted', 'visible');  // Multiple classes
```

### `classList.remove()`

Remove one or more classes:

```javascript
element.classList.remove('active');
element.classList.remove('highlighted', 'visible');
```

### `classList.toggle()`

Add the class if it's not present, remove it if it is:

```javascript
element.classList.toggle('active');  // Toggle on/off
element.classList.toggle('active', true);  // Force add
element.classList.toggle('active', false); // Force remove
```

### `classList.contains()`

Check if an element has a class:

```javascript
if (element.classList.contains('active')) {
  console.log('Element is active');
}
```

### `classList.replace()`

Replace one class with another:

```javascript
element.classList.replace('old-class', 'new-class');
```

### Example: Toggle button state

```javascript
const button = document.querySelector('button');

button.addEventListener('click', function() {
  button.classList.toggle('active');
  
  if (button.classList.contains('active')) {
    button.textContent = 'Active';
  } else {
    button.textContent = 'Inactive';
  }
});
```

## Inline styles

You can modify inline styles directly via the `style` property:

```javascript
const element = document.querySelector('div');

// Set individual styles
element.style.color = 'red';
element.style.backgroundColor = 'blue';
element.style.fontSize = '18px';
element.style.display = 'none';

// Note: CSS properties use camelCase in JavaScript
// CSS: background-color → JavaScript: backgroundColor
// CSS: font-size → JavaScript: fontSize
```

### Setting multiple styles

```javascript
// Method 1: Set individually
element.style.color = 'red';
element.style.fontSize = '18px';

// Method 2: Use cssText (replaces all styles)
element.style.cssText = 'color: red; font-size: 18px;';

// Method 3: Object.assign
Object.assign(element.style, {
  color: 'red',
  fontSize: '18px'
});
```

**Best practice:** Generally, use CSS classes instead of inline styles. Only use inline styles for dynamic values (e.g., positioning based on calculations).

## Creating elements

Create new elements dynamically:

```javascript
// Create element
const newDiv = document.createElement('div');
const newParagraph = document.createElement('p');
const newButton = document.createElement('button');

// Set properties before adding to DOM
newDiv.textContent = 'Hello';
newDiv.className = 'container';
newParagraph.textContent = 'Paragraph text';
```

### Creating with `innerHTML`

You can also create elements using `innerHTML`:

```javascript
const container = document.querySelector('#container');
container.innerHTML = '<div class="item">New item</div>';
```

**Note:** This replaces all content. For appending, use `insertAdjacentHTML`:

```javascript
container.insertAdjacentHTML('beforeend', '<div>New item</div>');
```

## Appending and removing elements

### Appending elements

Add elements to the DOM:

```javascript
const parent = document.querySelector('#container');
const newDiv = document.createElement('div');
newDiv.textContent = 'New element';

// Add to end
parent.appendChild(newDiv);

// Add to beginning
parent.insertBefore(newDiv, parent.firstChild);

// Add after another element
parent.insertBefore(newDiv, parent.children[1]);

// Modern alternative: insertAdjacentElement
parent.insertAdjacentElement('beforeend', newDiv);
```

### `insertAdjacentHTML` positions

```javascript
// beforebegin - before the element
element.insertAdjacentHTML('beforebegin', '<div>Before</div>');

// afterbegin - inside, at the start
element.insertAdjacentHTML('afterbegin', '<div>First child</div>');

// beforeend - inside, at the end (like appendChild)
element.insertAdjacentHTML('beforeend', '<div>Last child</div>');

// afterend - after the element
element.insertAdjacentHTML('afterend', '<div>After</div>');
```

### Removing elements

```javascript
const element = document.querySelector('#toRemove');

// Remove from parent
element.parentElement.removeChild(element);

// Modern alternative (simpler)
element.remove();
```

### Example: Dynamic list

```javascript
function addListItem(text) {
  const list = document.querySelector('#myList');
  const newItem = document.createElement('li');
  newItem.textContent = text;
  
  // Add delete button
  const deleteBtn = document.createElement('button');
  deleteBtn.textContent = 'Delete';
  deleteBtn.addEventListener('click', function() {
    newItem.remove();
  });
  
  newItem.appendChild(deleteBtn);
  list.appendChild(newItem);
}

addListItem('Item 1');
addListItem('Item 2');
```

## Document fragments

When adding many elements, use **document fragments** for better performance:

```javascript
// Without fragment (slow - triggers reflow each time)
const list = document.querySelector('#list');
for (let i = 0; i < 100; i++) {
  const item = document.createElement('li');
  item.textContent = `Item ${i}`;
  list.appendChild(item);  // Triggers reflow 100 times
}

// With fragment (fast - single reflow)
const list = document.querySelector('#list');
const fragment = document.createDocumentFragment();
for (let i = 0; i < 100; i++) {
  const item = document.createElement('li');
  item.textContent = `Item ${i}`;
  fragment.appendChild(item);
}
list.appendChild(fragment);  // Single reflow
```

Fragments let you build elements in memory before adding them to the DOM.

## Common patterns

### Show/hide elements

```javascript
// Method 1: display property
element.style.display = 'none';   // Hide
element.style.display = 'block';  // Show

// Method 2: visibility property (keeps space)
element.style.visibility = 'hidden';  // Hide
element.style.visibility = 'visible'; // Show

// Method 3: class-based (best practice)
element.classList.add('hidden');    // Hide (CSS: .hidden { display: none; })
element.classList.remove('hidden'); // Show
```

### Updating multiple elements

```javascript
// Update all matching elements
document.querySelectorAll('.item').forEach(item => {
  item.textContent = 'Updated';
  item.classList.add('highlighted');
});
```

### Cloning elements

```javascript
const original = document.querySelector('.template');
const clone = original.cloneNode(true);  // true = deep clone
clone.id = 'new-id';  // Change ID to avoid duplicates
document.body.appendChild(clone);
```

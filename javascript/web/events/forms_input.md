---
title: Forms and User Input
sidebar_position: 7
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Reading input values

Forms collect user input through various input types. JavaScript lets you read and validate these values.

### Text inputs

```html
<input type="text" id="username" />
```

```javascript
const input = document.querySelector('#username');

// Read value
const username = input.value;
console.log(username);

// Update value
input.value = 'new value';

// Listen for changes
input.addEventListener('input', function() {
  console.log('Current value:', input.value);
});
```

### Textareas

```html
<textarea id="message"></textarea>
```

```javascript
const textarea = document.querySelector('#message');
const message = textarea.value;
```

Textareas work the same way as text inputs—use `.value` to read and set their content.

### Select dropdowns

```html
<select id="country">
  <option value="us">United States</option>
  <option value="uk">United Kingdom</option>
  <option value="ca">Canada</option>
</select>
```

```javascript
const select = document.querySelector('#country');

// Get selected value
const country = select.value;  // "us", "uk", or "ca"

// Set selected value
select.value = 'uk';

// Get selected option element
const selectedOption = select.options[select.selectedIndex];
console.log(selectedOption.text);  // "United Kingdom"
```

### Checkboxes

```html
<input type="checkbox" id="agree" />
```

```javascript
const checkbox = document.querySelector('#agree');

// Check if checked
if (checkbox.checked) {
  console.log('Checkbox is checked');
}

// Set checked state
checkbox.checked = true;

// Listen for changes
checkbox.addEventListener('change', function() {
  console.log('Checked:', checkbox.checked);
});
```

### Radio buttons

```html
<input type="radio" name="size" value="small" id="size-small" />
<input type="radio" name="size" value="medium" id="size-medium" />
<input type="radio" name="size" value="large" id="size-large" />
```

```javascript
// Get selected radio button
const selected = document.querySelector('input[name="size"]:checked');
if (selected) {
  console.log('Selected size:', selected.value);
}

// Select a radio button
document.querySelector('#size-medium').checked = true;

// Listen for changes
document.querySelectorAll('input[name="size"]').forEach(radio => {
  radio.addEventListener('change', function() {
    console.log('Selected:', this.value);
  });
});
```

## Preventing default behavior

Forms have a default behavior: they submit to the server and reload the page. In modern web apps, you often want to handle submission with JavaScript instead.

### Prevent form submission

```html
<form id="myForm">
  <input type="text" name="username" />
  <button type="submit">Submit</button>
</form>
```

```javascript
const form = document.querySelector('#myForm');

form.addEventListener('submit', function(e) {
  e.preventDefault();  // Prevent default form submission
  
  // Get form data
  const formData = new FormData(form);
  const username = formData.get('username');
  
  // Handle form data yourself
  console.log('Username:', username);
  
  // Maybe send to server with fetch, update UI, etc.
});
```

### Why `preventDefault()` matters

Without `preventDefault()`, the form submits and the page reloads, losing any JavaScript state. By preventing the default, you keep control and can:

- Validate data before sending
- Show loading states
- Handle errors gracefully
- Update the UI without reloading

## Form validation basics

Validation ensures users enter correct data before submission.

### HTML5 validation

HTML5 provides built-in validation:

```html
<input type="email" required />
<input type="number" min="0" max="100" />
<input type="text" pattern="[A-Za-z]+" />
```

```javascript
const input = document.querySelector('input[type="email"]');

// Check if valid
if (input.validity.valid) {
  console.log('Valid email');
} else {
  console.log('Invalid email:', input.validationMessage);
}

// Check specific validation errors
if (input.validity.valueMissing) {
  console.log('Email is required');
}
if (input.validity.typeMismatch) {
  console.log('Not a valid email format');
}
```

### JavaScript validation

For custom validation, check values yourself:

```javascript
function validateForm(form) {
  const username = form.querySelector('#username').value;
  const email = form.querySelector('#email').value;
  
  // Check if empty
  if (!username.trim()) {
    showError('Username is required');
    return false;
  }
  
  // Check length
  if (username.length < 3) {
    showError('Username must be at least 3 characters');
    return false;
  }
  
  // Check email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    showError('Invalid email format');
    return false;
  }
  
  return true;
}

form.addEventListener('submit', function(e) {
  e.preventDefault();
  
  if (validateForm(this)) {
    // Form is valid, submit it
    submitForm(this);
  }
});
```

### Showing validation errors

```javascript
function showError(message) {
  // Remove existing errors
  const existingError = document.querySelector('.error-message');
  if (existingError) {
    existingError.remove();
  }
  
  // Show new error
  const errorDiv = document.createElement('div');
  errorDiv.className = 'error-message';
  errorDiv.textContent = message;
  errorDiv.style.color = 'red';
  
  form.insertBefore(errorDiv, form.firstChild);
}

function clearErrors() {
  const errors = document.querySelectorAll('.error-message');
  errors.forEach(error => error.remove());
}
```

### Real-time validation

Validate as users type:

```javascript
const emailInput = document.querySelector('#email');

emailInput.addEventListener('input', function() {
  clearErrors();
  
  if (this.value && !isValidEmail(this.value)) {
    showFieldError(this, 'Invalid email format');
  }
});

function showFieldError(input, message) {
  input.style.borderColor = 'red';
  
  let error = input.parentElement.querySelector('.field-error');
  if (!error) {
    error = document.createElement('span');
    error.className = 'field-error';
    error.style.color = 'red';
    input.parentElement.appendChild(error);
  }
  error.textContent = message;
}
```

## Working with formdata

The `FormData` API makes working with forms easier:

```javascript
const form = document.querySelector('#myForm');

form.addEventListener('submit', function(e) {
  e.preventDefault();
  
  const formData = new FormData(form);
  
  // Get specific fields
  const username = formData.get('username');
  const email = formData.get('email');
  
  // Get all data as object
  const data = Object.fromEntries(formData);
  
  // Iterate over all fields
  for (const [key, value] of formData.entries()) {
    console.log(key, value);
  }
  
  // Send to server
  fetch('/api/submit', {
    method: 'POST',
    body: formData  // Can send FormData directly
  });
```

Learn more about [making HTTP requests with fetch](/docs/javascript/web/browser_api/networking).
});
```

### FormData with file uploads

```html
<input type="file" name="avatar" />
```

```javascript
const formData = new FormData(form);
const file = formData.get('avatar');

// file is a File object
console.log(file.name);    // filename
console.log(file.size);    // file size in bytes
console.log(file.type);    // MIME type

// Send file to server
fetch('/api/upload', {
  method: 'POST',
  body: formData
});
```

## Accessibility considerations

Making forms accessible helps all users, including those using screen readers.

### Labels

Always associate labels with inputs:

```html
<!-- Good: explicit association -->
<label for="username">Username</label>
<input type="text" id="username" name="username" />

<!-- Also good: wrapping -->
<label>
  Username
  <input type="text" name="username" />
</label>
```

### Error messages

Associate error messages with inputs:

```html
<label for="email">Email</label>
<input type="email" id="email" name="email" aria-describedby="email-error" />
<span id="email-error" class="error" role="alert"></span>
```

```javascript
function showError(inputId, message) {
  const input = document.querySelector(`#${inputId}`);
  const error = document.querySelector(`#${inputId}-error`);
  
  input.setAttribute('aria-invalid', 'true');
  error.textContent = message;
  error.setAttribute('role', 'alert');  // Screen readers announce this
}
```

### Required fields

Indicate required fields clearly:

```html
<label for="username">
  Username <span aria-label="required">*</span>
</label>
<input type="text" id="username" required aria-required="true" />
```

### Focus management

Move focus to errors or success messages:

```javascript
function showError(message) {
  const errorDiv = document.createElement('div');
  errorDiv.id = 'form-error';
  errorDiv.textContent = message;
  form.insertBefore(errorDiv, form.firstChild);
  
  // Move focus to error for screen readers
  errorDiv.setAttribute('tabindex', '-1');
  errorDiv.focus();
}
```

## Common patterns

### Form reset

```javascript
form.reset();  // Resets all form fields to default values
```

### Disable submit button

```javascript
const submitBtn = form.querySelector('button[type="submit"]');

// Disable while submitting
submitBtn.disabled = true;
submitBtn.textContent = 'Submitting...';

// Re-enable on error
submitBtn.disabled = false;
submitBtn.textContent = 'Submit';
```

### Multi-step forms

```javascript
let currentStep = 1;

function showStep(step) {
  document.querySelectorAll('.form-step').forEach((s, i) => {
    s.style.display = i + 1 === step ? 'block' : 'none';
  });
}

function nextStep() {
  if (validateCurrentStep()) {
    currentStep++;
    showStep(currentStep);
  }
}

function previousStep() {
  currentStep--;
  showStep(currentStep);
}
```

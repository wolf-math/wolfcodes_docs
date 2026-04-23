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

## What are forms and user input?

**Forms and user input** are how users send information to your page. JavaScript can read those values, validate them, respond to changes, and control what happens when a form is submitted.

### Smallest working example

```html
<label for="username">Username</label>
<input type="text" id="username" />
```

```javascript
const input = document.querySelector("#username");

if (input) {
  input.addEventListener("input", () => {
    console.log("Current value:", input.value);
  });
}
```

## Why this matters

Most interactive web pages depend on user input:

- Sign-in and sign-up forms
- Search boxes and filters
- Settings panels and preferences
- Checkout, feedback, and contact forms

## Reading input values

Different form controls expose their values in slightly different ways.

### Text inputs

```html
<input type="text" id="username" />
```

```javascript
const input = document.querySelector("#username");

if (input) {
  const username = input.value;
  console.log(username);

  input.value = "new value";

  input.addEventListener("input", () => {
    console.log("Current value:", input.value);
  });
}
```

### Textareas

```html
<textarea id="message"></textarea>
```

```javascript
const textarea = document.querySelector("#message");

if (textarea) {
  const message = textarea.value;
  console.log(message);
}
```

Textareas work like text inputs. Use `.value` to read and update their content.

### Select dropdowns

```html
<select id="country">
  <option value="us">United States</option>
  <option value="uk">United Kingdom</option>
  <option value="ca">Canada</option>
</select>
```

```javascript
const select = document.querySelector("#country");

if (select) {
  const country = select.value;
  console.log(country);

  select.value = "uk";

  const selectedOption = select.options[select.selectedIndex];
  console.log(selectedOption.text);
}
```

### Checkboxes

```html
<input type="checkbox" id="agree" />
```

```javascript
const checkbox = document.querySelector("#agree");

if (checkbox) {
  console.log("Checked:", checkbox.checked);

  checkbox.checked = true;

  checkbox.addEventListener("change", () => {
    console.log("Checked:", checkbox.checked);
  });
}
```

### Radio buttons

```html
<input type="radio" name="size" value="small" id="size-small" />
<input type="radio" name="size" value="medium" id="size-medium" />
<input type="radio" name="size" value="large" id="size-large" />
```

```javascript
const selected = document.querySelector('input[name="size"]:checked');
if (selected) {
  console.log("Selected size:", selected.value);
}

const medium = document.querySelector("#size-medium");
if (medium) {
  medium.checked = true;
}

document.querySelectorAll('input[name="size"]').forEach(radio => {
  radio.addEventListener("change", () => {
    console.log("Selected:", radio.value);
  });
});
```

:::tip
Rule of thumb: use `.value` for text-like fields, `.checked` for checkboxes, and `:checked` when reading the selected radio button.
:::

## Handling form submission

By default, forms submit to the server and reload the page. In many JavaScript-driven interfaces, you want to handle submission yourself.

### Prevent form submission

```html
<form id="myForm">
  <input type="text" name="username" />
  <button type="submit">Submit</button>
</form>
```

```javascript
const form = document.querySelector("#myForm");

if (form) {
  form.addEventListener("submit", e => {
    e.preventDefault();

    const formData = new FormData(form);
    const username = formData.get("username");

    console.log("Username:", username);
  });
}
```

### Why `preventDefault()` matters

Without `preventDefault()`, the browser submits the form right away and usually reloads the page. Preventing the default gives your code a chance to:

- Validate the input first
- Show loading or error states
- Send the data with `fetch()`
- Update the page without a full reload

## Validating form input

Validation helps make sure the user entered acceptable data before you continue.

### HTML5 validation

Browsers already support some useful validation rules:

```html
<input type="email" required />
<input type="number" min="0" max="100" />
<input type="text" pattern="[A-Za-z]+" />
```

```javascript
const emailInput = document.querySelector('input[type="email"]');

if (emailInput) {
  if (emailInput.validity.valid) {
    console.log("Valid email");
  } else {
    console.log("Invalid email:", emailInput.validationMessage);
  }

  if (emailInput.validity.valueMissing) {
    console.log("Email is required");
  }

  if (emailInput.validity.typeMismatch) {
    console.log("Not a valid email format");
  }
}
```

### JavaScript validation

Use JavaScript validation when you need rules that HTML alone does not cover:

```javascript
const form = document.querySelector("#myForm");

if (form) {
  form.addEventListener("submit", e => {
    e.preventDefault();
    clearFormErrors(form);

    if (validateForm(form)) {
      console.log("Form is valid");
    }
  });
}

function validateForm(form) {
  const usernameInput = form.querySelector("#username");
  const emailInput = form.querySelector("#email");

  if (!usernameInput || !emailInput) {
    return false;
  }

  const username = usernameInput.value.trim();
  const email = emailInput.value.trim();

  if (!username) {
    showFormError(form, "Username is required");
    return false;
  }

  if (username.length < 3) {
    showFormError(form, "Username must be at least 3 characters");
    return false;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    showFormError(form, "Invalid email format");
    return false;
  }

  return true;
}
```

### Showing validation errors

```javascript
function showFormError(form, message) {
  clearFormErrors(form);

  const errorDiv = document.createElement("div");
  errorDiv.className = "error-message";
  errorDiv.textContent = message;
  errorDiv.setAttribute("role", "alert");

  form.prepend(errorDiv);
}

function clearFormErrors(form) {
  form.querySelectorAll(".error-message").forEach(error => {
    error.remove();
  });
}
```

### Real-time validation

```javascript
const emailInput = document.querySelector("#email");

if (emailInput) {
  emailInput.addEventListener("input", () => {
    clearFieldError(emailInput);

    if (emailInput.value && !isValidEmail(emailInput.value)) {
      showFieldError(emailInput, "Invalid email format");
    }
  });
}

function showFieldError(input, message) {
  input.setAttribute("aria-invalid", "true");

  let error = input.parentElement?.querySelector(".field-error");
  if (!error && input.parentElement) {
    error = document.createElement("span");
    error.className = "field-error";
    input.parentElement.appendChild(error);
  }

  if (error) {
    error.textContent = message;
  }
}

function clearFieldError(input) {
  input.removeAttribute("aria-invalid");

  const error = input.parentElement?.querySelector(".field-error");
  if (error) {
    error.remove();
  }
}

function isValidEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}
```

:::note
Real-time validation is helpful, but it can feel noisy if every keystroke shows an error immediately. In many cases, a good pattern is to validate after the user has typed something meaningful or after the field loses focus.
:::

## Working with `FormData`

The `FormData` API is a convenient way to collect form values.

```javascript
const form = document.querySelector("#myForm");

if (form) {
  form.addEventListener("submit", e => {
    e.preventDefault();

    const formData = new FormData(form);

    const username = formData.get("username");
    const email = formData.get("email");

    const data = Object.fromEntries(formData);
    console.log(username, email, data);

    for (const [key, value] of formData.entries()) {
      console.log(key, value);
    }
  });
}
```

### Sending `FormData` with `fetch()`

```javascript
const form = document.querySelector("#myForm");

if (form) {
  form.addEventListener("submit", async e => {
    e.preventDefault();

    const formData = new FormData(form);

    await fetch("/api/submit", {
      method: "POST",
      body: formData
    });
  });
}
```

Learn more about [making HTTP requests with `fetch()`](../browser_api/networking).

### `FormData` with file uploads

```html
<input type="file" name="avatar" />
```

```javascript
const form = document.querySelector("#myForm");

if (form) {
  const formData = new FormData(form);
  const file = formData.get("avatar");

  if (file instanceof File) {
    console.log(file.name);
    console.log(file.size);
    console.log(file.type);
  }
}
```

## Accessibility considerations

Accessible forms are easier for everyone to use, including people using screen readers or keyboard navigation.

### Use labels

Always associate labels with inputs:

```html
<label for="username">Username</label>
<input type="text" id="username" name="username" />

<label>
  Username
  <input type="text" name="username" />
</label>
```

### Associate error messages

```html
<label for="email">Email</label>
<input type="email" id="email" name="email" aria-describedby="email-error" />
<span id="email-error" class="error" role="alert"></span>
```

```javascript
function showAccessibleError(inputId, message) {
  const input = document.querySelector(`#${inputId}`);
  const error = document.querySelector(`#${inputId}-error`);

  if (input && error) {
    input.setAttribute("aria-invalid", "true");
    error.textContent = message;
  }
}
```

### Mark required fields clearly

```html
<label for="username">
  Username <span aria-label="required">*</span>
</label>
<input type="text" id="username" required aria-required="true" />
```

### Manage focus when needed

```javascript
function showFormErrorAndFocus(form, message) {
  const errorDiv = document.createElement("div");
  errorDiv.id = "form-error";
  errorDiv.textContent = message;
  errorDiv.setAttribute("tabindex", "-1");

  form.prepend(errorDiv);
  errorDiv.focus();
}
```

## Common patterns

### Reset a form

```javascript
const form = document.querySelector("#myForm");

if (form) {
  form.reset();
}
```

### Disable the submit button while submitting

```javascript
const form = document.querySelector("#myForm");

if (form) {
  const submitButton = form.querySelector('button[type="submit"]');

  if (submitButton) {
    submitButton.disabled = true;
    submitButton.textContent = "Submitting...";

    submitButton.disabled = false;
    submitButton.textContent = "Submit";
  }
}
```

### Multi-step forms

```javascript
let currentStep = 1;

function showStep(step) {
  document.querySelectorAll(".form-step").forEach((section, index) => {
    section.style.display = index + 1 === step ? "block" : "none";
  });
}

function nextStep() {
  if (validateCurrentStep()) {
    currentStep += 1;
    showStep(currentStep);
  }
}

function previousStep() {
  currentStep -= 1;
  showStep(currentStep);
}
```

## Summary

- Use `.value`, `.checked`, and `FormData` to read user input depending on the kind of field.
- `submit` handlers usually call `preventDefault()` so your JavaScript can validate and control what happens next.
- Start with built-in HTML validation when it fits, then add JavaScript rules for custom cases.
- Good forms are not just functional; they also need labels, clear errors, and accessible focus behavior.

## Next up

- [Events](./dom_events)
- [Selecting elements](../dom/selecting_elements)
- [Networking](../browser_api/networking)

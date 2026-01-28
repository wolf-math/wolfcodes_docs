---
title: Date
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
<!-- ## Properties

```javascript
> Object.getOwnPropertyNames(Date.prototype)
['constructor', 'toString', 'toDateString', 'toTimeString', 'toISOString', 'toUTCString', 'toLocaleString', 'toLocaleDateString', 'toLocaleTimeString', 'valueOf', 'getTime', 'getFullYear', 'getUTCFullYear', 'getMonth', 'getUTCMonth', 'getDate', 'getUTCDate', 'getDay', 'getUTCDay', 'getHours', 'getUTCHours', 'getMinutes', 'getUTCMinutes', 'getSeconds', 'getUTCSeconds', 'getMilliseconds', 'getUTCMilliseconds', 'getTimezoneOffset', 'setTime', 'setMilliseconds', 'setUTCMilliseconds', 'setSeconds', 'setUTCSeconds', 'setMinutes', 'setUTCMinutes', 'setHours', 'setUTCHours', 'setDate', 'setUTCDate', 'setMonth', 'setUTCMonth', 'setFullYear', 'setUTCFullYear', 'toJSON']
``` -->

## Definition

The `Date` object represents a single moment in time. JavaScript dates are based on the Unix Epoch (January 1, 1970, 00:00:00 UTC).

```javascript
> typeof new Date()
"object"

> new Date() instanceof Date
true
```

## Using dates

### Current Date/Time

```javascript
const now = new Date()  // Current date and time
```

### From Timestamp

```javascript
const date = new Date(1609459200000)  // Milliseconds since epoch
```

### From Date String

```javascript
const date1 = new Date("2023-01-01")
const date2 = new Date("January 1, 2023")
const date3 = new Date("2023-01-01T12:00:00Z")
```

### From Components

```javascript
// new Date(year, monthIndex, day, hours, minutes, seconds, milliseconds)
const date = new Date(2023, 0, 1, 12, 30, 0, 0)
// January 1, 2023, 12:30:00
// Note: monthIndex is 0-based (0 = January, 11 = December)
```

### Date.now()

Returns the current timestamp in milliseconds:

```javascript
Date.now()  // 1609459200000 (example)
```

## Operations on dates

### Getting Date Components

```javascript
const date = new Date(2023, 0, 15, 14, 30, 45)

date.getFullYear()      // 2023
date.getMonth()         // 0 (January, 0-based)
date.getDate()          // 15 (day of month)
date.getDay()           // 0 (Sunday, 0-based)
date.getHours()         // 14
date.getMinutes()       // 30
date.getSeconds()       // 45
date.getMilliseconds()  // 0
date.getTime()          // Timestamp in milliseconds
```

### UTC Methods

Get date components in UTC:

```javascript
const date = new Date("2023-01-15T14:30:45Z")

date.getUTCFullYear()      // 2023
date.getUTCMonth()         // 0
date.getUTCDate()          // 15
date.getUTCHours()         // 14
date.getUTCMinutes()       // 30
date.getUTCSeconds()       // 45
```

### Setting Date Components

```javascript
const date = new Date()

date.setFullYear(2024)
date.setMonth(5)         // June (0-based)
date.setDate(20)
date.setHours(15)
date.setMinutes(45)
date.setSeconds(30)
date.setMilliseconds(500)
```

### UTC Setting Methods

```javascript
const date = new Date()

date.setUTCFullYear(2024)
date.setUTCMonth(5)
date.setUTCDate(20)
date.setUTCHours(15)
date.setUTCMinutes(45)
date.setUTCSeconds(30)
```

## Date formatting

### toString()

Returns a string representation:

```javascript
new Date().toString()  // "Mon Jan 15 2024 14:30:45 GMT-0500 (EST)"
```

### toISOString()

Returns ISO 8601 format:

```javascript
new Date().toISOString()  // "2024-01-15T19:30:45.123Z"
```

### toDateString()

Returns date portion:

```javascript
new Date().toDateString()  // "Mon Jan 15 2024"
```

### toTimeString()

Returns time portion:

```javascript
new Date().toTimeString()  // "14:30:45 GMT-0500 (EST)"
```

### toLocaleString()

Returns localized string:

```javascript
new Date().toLocaleString()           // "1/15/2024, 2:30:45 PM"
new Date().toLocaleString('en-GB')    // "15/01/2024, 14:30:45"
new Date().toLocaleDateString()       // "1/15/2024"
new Date().toLocaleTimeString()       // "2:30:45 PM"
```

### Custom Formatting

```javascript
const date = new Date(2023, 0, 15)

const formatted = date.toLocaleDateString('en-US', {
  year: 'numeric',
  month: 'long',
  day: 'numeric'
})
// "January 15, 2023"
```

### Date arithmetic

#### Adding/subtracting time

```javascript
const date = new Date()

// Add days
date.setDate(date.getDate() + 7)  // 7 days later

// Add hours
date.setHours(date.getHours() + 2)  // 2 hours later

// Using timestamps
const tomorrow = new Date(Date.now() + 24 * 60 * 60 * 1000)  // 24 hours later
```

#### Date comparison

```javascript
const date1 = new Date(2023, 0, 1)
const date2 = new Date(2023, 0, 2)

date1 < date2    // true
date1 > date2    // false
date1.getTime() === date2.getTime()  // false
```

## Common patterns

### Get Start of Day

```javascript
function startOfDay(date) {
  const d = new Date(date)
  d.setHours(0, 0, 0, 0)
  return d
}
```

### Get End of Day

```javascript
function endOfDay(date) {
  const d = new Date(date)
  d.setHours(23, 59, 59, 999)
  return d
}
```

### Format Relative Time

```javascript
function formatRelative(date) {
  const now = new Date()
  const diff = now - date
  const seconds = Math.floor(diff / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)
  const days = Math.floor(hours / 24)
  
  if (days > 0) return `${days} days ago`
  if (hours > 0) return `${hours} hours ago`
  if (minutes > 0) return `${minutes} minutes ago`
  return `${seconds} seconds ago`
}
```

## Timezone considerations

JavaScript Date objects work in the local timezone:

```javascript
const date = new Date("2023-01-01T00:00:00Z")  // UTC midnight
date.toString()  // Shows in local timezone
date.toISOString()  // Always shows UTC
```

## Best practices

1. **Use ISO strings for storage**: Store dates as ISO strings for consistency.

2. **Be aware of timezones**: Always consider timezone when working with dates.

3. **Use libraries for complex operations**: Consider libraries like `date-fns` or `moment.js` for complex date manipulation.

4. **Use `getTime()` for comparisons**: More reliable than direct comparison.

5. **Remember month is 0-based**: January is 0, December is 11.


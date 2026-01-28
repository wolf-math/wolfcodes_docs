---
title: Dates and Times
sidebar_position: 2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is the datetime module?

The `datetime` module provides classes for working with dates and times in Python. It's part of the standard library and gives you everything you need to create, manipulate, format, and calculate with dates and times.

```python
from datetime import datetime, date, time

now = datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

today = date.today()
print(today)  # 2024-01-15
```

## Why this matters

Dates and times are everywhere in programming from logging events, scheduling tasks, calculating durations, parsing user input, working with databases, and more. The `datetime` module gives you:

- **Precise date/time handling**: Work with dates, times, and combinations of both
- **Timezone support**: Handle different timezones (with `timezone` and `timedelta`)
- **Formatting and parsing**: Convert between strings and datetime objects
- **Date arithmetic**: Calculate differences, add/subtract time periods
- **Calendar operations**: Get weekdays, determine if dates fall on weekends, etc.

Without proper date/time handling, you'd struggle with timezone conversions, leap years, daylight saving time, and other complexities. The `datetime` module handles all of this for you.

## How dates and times are stored

Understanding how computers store dates and times helps you work with the `datetime` module more effectively.

### Unix epoch time

Computers typically store dates and times as a number representing seconds (or milliseconds) since a fixed point in time called the **epoch**. The Unix epoch is January 1, 1970, 00:00:00 UTC.

```python
import time
from datetime import datetime

# Get current time as seconds since epoch
epoch_seconds = time.time()
print(epoch_seconds)  # 1705327845.123456 (example)

# Convert epoch time to datetime
dt = datetime.fromtimestamp(epoch_seconds)
print(dt)  # 2024-01-15 14:30:45.123456

# Convert datetime back to epoch time
epoch_seconds = dt.timestamp()
print(epoch_seconds)  # 1705327845.123456
```

### Why epoch time?

Storing dates as numbers since the epoch makes it easy to:
- **Calculate differences**: Subtract two epoch times to get the duration
- **Compare dates**: Compare numbers directly
- **Store efficiently**: A single number instead of multiple fields
- **Handle timezones**: Convert to/from UTC consistently

### Databases and epoch time

Most databases store dates and times as epoch seconds or milliseconds. This is why you'll often need to convert between `datetime` objects and timestamps when working with databases:

```python
from datetime import datetime

# When saving to database: convert datetime to timestamp
dt = datetime.now()
db_timestamp = int(dt.timestamp())  # Store as integer seconds
# or
db_timestamp_ms = int(dt.timestamp() * 1000)  # Store as milliseconds

# When reading from database: convert timestamp to datetime
stored_timestamp = 1705327845
dt = datetime.fromtimestamp(stored_timestamp)
print(dt)  # 2024-01-15 14:30:45
```

Different databases use different formats:
- **PostgreSQL, MySQL**: Often store as `TIMESTAMP` (internally epoch seconds)
- **SQLite**: Stores as text, integer (epoch seconds), or real (Julian day)
- **MongoDB**: Uses BSON Date type (milliseconds since epoch)
- **Redis**: Stores as integer (seconds) or string

The `datetime` module's `timestamp()` and `fromtimestamp()` methods make it easy to convert between Python's `datetime` objects and the numeric formats databases use.

### Internal representation

Python's `datetime` objects store dates and times internally as separate components (year, month, day, hour, minute, second, microsecond), but they can easily convert to and from epoch time when needed:

```python
from datetime import datetime

# Create a datetime
dt = datetime(2024, 1, 15, 14, 30, 45)

# Convert to timestamp (seconds since epoch)
timestamp = dt.timestamp()
print(timestamp)  # 1705327845.0

# Create from timestamp
dt2 = datetime.fromtimestamp(timestamp)
print(dt2)  # 2024-01-15 14:30:45
```

The `datetime` module abstracts away the epoch time details, letting you work with human readable dates and times while handling the underlying representation automatically.

## The main classes

The `datetime` module provides several classes:

- `date` - Represents a date (year, month, day)
- `time` - Represents a time (hour, minute, second, microsecond)
- `datetime` - Represents both date and time
- `timedelta` - Represents a duration (difference between dates/times)
- `timezone` - Represents timezone information

## Creating datetime objects

### Current date and time

```python
from datetime import datetime, date, time

# Current date and time
now = datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

# Current date only
today = date.today()
print(today)  # 2024-01-15

# Current time only (requires a date reference)
current_time = datetime.now().time()
print(current_time)  # 14:30:45.123456
```

### Creating specific dates and times

```python
from datetime import datetime, date, time

# Create a specific date
birthday = date(1990, 5, 15)
print(birthday)  # 1990-05-15

# Create a specific time
meeting_time = time(14, 30, 0)  # 2:30 PM
print(meeting_time)  # 14:30:00

# Create a specific datetime
event = datetime(2024, 12, 25, 10, 0, 0)
print(event)  # 2024-12-25 10:00:00

# Or combine date and time
event_date = date(2024, 12, 25)
event_time = time(10, 0, 0)
event = datetime.combine(event_date, event_time)
print(event)  # 2024-12-25 10:00:00
```

### Parsing strings

```python
from datetime import datetime

# Parse a string into a datetime object
date_string = "2024-01-15 14:30:00"
dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(dt)  # 2024-01-15 14:30:00

# Common format strings
dt1 = datetime.strptime("2024-01-15", "%Y-%m-%d")
dt2 = datetime.strptime("01/15/2024", "%m/%d/%Y")
dt3 = datetime.strptime("January 15, 2024", "%B %d, %Y")
```

## Accessing date and time components

You can access individual components of datetime objects:

```python
from datetime import datetime

now = datetime.now()

print(now.year)        # 2024
print(now.month)       # 1
print(now.day)         # 15
print(now.hour)        # 14
print(now.minute)      # 30
print(now.second)      # 45
print(now.microsecond) # 123456

# Day of the week (Monday is 0, Sunday is 6)
print(now.weekday())   # 0 (Monday)
print(now.isoweekday()) # 1 (Monday is 1, Sunday is 7)
```

## Formatting dates and times

Convert datetime objects to strings using `strftime()`:

```python
from datetime import datetime

now = datetime.now()

# Common format codes
print(now.strftime("%Y-%m-%d"))           # 2024-01-15
print(now.strftime("%B %d, %Y"))         # January 15, 2024
print(now.strftime("%m/%d/%Y"))           # 01/15/2024
print(now.strftime("%H:%M:%S"))           # 14:30:45
print(now.strftime("%I:%M %p"))           # 02:30 PM
print(now.strftime("%A, %B %d, %Y"))      # Monday, January 15, 2024
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-01-15 14:30:45
```

### Common format codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | Year with century | 2024 |
| `%y` | Year without century | 24 |
| `%m` | Month as number | 01 |
| `%B` | Full month name | January |
| `%b` | Abbreviated month | Jan |
| `%d` | Day of month | 15 |
| `%A` | Full weekday name | Monday |
| `%a` | Abbreviated weekday | Mon |
| `%H` | Hour (24-hour) | 14 |
| `%I` | Hour (12-hour) | 02 |
| `%M` | Minute | 30 |
| `%S` | Second | 45 |
| `%p` | AM/PM | PM |

## Date and time arithmetic

### Using timedelta

`timedelta` represents a duration, which is the difference between two dates or times:

```python
from datetime import datetime, timedelta

now = datetime.now()

# Add time
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)
in_30_minutes = now + timedelta(minutes=30)

# Subtract time
yesterday = now - timedelta(days=1)
last_week = now - timedelta(weeks=1)

# Combine units
future = now + timedelta(days=5, hours=3, minutes=30)
```

### Calculating differences

```python
from datetime import datetime, timedelta

date1 = datetime(2024, 1, 15)
date2 = datetime(2024, 1, 20)

difference = date2 - date1
print(difference)           # 5 days, 0:00:00
print(difference.days)      # 5
print(difference.seconds)   # 0
print(difference.total_seconds())  # 432000.0
```

### Comparing dates

```python
from datetime import datetime

date1 = datetime(2024, 1, 15)
date2 = datetime(2024, 1, 20)

print(date1 < date2)   # True
print(date1 > date2)   # False
print(date1 == date2)  # False
print(date1 != date2)  # True
```

## Working with timezones

### Naive vs aware datetime objects

- **Naive**: No timezone information (most common)
- **Aware**: Has timezone information

```python
from datetime import datetime, timezone, timedelta

# Naive datetime (no timezone)
naive = datetime.now()
print(naive.tzinfo)  # None

# Aware datetime (with timezone)
utc_now = datetime.now(timezone.utc)
print(utc_now.tzinfo)  # UTC

# Create timezone-aware datetime
eastern = timezone(timedelta(hours=-5))  # EST
dt_eastern = datetime.now(eastern)
print(dt_eastern)  # 2024-01-15 09:30:45.123456-05:00
```

### Converting between timezones

```python
from datetime import datetime, timezone, timedelta

# Create timezone objects
utc = timezone.utc
eastern = timezone(timedelta(hours=-5))
pacific = timezone(timedelta(hours=-8))

# Start with UTC time
utc_time = datetime(2024, 1, 15, 14, 30, 0, tzinfo=utc)

# Convert to Eastern
eastern_time = utc_time.astimezone(eastern)
print(eastern_time)  # 2024-01-15 09:30:00-05:00

# Convert to Pacific
pacific_time = utc_time.astimezone(pacific)
print(pacific_time)  # 2024-01-15 06:30:00-08:00
```

## Common patterns

### Get start/end of day

```python
from datetime import datetime, time

now = datetime.now()

# Start of day (midnight)
start_of_day = datetime.combine(now.date(), time.min)
print(start_of_day)  # 2024-01-15 00:00:00

# End of day (just before midnight)
end_of_day = datetime.combine(now.date(), time.max)
print(end_of_day)  # 2024-01-15 23:59:59.999999
```

### Calculate age

```python
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birthday = date(1990, 5, 15)
print(calculate_age(birthday))  # 33 (example)
```

### Find next occurrence of a weekday

```python
from datetime import datetime, timedelta

def next_weekday(start_date, weekday):
    """Find next occurrence of weekday (0=Monday, 6=Sunday)"""
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

today = datetime.now().date()
next_monday = next_weekday(today, 0)  # 0 = Monday
print(next_monday)
```

### Format relative time

```python
from datetime import datetime, timedelta

def time_ago(dt):
    """Return human-readable time difference"""
    now = datetime.now()
    diff = now - dt
    
    if diff.days > 365:
        years = diff.days // 365
        return f"{years} year{'s' if years > 1 else ''} ago"
    elif diff.days > 30:
        months = diff.days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    elif diff.days > 0:
        return f"{diff.days} day{'s' if diff.days > 1 else ''} ago"
    elif diff.seconds > 3600:
        hours = diff.seconds // 3600
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    else:
        return "just now"

past_time = datetime.now() - timedelta(hours=2)
print(time_ago(past_time))  # 2 hours ago
```

## Best practices

1. **Use `datetime` for most cases**: Unless you only need a date or time, `datetime` is usually the most flexible choice.
2. **Be aware of timezone issues**: If your application deals with multiple timezones, always use timezone-aware datetime objects. Store times in UTC and convert to local timezones for display.
3. **Use `strftime` and `strptime` consistently**: Stick to a consistent date format throughout your application to avoid parsing errors.
4. **Handle edge cases**: Be careful with date arithmetic around month boundaries, leap years, and daylight saving time transitions.
5. **Use `date.today()` instead of `datetime.now().date()`**: When you only need the date, `date.today()` is clearer and slightly more efficient.
6. **Prefer `timedelta` for date arithmetic**: It handles all the complexities of months, years, and leap years correctly.
7. **Validate user input**: When parsing date strings from users, always use try/except to handle invalid formats gracefully.

```python
from datetime import datetime

def safe_parse_date(date_string):
    """Safely parse a date string, returning None if invalid"""
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return None

user_input = "2024-01-15"
date = safe_parse_date(user_input)
if date:
    print(f"Valid date: {date}")
else:
    print("Invalid date format")
```

The `datetime` module is essential for any Python program that deals with dates and times. Master it, and you'll be able to handle all kinds of temporal data with confidence!


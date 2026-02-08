---
slug: temporal-datetime
title: "Temporal DateTime API"
author: Aaron Wolf
sidebar_position: 5
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
description: A practical introduction to JavaScript’s upcoming Temporal API, focusing on real-world use cases and mental models.
---

Dates in JavaScript have a well-earned reputation for being frustrating. The **Temporal API** is the long-term replacement for the legacy `Date` object, designed to fix many of its conceptual and practical flaws.

This article is based on my experience using Temporal and experimenting with how it fits into real-world applications. It is not as a comprehensive reference, but as a guide to how you might actually use it.

At the time of writing, Temporal is still a **Stage 3 proposal** (out of 4). That means it is close to standardization, but **not yet available natively** in JavaScript runtimes. If you want to try it today, you can use the official [polyfill](https://www.npmjs.com/package/@js-temporal/polyfill):

## A paradigm shift

To understand Temporal, you have to change how you think about dates.

In legacy JavaScript, `Date` objects are ultimately just wrappers around **epoch milliseconds**. Every date represents a specific instant in time, whether you care about that or not.

Temporal separates these ideas.

With Temporal, you can represent:
- a **calendar date** with no time,
- a **time of day** with no date,
- a **date and time** with no timezone,
- or a **fully qualified instant in time** tied to a location.

Some Temporal objects can be converted to epoch milliseconds. Others are intentionally *disconnected* from them.

That distinction is the core design improvement.

## Common use cases (for me, at least)

A useful naming rule of thumb:

> Temporal types that start with `Plain` are **not tied to epoch milliseconds**.

### `PlainDate`

A `PlainDate` represents a calendar date without time or timezone.

```js
const today = "2022-09-10";
// or:
// const today = { year: 2022, month: 9, day: 10 };

const temporalToday = Temporal.PlainDate.from(today);
```

The resulting object contains much more than just year, month, and day:

```js
{
  calendar: Calendar { id: "iso8601" },
  year: 2022,
  month: 9,
  day: 10,
  dayOfWeek: 6,
  dayOfYear: 253,
  weekOfYear: 36,
  daysInMonth: 30,
  daysInYear: 365,
  inLeapYear: false
}
```

This information is available *without* extra libraries or manual calculations.

The default calendar is `iso8601`, but Temporal supports others as well (for example, Hebrew or Chinese calendars).

### `PlainTime`

`PlainTime` represents a time of day, independent of any date.

```js
const time = "13:55:14";
const plainTimeNow = Temporal.PlainTime.from(time);
```

```js
{
  calendar: Calendar { id: "iso8601" },
  hour: 13,
  minute: 55,
  second: 14,
  millisecond: 0,
  microsecond: 0,
  nanosecond: 0
}
```

This is ideal for schedules, business hours, or recurring daily events.

### `PlainDateTime`

`PlainDateTime` combines a date and a time—still with **no timezone**.

```js
const dateTime = "2022-09-10T13:55:14";
// or an object with date + time fields

const dateTimeNow = Temporal.PlainDateTime.from(dateTime);
```

It contains the combined fields you’d expect from `PlainDate` and `PlainTime` together.

This is useful when the *local date and time matter*, but the absolute instant does not.

### `ZonedDateTime`

Notice that this type is **not** prefixed with `Plain`.

`ZonedDateTime` represents a specific moment in time *at a specific location*, which means it **can** be converted to epoch values.

```js
const hereAndNow = {
  year: 2020,
  month: 9,
  day: 10,
  hour: 13,
  minute: 55,
  second: 14,
  timeZone: "America/New_York"
};

const zonedDateTime = Temporal.ZonedDateTime.from(hereAndNow);
```

This produces a very rich object:

```js
{
  year: 2020,
  month: 9,
  day: 10,
  hour: 13,
  minute: 55,
  second: 14,
  timeZone: { id: "America/New_York" },
  offset: "-04:00",
  epochMilliseconds: 1599760514000,
  epochNanoseconds: 1599760514000000000n,
  inLeapYear: true,
  weekOfYear: 37
}
```

This is the Temporal type you’ll most often use when persisting timestamps to a database or interacting with external systems.

### `Instant`

An `Instant` represents **a single, absolute moment in time**, independent of timezone or calendar.

It can be created from:

* an ISO string with a timezone, or
* epoch milliseconds / microseconds / nanoseconds

```js
const todayString = "2022-09-10T13:55Z";
const todayMilliseconds = 1662818100000;

const fromString = Temporal.Instant.from(todayString);
const fromMilliseconds =
  Temporal.Instant.fromEpochMilliseconds(todayMilliseconds);
```

Both produce the same result:

```js
{
  epochSeconds: 1662818100,
  epochMilliseconds: 1662818100000,
  epochMicroseconds: 1662818100000000n,
  epochNanoseconds: 1662818100000000000n
}
```

`Instant` is the Temporal equivalent of a raw timestamp.

## Coercion between Temporal types

This was the **most confusing part** of Temporal for me—and the main reason I’m writing this article.

The question I kept running into was:

> *How do I take epoch milliseconds from the database and turn them into usable Temporal objects?*

The answer lies in **`to`** and **`with`** methods.

### From epoch milliseconds → Temporal types

Let’s say your database stores a UTC timestamp:

```js
const createdAt = 1662818100000;
```

Step 1: Convert it to an `Instant`.

```js
const createdAtInstant =
  Temporal.Instant.fromEpochMilliseconds(createdAt);
```

Step 2: Convert the `Instant` to a `ZonedDateTime` by supplying a timezone.

```js
const tz = "America/New_York";

const zonedCreatedAt = createdAtInstant.toZonedDateTime({
  timeZone: tz,
  calendar: "iso8601"
});
```

Now you have a fully qualified Temporal object tied to a location.

From here, you can easily derive other Temporal types:

```js
const plainDate = zonedCreatedAt.toPlainDate();
const plainTime = zonedCreatedAt.toPlainTime();
const plainDateTime = zonedCreatedAt.toPlainDateTime();
```

This explicit conversion chain is intentional—and far safer than the implicit timezone behavior of `Date`.

## Conclusion

This article is meant as a **practical primer**, not a complete guide.

Temporal has many more features:

* duration arithmetic
* calendar conversions
* precise rounding
* safe timezone handling

But even at a basic level, it offers something legacy `Date` never did:
**clear, explicit representations of time.**

Once you internalize the difference between `Plain`, `Zoned`, and `Instant`, Temporal starts to feel less magical—and a lot more trustworthy.

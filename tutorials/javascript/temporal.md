---
slug: temporal-datetime
title: "Temporal Datetime API"
authors: Aaron Wolf
sidebar_position: 5
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---


We all know that dates in JavaScript suck. Temporal is the API that we will come to succeed the legacy date API in JavaScript. This post is about my experience with the new [Temporal API](https://tc39.es/proposal-temporal/). 

At the moment (no pun intended), Temporal is still in stage 3 (out of 4) of development. This means that it should not be used in development, but if you're curious on how to use it you can still use the [Temporal polyfill](https://www.npmjs.com/package/@js-temporal/polyfill).


The reason why I'm writing this- despite there being a plethora of other tutorials- is because I haven't seen others showcase how Temporal might be used in the real world. However, this is not a comprehensive overview of the entire API. 

# The paradigm shift

In order to understand Temporal dates one must think about dates differently. In Legacy JavaScript dates are ultimately wrappers for epoch milliseconds. While Temporal dates _can_ do this, they are not necessarily this. This means that you can have a Temporal Date object (or a time object) that is completely divorced from epoch milliseconds. 

# Most common use cases (for me at least)

As far as I understand the naming convention, anything that begins with `Plain` is disconnected from epoch milliseconds.

### `PlainDate`
One can create a plain date like so:

input:
```javascript
// today can be an ISO string or an object
const today = '2022-09-10'
// or 
// const today = { year: 2022, month: 9, day: 10 }
const temporalToday = Temporal.PlainDate.from(today)
```

`temporalToday` is an object with the following characteristics:

```javascript
{
  calendar: Calendar {
    id: 'iso8601'},
  day: 10,
  dayOfWeek: 6,
  dayOfYear: 253,
  daysInMonth: 30,
  daysInWeek: 7,
  daysInYear: 365,
  era: undefined,
  eraYear: undefined,
  inLeapYear: false,
  month: 9,
  monthCode: "M09",
  monthsInYear: 12,
  weekOfYear: 36,
  year: 2022
}
```

You can see that this provides a lot more information that simply the year, month, and date. Also, it's implied that the preferred calendar is iso8601, but there are other calendars that can be used, such as the Jewish or Chinese calendars.

### `PlainTime`

Similar to `PlainDate` if the following is instantiated:

```javascript
const time = '13:55:14'
const plainTimeNow = Temporal.PlainTime.from(time)
```

The following object will be returned:

```javascript
{
  calendar: Calendar {
    id: 'iso8601'},
  hour: 13,
  microsecond: 0,
  millisecond: 0,
  minute: 55,
  nanosecond: 0,
  second: 14
}
```

### `PlainDateTime`

Like `PlainDate` and `PlainTime`, this returns an object, but with the attributes of both of them together. Remember that the input must be in ISO format or an object.

```javascript
const dateTime = '2022-09-10T13:55:14'
// or
// const dateTime = {
//   year: 2022,
//   month: 9,
//   day: 10,
//   hour: 13,
//   minute: 55,
//   second: 14
// }

const dateTimeNow = Temporal.PlainDateTime.from(dateTime)
```

```javascript
{
  ...
  day: 10
  dayOfWeek: 6
  dayOfYear: 253,
  daysInMonth: 30,
  daysInWeek: 7,
  daysInYear: 365,
  era: undefined,
  eraYear: undefined,
  hour: 13,
  inLeapYear: false,
  microsecond: 0,
  millisecond: 0,
  minute: 55,
  month: 9,
  monthCode: "M09",
  monthsInYear: 12,
  nanosecond: 0,
  second: 14,
  weekOfYear: 36,
  year: 2022
}
```

This is pretty self explanatory once the previous 2 sections are understood.

### `ZonedDateTime`

Notice that `ZonedDateTime` isn't preceded by the work "plain". This is because there is a full time _and_ location, and therefore epoch milliseconds can be calculated. 

Note that only an object or [epoch nanoseconds](https://tc39.es/proposal-temporal/docs/zoneddatetime.html#new-Temporal-ZonedDateTime) can be passed into `ZonedDateTime`. I don't have a sample of using epoch nanoseconds since it's outside of my use case. 

```javascript
const hereAndNow = {
  year: 2020,
  month: 9,
  day: 10,
  hour: 13,
  minute: 55,
  second: 14,
  timeZone: 'America/New_York'
}
const zonedDateTime = Temporal.ZonedDateTime.from(hereAndNow)
```

This will produce:
```javascript
{
  day: 10,
  dayOfWeek: 4,
  dayOfYear: 254,
  daysInMonth: 30,
  daysInWeek: 7,
  daysInYear: 366,
  epochMicroseconds: 1599760514000000n,
  epochMilliseconds: 1599760514000,
  epochNanoseconds: 1599760514000000000n,
  epochSeconds: 1599760514,
  era: undefined,
  eraYear: undefined,
  hour: 13,
  hoursInDay: 24,
  inLeapYear: true,
  microsecond: 0,
  millisecond: 0,
  minute: 55,
  month: 9,
  monthCode: "M09",
  monthsInYear: 12,
  nanosecond: 0,
  offset: "-04:00",
  offsetNanoseconds: -14400000000000,
  second: 14,
  timeZone: {
    id: "America/New_York",
  },
  weekOfYear: 37,
  year: 2020,
}
```

Look at all those attributes available to us! Notice that the `epochMilliseconds` are there along with `epochMircoseconds` and others. 

This makes saving this information to the database extremely easy.

### `Instant`

`Instant` can be instantiated from _either_ a date string, or a number. The number can be epoch milliseconds, nanoseconds, or microseconds. Since I work with epoch milliseconds, that's what I'll show. Assume my timezone is UTC right now.

```javascript
const todayString = '2022-09-10T13:55Z'
const todayMilliseconds = 1662818100000
```

Note: There is an added `Z` at the end of the string date to denote the timezone. 

There's also a slight difference to how one interacts with the two different types of dates.

Note: Objects cannot be passed in as an argument the way we did above with the `Plain` Temporal objects.

```javascript
const fromString = Temporal.Instant.from(todayString)
const fromMilliseconds = 
  Temporal.Instant.fromEpochMilliseconds(todayMilliseconds)
```

Both of these are the same date so they will output the same information.

```javascript 
{
  epochMicroseconds: 1662818100000000n
  epochMilliseconds: 1662818100000
  epochNanoseconds: 1662818100000000000n
  epochSeconds: 1662818100
}
```

# Coercion

The biggest frustration I had was figuring out how to coerce a `Plain` object into an `Instant` and vice versa. **This section is the reason I'm writing this piece**.

The problem I encountered was **how do I read epochMilliseconds and coerce them into other Temporal types?** 

The answer! `with` and `to`.

Let's say I had a value in the db called `createdAt` (really clever, I know) which is stored as a UTC timestamp. How could this be coerced into a Temporal object (PlainTime, PlainDate, or PlainDateTime)?

The first step is to convert that into a `ZonedDateTime`. But before doing that a timezone is required. For this I'm going to use my local timezone.

```javascript
const myTZ = Temporal.timezone.from('America/New_York')
const createdAt = 1662818100000
const createdAtInstant = 
  Temporal.Instant.fromEpochMilliseconds(createdAt)
const zonedCreatedAt = createdAtInstant.toZonedDateTime({
  timeZone: tz,
  calendar: 'iso8601'
})
```

It's a bit much, but now `zonedCreatedAt` is a Temporal `ZonedDateTime` created from an instant that was created from an epoch millisecond timestamp. 

If you wanted to convert the above to another Temporal type `toPlainDate` and `toPlainTime` can be used on `zonedCreatedAt`.

# Conclusion 
This was a bit of a primer. If you go through the documentation there are other ways to do some of the things I showed above and there are more details to know.
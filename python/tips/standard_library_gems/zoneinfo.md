---
title: `zoneinfo`
sidebar_position: 23
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`zoneinfo` gives Python first-class time zone support from the standard library. It is the right tool when your code needs real named time zones instead of fixed UTC offsets.

## Why it is useful

```python
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(2026, 1, 1, 12, 0, tzinfo=ZoneInfo("America/New_York"))
print(dt.tzinfo)
```

Named zones matter because daylight saving rules and local offsets change over time.

## Good use cases

- calendars
- scheduled jobs
- user-facing timestamps
- converting between regions

## One important detail

Prefer named zones like `"America/New_York"` over hardcoded offsets when the time is tied to a real place.

## Rules of thumb

- Use `zoneinfo` for real time zone handling.
- Prefer named zones over fixed offsets for user-local time.
- Reach for it whenever daylight saving behavior matters.

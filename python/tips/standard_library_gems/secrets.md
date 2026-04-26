---
title: `secrets`
sidebar_position: 13
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Use `secrets` when generating tokens, passwords, or anything security-sensitive. It is designed for cryptographically strong randomness, unlike `random`.

## Why it is useful

This is the right kind of code for tokens:

```python
import secrets

token = secrets.token_urlsafe(16)
print(token)
```

`random` is fine for simulations and simple games, but not for security-sensitive values.

## Good use cases

- password reset tokens
- API keys
- invite codes
- secret values in tests that should be hard to guess

## Rules of thumb

- Use `secrets`, not `random`, for tokens and passwords.
- Reach for `token_urlsafe()` when the value will appear in URLs.
- Treat secure randomness as a separate requirement from ordinary randomness.

---
title: Separate configuration
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

# Keep configuration separate from code

Configuration answers questions like "which database should this use?" or "which port should this run on?" Keeping those choices separate from business logic makes code easier to reuse, test, and deploy.

## Why this matters

Hardcoded settings spread quickly:

```python
def connect_to_database() -> None:
    host = "localhost"
    port = 5432
    debug = True
```

This is manageable at first, but it creates friction later:

- tests need different settings
- staging and production need different values
- local development needs overrides
- configuration changes require code edits

## Keep settings in one place

A better pattern is to load configuration once and pass it where it is needed:

```python
from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    db_host: str
    db_port: int
    debug: bool


def load_config() -> AppConfig:
    return AppConfig(
        db_host=os.getenv("DB_HOST", "localhost"),
        db_port=int(os.getenv("DB_PORT", "5432")),
        debug=os.getenv("DEBUG", "false").lower() == "true",
    )
```

Now the rest of the code can depend on `AppConfig` instead of reading environment variables all over the program.

## Separate configuration from logic

This division makes code cleaner:

- configuration code decides values
- application code uses those values

For example:

```python
def start_server(config: AppConfig) -> None:
    print(f"Starting on {config.db_host}:{config.db_port}")
```

That function is easier to test because the configuration arrives as an argument instead of being fetched implicitly.

## Good configuration sources

Common choices include:

- environment variables
- config files such as JSON, TOML, or YAML
- small config objects passed through the program

The exact source matters less than the separation. The important part is to avoid scattering settings across unrelated modules.

## Rules of thumb

- Load configuration near program startup.
- Store configuration in one clear structure.
- Pass config into code instead of reading global settings everywhere.
- Avoid hardcoding values that differ between environments.

# Vinyl Record Library Tracker

This is the final capstone project for the Python guides: a terminal app for cataloging, editing, selling, analyzing, and saving a personal vinyl record collection.

The goal of this project is not just to be a CRUD app. It is meant to bring together as many guide concepts as possible in one codebase, with a simple main workflow and richer secondary modules.

## Covered concepts

The project now includes examples of:

- variables, types, operators, and truthiness
- lists, dictionaries, sets, tuples, and ranges
- conditionals, `for` loops, and `while` loops
- functions, return values, and type hints
- `*args` and `**kwargs`
- lambdas and higher-order functions
- classes, instances, dataclasses, inheritance, and polymorphism
- encapsulation, properties, class methods, and static methods
- dunder methods such as `__post_init__`, `__len__`, `__iter__`, `__contains__`, `__getitem__`, and `__str__`
- decorators
- file handling, JSON, exceptions, modules, and `datetime`

## Features

- View all records in the collection
- Add a new record
- Edit an existing record
- Sell a record and track sales history
- Search records by artist
- Filter records by genre
- View collection stats
- View sales history
- View a capstone analytics report
- Save and load the collection to and from JSON

## Files

- `app.py`: the main entry point and menu loop
- `actions.py`: user actions such as add, edit, sell, search, reports, and save
- `analytics.py`: higher-order helpers and report-building utilities
- `decorators.py`: reusable decorators for action banners and collection guards
- `models.py`: dataclasses, inheritance, properties, dunder methods, and collection logic
- `prompts.py`: input helpers, update helpers, and date prompts
- `storage.py`: JSON loading and saving
- `ui.py`: menus, rendering, stats, and capstone report output
- `sample_records.json`: starter data

## Run the project

From the `final_project` directory:

```bash
python3 app.py
```

Or from the repository root:

```bash
python3 docs/python/guides/final_project/app.py
```

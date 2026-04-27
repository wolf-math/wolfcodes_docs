# Vinyl Record Library Tracker

This is the final project for the Python guides: a small terminal app for cataloging a personal vinyl record collection.

The project brings together the concepts introduced across the guide series:

- variables and types
- lists, dictionaries, and sets
- conditionals and loops
- functions
- classes and dataclasses
- file handling and JSON
- exceptions
- modules

## Features

- View all records in the collection
- Add a new record
- Search records by artist
- Filter records by genre
- View collection stats
- Save the collection to JSON
- Load the collection from JSON

## Files

- `app.py`: the main entry point and menu loop
- `actions.py`: user actions such as add, edit, sell, search, and save
- `models.py`: dataclasses and collection logic
- `prompts.py`: input and record-selection helpers
- `storage.py`: JSON loading and saving
- `ui.py`: printing menus, records, and stats
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

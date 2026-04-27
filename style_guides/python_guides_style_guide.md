---
title: Python Guides Style Guide
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Python guides style guide

Use this guide when revising pages in `docs/python/guides`.

This guide extends [master guide style](/Users/aaron/code/wolf_codes/docs/style_guides/master_guides_style.md). When this guide is more specific, use it for Python guides. When it is silent, follow the master guide.

The Python guides are already in strong shape. This guide is not a mandate to rewrite them from scratch. It is a framework for making targeted, incremental updates so the section gains a clearer shared arc without losing the strengths of the existing pages.

The Python guides are not just a collection of isolated lessons. They are a connected learning path built around one evolving project. Each guide must still stand on its own, but across the whole section the reader should feel a steadier sense of progression after revisions.

## Core idea

Write the Python guides like a season of a good procedural show:

- Each episode solves one clear problem.
- A larger story continues in the background.
- A reader can jump into one episode and still follow it.
- A reader who stays for the full season feels the project grow in a satisfying way.

For the current Python guides, the shared project should be a **vinyl record library tracker** built in Python.

That project is the recurring thread that connects the guides. It gives continuity to future revisions, a coherent structure for companion videos, and a practical reason for each new Python feature.

This does **not** mean every guide must be rebuilt around the project. It means revisions should gently align examples, transitions, and project applications where that improves continuity.

## Canonical project reference

The canonical implementation of the shared project lives in:

- `docs/python/guides/final_project`

Use that directory as the concrete reference point for guide revisions, examples, terminology, and project continuity.

That means:

- The style guide is referring to the real final project in `final_project`, not to a hypothetical version of it.
- Guide examples should align with the data model, naming, and domain of that project whenever practical.
- When choosing example fields, record attributes, helper function names, or class names, prefer the names already used in the final project unless there is a clear teaching reason to simplify or vary them.
- If the final project evolves, the guides and this style guide should evolve with it.

The final project is the shared source of truth for the project world used across the Python guides.

## Revision-first principle

Treat this guide as an **editing guide**, not a blank-page content spec.

When updating an existing guide:

- Preserve explanations that are already clear and effective.
- Keep the current structure when it already serves the topic well.
- Add project continuity through small, deliberate changes.
- Prefer tightening, adding, or reshaping sections over replacing the entire page.
- Rewrite only when a section is genuinely weak, confusing, or mismatched with the current quality bar.

The goal is to improve cohesion across the guide set, not to erase the voice and work already present.

## Goals of the guides

Each guide should do all of the following:

- Teach one Python concept clearly.
- Show a small example that stands alone.
- Connect that concept to the vinyl tracker project.
- Move the larger project forward by one meaningful step.
- Leave the reader with a useful, working mental model.

The page should never depend on the reader having finished previous guides. The progression is cumulative at the section level, not required at the page level.

In revision work, this usually means adding missing connective tissue rather than rebuilding the lesson from the ground up.

Across the full section, the guides should cumulatively explain the ideas that are eventually present in `docs/python/guides/final_project`.

## The project arc

The shared project is a terminal-based vinyl record library tracker. Over time, the reader learns how to:

- Represent one record with basic values
- Store multiple records in collections
- Search, filter, and summarize a collection
- Extract repeated logic into functions
- Model records and collections with classes
- Use dataclasses for data-focused objects
- Save and load the collection with files and JSON
- Handle invalid input and runtime errors
- Split larger code into modules

This is the end state. Individual guides should only build one layer at a time, and revisions should only introduce the amount of project context that the existing page can support cleanly.

The long-term goal is for the final project to reflect nearly all major guide concepts except foundational environment topics such as REPL vs. script and how Python runs code.

## Project rules

To keep the project useful and teachable, follow these rules:

- Keep the scope intentionally small. This is a personal collection tool, not Discogs.
- Prefer realistic fields: `title`, `artist`, `year`, `genre`, `condition`, `purchase_price`, `estimated_value`, `notes`.
- Use a terminal app mindset throughout. Avoid web framework or database assumptions.
- Introduce only the minimum project complexity needed to teach the concept.
- Do not force every guide to touch the project if the connection would feel artificial, but most guides should include a short project application.
- Prefer examples, names, and structures that can plausibly map back to `docs/python/guides/final_project`.

When revising an existing guide, a brief paragraph, one example, or one short section is often enough to create the connection.

## Progression from guide to guide

The section should feel like a sequence of increasingly capable versions of the same app.

Use this progression model:

1. Start with one record.
2. Move to multiple records.
3. Add decisions and repetition.
4. Extract reusable behavior.
5. Introduce richer data modeling.
6. Persist the data.
7. Make the program more robust and better organized.

In practice, that means concepts should generally map like this:

- Intro guides: run Python, print output, experiment in the REPL, create the first tiny record examples.
- Types and variables: store record fields and compare values.
- Data structures: represent collections of records and their metadata.
- Control flow: browse the collection, filter records, validate choices.
- Functions: extract tasks like `add_record()`, `find_by_artist()`, and `total_collection_value()`.
- OOP: create `Record`, `Collection`, and related models.
- Standard library: save, load, and protect the app from bad input or missing files.

This progression should feel natural, not mechanical. Each page should unlock one new capability in the imaginary app.

Use this progression to guide updates across the set. Do not pause on one page and try to force all of the continuity work into it.

## Standalone page rule

Every guide must be readable on its own.

That means:

- Define the concept as if the reader has not seen the earlier project chapters.
- Include a concept-first example before relying on the project example.
- Restate enough project context to make the vinyl example understandable.
- Avoid phrases like "as we built earlier" unless you immediately summarize the needed context.
- Do not require a shared codebase across pages.

Think of the project as a recurring teaching context, not as a prerequisite.

For existing guides, this often means adding a little more context around examples and transitions, not replacing the underlying lesson.

Standalone does **not** mean domain-neutral. A guide can stand alone while still using examples that belong to the same shared project world.

## Recommended page shape

Most Python guide pages should follow this pattern:

1. Frontmatter
2. `## What is/are [concept]?`
3. `## Why this matters` when motivation is useful
4. A smallest standalone example
5. Explanation of the behavior
6. One or more practical variations
7. A short vinyl tracker application section
8. Important gotchas or best practices
9. `## Summary` for longer pages

This is a guide pattern, not a rigid template. Short pages can be lighter. More technical pages can use more specific task-based headings.

Existing pages do not need to be rearranged to match this outline exactly. Use it as a target for gradual alignment.

## Required teaching pattern

For most pages, teach in this order:

1. The concept in isolation
2. The Python syntax or behavior
3. The mental model
4. The vinyl tracker application
5. The practical takeaway

This ordering matters. The guide should not open with project complexity if a simpler example would teach the concept better.

If an existing guide already teaches clearly in a slightly different order, keep that order unless changing it would clearly improve the page.

## The vinyl application section

Most guides should include a short section that applies the concept to the shared project.

Good heading patterns:

- `## In the vinyl tracker`
- `## Applying this to the record library`
- `## Using this in our project`

This section should:

- Use the same concept already taught on the page
- Add only one new layer of app behavior
- Stay short and concrete
- Feel like a meaningful feature, not filler

Good examples:

- Variables: store a record title, artist, and purchase price
- Lists: store multiple owned records
- Dictionaries: track record metadata
- Conditionals: check whether a record is already owned or whether its condition is poor
- Functions: create `add_record()` or `find_records_by_genre()`
- Dataclasses: define a `Record` model
- JSON: save the collection to a file

For revision work, this can be a light-touch addition. A guide does not need a large new section if a short applied example achieves the same goal.

## Shared example world

All code examples in the Python guides should live within the scope of the final project world, even when the example is small and self-contained.

That means example values, names, and tiny snippets should usually point back to music, records, artists, collecting, listening, cataloging, or related personal-library ideas.

Use examples like:

- `record_title = "Electric Ladyland"`
- `artist = "Jimi Hendrix"`
- `genres = ["psychedelic rock", "blues rock"]`
- `wishlist = ["Blue Train", "Giant Steps"]`
- `username = "JimiHendrix"`
- `hobbies = ["playing guitar", "collecting vinyl", "crate digging"]`

This rule applies even when the snippet is only teaching a basic concept like variables, lists, strings, loops, or functions.

The goal is for the entire guide set to feel like it belongs to one coherent project and one coherent creative world.

Whenever possible, examples should feel like smaller slices, earlier drafts, or simplified cousins of the code and data shapes used in `docs/python/guides/final_project`.

## Example domain guidance

When choosing example values, prefer:

- musicians
- bands
- albums
- songs
- genres
- record labels
- playlists
- collecting habits
- shelves, crates, and wishlists
- record condition, purchase price, and collection value

Good examples:

```python
username = "JimiHendrix"
hobbies = ["playing guitar", "collecting vinyl", "crate digging"]
```

```python
favorite_albums = ["Are You Experienced", "Kind of Blue", "Blue Train"]
```

```python
record = {
    "title": "Rumours",
    "artist": "Fleetwood Mac",
    "year": 1977,
}
```

Avoid examples that feel disconnected from the project world unless the concept truly requires a more neutral example.

Less preferred:

```python
name = "Alice"
age = 30
favorite_color = "blue"
```

If a neutral example is dramatically clearer for a specific teaching moment, it is allowed, but that should be the exception rather than the default.

If there is a choice between:

- a generic example that could belong to any tutorial
- and an equally clear example that resembles the final project

choose the example that resembles the final project.

## Voice and tone

The tone should be:

- Friendly
- Calm
- Practical
- Encouraging
- Clear enough for beginners
- Concrete enough for readers who want to build something real

Write like a patient teacher who respects the learner's intelligence.

Prefer:

- Plain-language definitions
- Small examples
- Direct explanations of what Python is doing
- Practical reasons a learner would use the concept
- Consistent music- and vinyl-themed example values

Avoid:

- Overly academic phrasing
- Jokes that distract from the lesson
- Excessive hype
- Dense walls of text
- Treating beginner questions as obvious

## Writing style

Use these habits consistently:

- Prefer short paragraphs.
- Use examples early.
- Explain unfamiliar terms immediately.
- Name common mistakes before they become confusing.
- Use beginner-readable variable names.
- Prefer concrete domain values over placeholders when the example benefits from it.
- Keep example names and values inside the shared music/vinyl project world whenever practical.
- Use the final project as the preferred source for recurring names, entities, and example shapes.

When the shared project appears, use names like:

- `record`
- `records`
- `collection`
- `wishlist`
- `artist`
- `genre`
- `condition`
- `purchase_price`
- `album`
- `artist_name`
- `favorite_albums`
- `record_title`

Avoid domain details that require specialized music knowledge unless they directly help the example.

When editing existing pages, preserve examples that are already working well unless the vinyl project connection would add clear value.

## Example style

Examples should be:

- Small enough to read quickly
- Complete enough to understand without hidden setup
- Focused on one lesson
- Written in valid modern Python
- Grounded in the shared music and vinyl project world

When a project example would become too large, reduce it. Do not let the running project make examples bulky.

Prefer:

```python
record = {
    "title": "Kind of Blue",
    "artist": "Miles Davis",
    "year": 1959,
}
```

Over:

```python
record = {
    "title": "Kind of Blue",
    "artist": "Miles Davis",
    "year": 1959,
    "genre": "Jazz",
    "label": "Columbia",
    "catalog_number": "CL 1355",
    "pressing_country": "US",
    "purchase_price": 24.99,
    "estimated_value": 40.00,
    "condition": "VG+",
    "notes": "First mono pressing with sleeve wear",
}
```

Use richer examples only when the extra fields help teach the concept.

Do not replace simple existing examples with project examples unless the page becomes better as a result.

But when a simple example can be swapped for an equally clear music-themed one, prefer the music-themed version.

## Explanations after examples

After important examples, explain behavior right away.

Useful labels:

- `**What happens:**`
- `**Why this works:**`
- `**Important:**`
- `**Rule of thumb:**`

Use short lists when they make behavior easier to scan.

## Choosing project detail

Each page should introduce only the amount of project detail that the concept can support.

Good escalation:

- Early pages: one record, a few fields
- Mid-level pages: lists, dictionaries, filtering, totals
- Later pages: reusable functions, classes, persistence

Bad escalation:

- Introducing classes before the class guides
- Using nested data structures before the reader has learned the simpler forms
- Showing a full application menu in a page that is really about strings or booleans

In practice, revision work should usually mean adding one small applied example, one brief note, or one new subsection rather than expanding the page dramatically.

## Companion video alignment

These guides are designed to support a long master video that is later split into per-guide sections.

Write pages so they map cleanly to a video chapter.

Each guide should correspond to a chapter with:

- One concept focus
- One small project milestone
- One satisfying payoff by the end

The docs and video should reinforce each other, but neither should depend on the other to be understandable.

That alignment can emerge through revision. It does not require every page to be reauthored from the beginning.

## Video-friendly doc pattern

When shaping a guide, imagine it as one segment in the larger recording:

1. Briefly introduce the concept
2. Show the smallest example
3. Explain what is happening
4. Apply it to the vinyl tracker
5. End with a concrete result

This makes it easier to record one continuous build while still cutting the footage into useful standalone sections.

## Section endings

Guide endings should create a gentle sense of momentum.

Good endings:

- Summarize what the reader can now do
- Reinforce the project feature they just added
- Briefly hint at the next kind of problem Python will help solve

Avoid endings that make the page sound incomplete or dependent on another page.

## What to avoid

Do not:

- Turn the guides into a strict step-by-step tutorial that breaks if one page is skipped
- Let the project story overshadow the Python concept
- Add unnecessary complexity just to preserve narrative continuity
- Make every example use the vinyl domain when a simpler generic example teaches better
- Refer to a hidden shared file structure unless the page explicitly shows it
- Assume the reader watched the video
- Treat the existing guides as disposable source material
- Rewrite a page purely for consistency when the current version already teaches well

## Quality bar

A strong Python guide page should let a reader say:

- I understand this Python concept.
- I saw a simple example first.
- I saw how it fits into a real project.
- I could use this page without reading the others.
- If I read the whole series, I would feel the project growing.

That is the target.

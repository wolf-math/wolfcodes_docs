from pathlib import Path

from models import RecordCollection
from prompts import (
    choose_record_index,
    prompt_for_new_record,
    prompt_for_updated_record,
)
from storage import load_collection, save_collection, seed_collection
from ui import display_collection, display_stats, print_records


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sample_records.json"
COLLECTION_NAME = "Vinyl Record Library"


def view_records(collection: RecordCollection) -> None:
    display_collection(collection)


def add_record(collection: RecordCollection) -> None:
    print("\nAdd a record")
    print("------------")

    try:
        record = prompt_for_new_record()
    except ValueError as error:
        print(f"Could not add record: {error}")
        return

    collection.add_record(record)
    print(f"Added {record.title} by {record.artist}.")


def edit_record(collection: RecordCollection) -> None:
    index = choose_record_index(collection, "edit")
    if index is None:
        return

    current_record = collection.get_record(index)

    print("\nEdit record")
    print("-----------")
    print("Press Enter to keep the current value.")

    try:
        updated_record = prompt_for_updated_record(current_record)
    except ValueError as error:
        print(f"Could not update record: {error}")
        return

    collection.update_record(index, updated_record)
    print(f"Updated {updated_record.title} by {updated_record.artist}.")


def sell_record(collection: RecordCollection) -> None:
    index = choose_record_index(collection, "sell")
    if index is None:
        return

    record = collection.get_record(index)
    confirmation = input(
        f"Sell {record.title} by {record.artist}? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Sale canceled.")
        return

    sold_record = collection.sell_record(index)
    print(f"Sold {sold_record.title} by {sold_record.artist}.")


def search_by_artist(collection: RecordCollection) -> None:
    artist_name = input("\nSearch for artist: ").strip()
    results = collection.find_by_artist(artist_name)
    print_records(results)


def filter_by_genre(collection: RecordCollection) -> None:
    genre_name = input("\nFilter by genre: ").strip()
    results = collection.filter_by_genre(genre_name)
    print_records(results)


def view_stats(collection: RecordCollection) -> None:
    display_stats(collection)


def save_records(collection: RecordCollection) -> None:
    try:
        save_collection(collection, str(DATA_FILE))
    except OSError as error:
        print(f"Could not save records: {error}")
        return

    print(f"Saved collection to {DATA_FILE.name}.")


def load_records() -> RecordCollection:
    try:
        return load_collection(str(DATA_FILE), COLLECTION_NAME)
    except FileNotFoundError:
        print("No existing collection file found. Starting with an empty library.")
    except (OSError, ValueError) as error:
        print(f"Could not load collection: {error}")

    return seed_collection(COLLECTION_NAME, [])

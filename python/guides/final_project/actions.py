from pathlib import Path

from decorators import action_banner, require_owned_records
from models import RecordCollection
from prompts import (
    choose_record_index,
    prompt_for_new_record,
    prompt_for_sale_details,
    prompt_for_updated_record,
)
from storage import load_collection, save_collection, seed_collection
from ui import (
    display_capstone_report,
    display_collection,
    display_sales_history,
    display_stats,
    print_items,
)


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sample_records.json"
COLLECTION_NAME = "Vinyl Record Library"


def view_records(collection: RecordCollection) -> None:
    display_collection(collection)


@action_banner("Add a record")
def add_record(collection: RecordCollection) -> None:
    try:
        record = prompt_for_new_record()
    except ValueError as error:
        print(f"Could not add record: {error}")
        return

    collection.add_record(record)
    print(f"Added {record.title} by {record.artist}.")


@action_banner("Edit record")
@require_owned_records("edit")
def edit_record(collection: RecordCollection) -> None:
    print("Press Enter to keep the current value.")
    index = choose_record_index(collection, "edit")
    if index is None:
        return

    current_record = collection.get_record(index)

    try:
        updated_record = prompt_for_updated_record(current_record)
    except ValueError as error:
        print(f"Could not update record: {error}")
        return

    collection.update_record(index, updated_record)
    print(f"Updated {updated_record.title} by {updated_record.artist}.")


@action_banner("Sell a record")
@require_owned_records("sell")
def sell_record(collection: RecordCollection) -> None:
    index = choose_record_index(collection, "sell")
    if index is None:
        return

    record = collection.get_record(index)

    try:
        sold_price, sold_on = prompt_for_sale_details()
    except ValueError as error:
        print(f"Could not record the sale: {error}")
        return

    confirmation = input(
        f"Sell {record.title} by {record.artist}? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Sale canceled.")
        return

    sold_record = collection.sell_record(index, sold_price, sold_on)
    print(
        f"Sold {sold_record.title} for "
        f"${sold_record.sold_price:.2f} on {sold_record.sold_on.isoformat()}."
    )


@action_banner("Search by artist")
def search_by_artist(collection: RecordCollection) -> None:
    artist_name = input("Search for artist: ").strip()
    results = collection.find_by_artist(artist_name)
    ordered_results = sorted(results, key=lambda record: record.year)
    print_items(ordered_results)


@action_banner("Filter by genre")
def filter_by_genre(collection: RecordCollection) -> None:
    genre_name = input("Filter by genre: ").strip()
    results = collection.filter_by_genre(genre_name)
    ordered_results = sorted(results, key=lambda record: record.artist)
    print_items(ordered_results)


def view_stats(collection: RecordCollection) -> None:
    display_stats(collection)


def view_sales_history(collection: RecordCollection) -> None:
    display_sales_history(collection)


def view_capstone_report(collection: RecordCollection) -> None:
    display_capstone_report(collection)


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

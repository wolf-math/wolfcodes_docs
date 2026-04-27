from typing import List

from models import Record, RecordCollection


def format_money(amount: float) -> str:
    return f"${amount:.2f}"


def print_record(record: Record, index: int = 0) -> None:
    label = f"{index}. " if index else ""
    print(
        f"{label}{record.artist} - {record.title} "
        f"({record.year}) | {record.genre} | "
        f"Condition: {record.condition} | "
        f"Paid: {format_money(record.purchase_price)} | "
        f"Value: {format_money(record.estimated_value)}"
    )

    if record.notes:
        print(f"   Notes: {record.notes}")


def print_records(records: List[Record]) -> None:
    if not records:
        print("No records found.")
        return

    for index, record in enumerate(records, start=1):
        print_record(record, index=index)


def pause_for_menu() -> None:
    input("\nPress Enter to return to the main menu...")


def display_collection(collection: RecordCollection) -> None:
    print(f"\n{collection.name}")
    print("-" * len(collection.name))
    print_records(collection.records)


def display_stats(collection: RecordCollection) -> None:
    stats = collection.stats()
    print("\nCollection stats")
    print("----------------")
    print(f"Total records: {stats['total_records']}")
    print(f"Unique artists: {stats['unique_artists']}")
    print(f"Unique genres: {stats['unique_genres']}")
    print(
        "Total purchase price: "
        f"{format_money(stats['total_purchase_price'])}"
    )
    print(
        "Total estimated value: "
        f"{format_money(stats['total_estimated_value'])}"
    )


def print_menu() -> None:
    print("\nVinyl Record Library Tracker")
    print("----------------------------")
    print("1. View all records")
    print("2. Add a record")
    print("3. Edit a record")
    print("4. Sell a record")
    print("5. Search by artist")
    print("6. Filter by genre")
    print("7. View collection stats")
    print("8. Save collection")
    print("9. Quit")

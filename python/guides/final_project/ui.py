from typing import Sequence

from analytics import build_capstone_report
from models import LibraryItem, RecordCollection


def format_money(amount: float) -> str:
    return f"${amount:.2f}"


def print_item(item: LibraryItem, index: int = 0) -> None:
    label = f"{index}. " if index else ""
    print(f"{label}{item.summary()}")
    notes = getattr(item, "notes", "")
    if notes:
        print(f"   Notes: {notes}")


def print_items(items: Sequence[LibraryItem]) -> None:
    if not items:
        print("No records found.")
        return

    for index, item in enumerate(items, start=1):
        print_item(item, index=index)


def pause_for_menu() -> None:
    input("\nPress Enter to return to the main menu...")


def display_collection(collection: RecordCollection) -> None:
    print(f"\n{collection.name}")
    print("-" * len(collection.name))
    print_items(collection.records)


def display_sales_history(collection: RecordCollection) -> None:
    print("\nSales history")
    print("-------------")
    print_items(collection.sold_records)


def display_stats(collection: RecordCollection) -> None:
    stats = collection.stats()
    value_low, value_high = stats["value_range"]

    print("\nCollection stats")
    print("----------------")
    print(f"Total records: {stats['total_records']}")
    print(f"Sold records: {stats['sold_records']}")
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
    print(
        "Total profit from sales: "
        f"{format_money(stats['total_profit_from_sales'])}"
    )
    print(
        f"Estimated value range: {format_money(value_low)}"
        f" to {format_money(value_high)}"
    )


def display_capstone_report(collection: RecordCollection) -> None:
    report = build_capstone_report(collection)

    print("\nCapstone report")
    print("---------------")

    print("Top records by estimated value:")
    top_records = report["top_records"]
    if top_records:
        for record in top_records:
            print(f"- {record.title} by {record.artist}")
    else:
        print("- No owned records yet.")

    print("\nRecently added records:")
    recent_records = report["recent_records"]
    if recent_records:
        for record in recent_records:
            print(f"- {record.title} ({record.added_on.isoformat()})")
    else:
        print("- No owned records yet.")

    print("\nDecade breakdown:")
    decades = report["decades"]
    if decades:
        for decade_label, count in decades:
            print(f"- {decade_label}: {count}")
    else:
        print("- No decade data yet.")

    print("\nTop artists:")
    top_artists = report["top_artists"]
    if top_artists:
        for artist_name, count in top_artists:
            print(f"- {artist_name}: {count}")
    else:
        print("- No artist data yet.")

    print("\nExpensive purchases:")
    expensive_purchases = report["expensive_purchases"]
    if expensive_purchases:
        for record in expensive_purchases:
            print(
                f"- {record.title}: "
                f"{format_money(record.purchase_price)}"
            )
    else:
        print("- No purchases to compare yet.")

    print(
        "\nSold revenue: "
        f"{format_money(report['sold_revenue'])}"
    )
    print(
        "Sold profit: "
        f"{format_money(report['sold_profit'])}"
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
    print("8. View sales history")
    print("9. View capstone report")
    print("0. Save collection")
    print("X. Quit")

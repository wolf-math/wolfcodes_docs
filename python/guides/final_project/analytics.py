from __future__ import annotations

from typing import Callable, Dict, Iterable, List, Sequence

from models import LibraryItem, Record, RecordCollection, SoldRecord


DECADE_STARTS = tuple(range(1950, 2030, 10))


def select_items(
    items: Iterable[Record],
    predicate: Callable[[Record], bool],
) -> List[Record]:
    return list(filter(predicate, items))


def top_records_by_value(
    collection: RecordCollection,
    limit: int = 3,
) -> List[Record]:
    return collection.sort_records(
        key_function=lambda record: record.estimated_value,
        reverse=True,
    )[:limit]


def recently_added_records(
    collection: RecordCollection,
    limit: int = 3,
) -> List[Record]:
    return collection.sort_records(
        key_function=lambda record: record.added_on,
        reverse=True,
    )[:limit]


def records_in_decade(
    collection: RecordCollection,
    decade_start: int,
) -> List[Record]:
    return select_items(
        collection,
        lambda record: decade_start <= record.year < decade_start + 10,
    )


def decade_breakdown(
    collection: RecordCollection,
) -> tuple[tuple[str, int], ...]:
    breakdown = []

    for decade_start in DECADE_STARTS:
        matches = records_in_decade(collection, decade_start)
        if matches:
            breakdown.append((f"{decade_start}s", len(matches)))

    return tuple(breakdown)


def top_artists(
    collection: RecordCollection,
    limit: int = 3,
) -> tuple[tuple[str, int], ...]:
    artist_counts = [
        (
            artist,
            len(select_items(collection, lambda record: record.artist == artist)),
        )
        for artist in sorted(collection.unique_artists())
    ]

    ordered = sorted(artist_counts, key=lambda item: item[1], reverse=True)
    return tuple(ordered[:limit])


def expensive_purchases(collection: RecordCollection) -> List[Record]:
    average_price = (
        collection.total_purchase_price() / len(collection)
        if len(collection) > 0
        else 0.0
    )
    return select_items(
        collection,
        lambda record: record.purchase_price >= average_price,
    )


def total_sold_revenue(sold_records: Sequence[SoldRecord]) -> float:
    return sum(record.sold_price for record in sold_records)


def build_capstone_report(collection: RecordCollection) -> Dict[str, object]:
    return {
        "top_records": top_records_by_value(collection),
        "recent_records": recently_added_records(collection),
        "decades": decade_breakdown(collection),
        "top_artists": top_artists(collection),
        "expensive_purchases": expensive_purchases(collection),
        "sold_revenue": total_sold_revenue(collection.sold_records),
        "sold_profit": collection.total_profit_from_sales(),
    }


def item_summaries(items: Sequence[LibraryItem]) -> tuple[str, ...]:
    return tuple(item.summary() for item in items)

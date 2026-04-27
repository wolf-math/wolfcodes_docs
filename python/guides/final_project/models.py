from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Callable, Dict, Iterable, Iterator, List, Sequence, Set


VALID_CONDITIONS = {"Mint", "NM", "VG+", "VG", "G", "Fair", "Poor"}


@dataclass
class LibraryItem:
    title: str
    artist: str
    year: int
    genre: str

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("Title cannot be empty.")

        if not self.artist.strip():
            raise ValueError("Artist name cannot be empty.")

        if self.year < 1900:
            raise ValueError("Year must be 1900 or later.")

        if not self.genre.strip():
            raise ValueError("Genre cannot be empty.")

    @property
    def decade(self) -> str:
        decade_start = (self.year // 10) * 10
        return f"{decade_start}s"

    def summary(self) -> str:
        return f"{self.artist} - {self.title} ({self.year})"


@dataclass
class Record(LibraryItem):
    condition: str
    purchase_price: float
    estimated_value: float
    notes: str = ""
    added_on: date = field(default_factory=date.today)

    collection_type = "owned"
    condition_rank = {
        "Poor": 0,
        "Fair": 1,
        "G": 2,
        "VG": 3,
        "VG+": 4,
        "NM": 5,
        "Mint": 6,
    }

    def __post_init__(self) -> None:
        super().__post_init__()

        if isinstance(self.added_on, str):
            self.added_on = date.fromisoformat(self.added_on)

        if not self.is_valid_condition(self.condition):
            raise ValueError(
                "Condition must be one of: "
                + ", ".join(sorted(VALID_CONDITIONS))
            )

        if self.purchase_price < 0:
            raise ValueError("Purchase price cannot be negative.")

        if self.estimated_value < 0:
            raise ValueError("Estimated value cannot be negative.")

    @staticmethod
    def is_valid_condition(condition: str) -> bool:
        return condition in VALID_CONDITIONS

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Record:
        payload = dict(data)
        payload["added_on"] = payload.get("added_on", date.today().isoformat())
        return cls(**payload)

    @property
    def age(self) -> int:
        return date.today().year - self.year

    @property
    def is_profitable(self) -> bool:
        return self.estimated_value > self.purchase_price

    @property
    def display_condition(self) -> str:
        return self.condition.upper()

    def summary(self) -> str:
        return (
            f"{self.artist} - {self.title} ({self.year}) | {self.genre} | "
            f"Condition: {self.condition} | Paid: ${self.purchase_price:.2f} | "
            f"Value: ${self.estimated_value:.2f}"
        )

    def with_updates(self, **changes: Any) -> Record:
        payload = self.to_dict()
        payload.update(changes)
        return type(self).from_dict(payload)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "genre": self.genre,
            "condition": self.condition,
            "purchase_price": self.purchase_price,
            "estimated_value": self.estimated_value,
            "notes": self.notes,
            "added_on": self.added_on.isoformat(),
        }

    def __str__(self) -> str:
        return self.summary()


@dataclass
class SoldRecord(Record):
    sold_price: float = 0.0
    sold_on: date = field(default_factory=date.today)

    collection_type = "sold"

    def __post_init__(self) -> None:
        super().__post_init__()

        if isinstance(self.sold_on, str):
            self.sold_on = date.fromisoformat(self.sold_on)

        if self.sold_price < 0:
            raise ValueError("Sold price cannot be negative.")

    @classmethod
    def from_record(
        cls,
        record: Record,
        sold_price: float,
        sold_on: date | None = None,
    ) -> SoldRecord:
        return cls(
            title=record.title,
            artist=record.artist,
            year=record.year,
            genre=record.genre,
            condition=record.condition,
            purchase_price=record.purchase_price,
            estimated_value=record.estimated_value,
            notes=record.notes,
            added_on=record.added_on,
            sold_price=sold_price,
            sold_on=sold_on or date.today(),
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> SoldRecord:
        payload = dict(data)
        payload["added_on"] = payload.get("added_on", date.today().isoformat())
        payload["sold_on"] = payload.get("sold_on", date.today().isoformat())
        return cls(**payload)

    @property
    def profit(self) -> float:
        return self.sold_price - self.purchase_price

    def summary(self) -> str:
        return (
            f"{self.artist} - {self.title} ({self.year}) | Sold for "
            f"${self.sold_price:.2f} on {self.sold_on.isoformat()} | "
            f"Profit: ${self.profit:.2f}"
        )

    def to_dict(self) -> Dict[str, Any]:
        payload = super().to_dict()
        payload["sold_price"] = self.sold_price
        payload["sold_on"] = self.sold_on.isoformat()
        return payload


class RecordCollection:
    collection_label = "Vinyl Record Library"

    def __init__(
        self,
        name: str,
        records: Iterable[Record] | None = None,
        sold_records: Iterable[SoldRecord] | None = None,
    ) -> None:
        self.name = name
        self._records: List[Record] = list(records or [])
        self._sold_records: List[SoldRecord] = list(sold_records or [])

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> RecordCollection:
        name = data.get("name", cls.collection_label)
        records = [Record.from_dict(item) for item in data.get("records", [])]
        sold_records = [
            SoldRecord.from_dict(item)
            for item in data.get("sold_records", [])
        ]
        return cls(name=name, records=records, sold_records=sold_records)

    @property
    def records(self) -> tuple[Record, ...]:
        return tuple(self._records)

    @property
    def sold_records(self) -> tuple[SoldRecord, ...]:
        return tuple(self._sold_records)

    @staticmethod
    def matches_text(item: LibraryItem, search_term: str) -> bool:
        normalized = search_term.strip().lower()
        haystack = f"{item.title} {item.artist} {item.genre}".lower()
        return normalized in haystack

    def __len__(self) -> int:
        return len(self._records)

    def __iter__(self) -> Iterator[Record]:
        return iter(self._records)

    def __contains__(self, title_or_record: object) -> bool:
        if isinstance(title_or_record, Record):
            return any(record == title_or_record for record in self._records)

        if isinstance(title_or_record, str):
            title = title_or_record.strip().lower()
            return any(record.title.lower() == title for record in self._records)

        return False

    def __getitem__(self, index: int) -> Record:
        return self._records[index]

    def __str__(self) -> str:
        return f"{self.name} ({len(self)} records)"

    def add_record(self, record: Record) -> None:
        self._records.append(record)

    def add_records(self, *records: Record) -> None:
        self._records.extend(records)

    def record_count(self) -> int:
        return len(self._records)

    def sold_count(self) -> int:
        return len(self._sold_records)

    def get_record(self, index: int) -> Record:
        return self._records[index]

    def update_record(self, index: int, updated_record: Record) -> None:
        self._records[index] = updated_record

    def sell_record(
        self,
        index: int,
        sold_price: float,
        sold_on: date | None = None,
    ) -> SoldRecord:
        record = self._records.pop(index)
        sold_record = SoldRecord.from_record(record, sold_price, sold_on)
        self._sold_records.append(sold_record)
        return sold_record

    def _filter_records(
        self,
        predicate: Callable[[Record], bool],
    ) -> List[Record]:
        return [record for record in self._records if predicate(record)]

    def find_by_artist(self, artist_name: str) -> List[Record]:
        search_term = artist_name.strip().lower()
        return self._filter_records(
            lambda record: search_term in record.artist.lower()
        )

    def filter_by_genre(self, genre_name: str) -> List[Record]:
        search_term = genre_name.strip().lower()
        return self._filter_records(
            lambda record: search_term in record.genre.lower()
        )

    def sort_records(
        self,
        key_function: Callable[[Record], object],
        reverse: bool = False,
    ) -> List[Record]:
        return sorted(self._records, key=key_function, reverse=reverse)

    def total_purchase_price(self) -> float:
        return sum(record.purchase_price for record in self._records)

    def total_estimated_value(self) -> float:
        return sum(record.estimated_value for record in self._records)

    def total_profit_from_sales(self) -> float:
        return sum(record.profit for record in self._sold_records)

    def unique_artists(self) -> Set[str]:
        return {record.artist for record in self._records}

    def unique_genres(self) -> Set[str]:
        return {record.genre for record in self._records}

    def value_range(self) -> tuple[float, float]:
        if not self._records:
            return (0.0, 0.0)

        values = [record.estimated_value for record in self._records]
        return (min(values), max(values))

    def stats(self) -> Dict[str, object]:
        value_low, value_high = self.value_range()
        return {
            "total_records": len(self._records),
            "sold_records": len(self._sold_records),
            "total_purchase_price": self.total_purchase_price(),
            "total_estimated_value": self.total_estimated_value(),
            "total_profit_from_sales": self.total_profit_from_sales(),
            "unique_artists": len(self.unique_artists()),
            "unique_genres": len(self.unique_genres()),
            "value_range": (value_low, value_high),
        }

    def to_dict(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "records": [record.to_dict() for record in self._records],
            "sold_records": [
                record.to_dict() for record in self._sold_records
            ],
        }

    def to_dict_list(self) -> List[Dict[str, object]]:
        return [record.to_dict() for record in self._records]

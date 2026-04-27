from dataclasses import asdict, dataclass, field
from typing import Dict, List, Set


VALID_CONDITIONS = {"Mint", "NM", "VG+", "VG", "G", "Fair", "Poor"}


@dataclass
class Record:
    title: str
    artist: str
    year: int
    genre: str
    condition: str
    purchase_price: float
    estimated_value: float
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("Record title cannot be empty.")

        if not self.artist.strip():
            raise ValueError("Artist name cannot be empty.")

        if self.year < 1900:
            raise ValueError("Year must be 1900 or later.")

        if self.condition not in VALID_CONDITIONS:
            raise ValueError(
                "Condition must be one of: "
                + ", ".join(sorted(VALID_CONDITIONS))
            )

        if self.purchase_price < 0:
            raise ValueError("Purchase price cannot be negative.")

        if self.estimated_value < 0:
            raise ValueError("Estimated value cannot be negative.")

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


@dataclass
class RecordCollection:
    name: str
    records: List[Record] = field(default_factory=list)

    def add_record(self, record: Record) -> None:
        self.records.append(record)

    def record_count(self) -> int:
        return len(self.records)

    def get_record(self, index: int) -> Record:
        return self.records[index]

    def update_record(self, index: int, updated_record: Record) -> None:
        self.records[index] = updated_record

    def sell_record(self, index: int) -> Record:
        return self.records.pop(index)

    def find_by_artist(self, artist_name: str) -> List[Record]:
        search_term = artist_name.strip().lower()
        return [
            record
            for record in self.records
            if search_term in record.artist.lower()
        ]

    def filter_by_genre(self, genre_name: str) -> List[Record]:
        search_term = genre_name.strip().lower()
        return [
            record
            for record in self.records
            if search_term in record.genre.lower()
        ]

    def total_purchase_price(self) -> float:
        return sum(record.purchase_price for record in self.records)

    def total_estimated_value(self) -> float:
        return sum(record.estimated_value for record in self.records)

    def unique_artists(self) -> Set[str]:
        return {record.artist for record in self.records}

    def unique_genres(self) -> Set[str]:
        return {record.genre for record in self.records}

    def stats(self) -> Dict[str, object]:
        return {
            "total_records": len(self.records),
            "total_purchase_price": self.total_purchase_price(),
            "total_estimated_value": self.total_estimated_value(),
            "unique_artists": len(self.unique_artists()),
            "unique_genres": len(self.unique_genres()),
        }

    def to_dict_list(self) -> List[Dict[str, object]]:
        return [record.to_dict() for record in self.records]

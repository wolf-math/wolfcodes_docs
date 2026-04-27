import json
from pathlib import Path
from typing import Iterable

from models import Record, RecordCollection


def load_collection(file_path: str, collection_name: str) -> RecordCollection:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Could not find file: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Collection data must be a list of records.")

    records = [Record(**item) for item in data]
    return RecordCollection(name=collection_name, records=records)


def save_collection(collection: RecordCollection, file_path: str) -> None:
    path = Path(file_path)

    with path.open("w", encoding="utf-8") as file:
        json.dump(collection.to_dict_list(), file, indent=2)
        file.write("\n")


def seed_collection(
    collection_name: str,
    records: Iterable[Record],
) -> RecordCollection:
    return RecordCollection(name=collection_name, records=list(records))

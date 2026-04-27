from models import Record, RecordCollection, VALID_CONDITIONS
from ui import print_records


def prompt_for_text(prompt: str) -> str:
    value = input(prompt).strip()
    if not value:
        raise ValueError("This field cannot be empty.")
    return value


def prompt_for_int(prompt: str) -> int:
    value = input(prompt).strip()
    return int(value)


def prompt_for_float(prompt: str) -> float:
    value = input(prompt).strip()
    return float(value)


def prompt_for_condition() -> str:
    print(f"Valid conditions: {', '.join(sorted(VALID_CONDITIONS))}")
    return prompt_for_text("Condition: ")


def prompt_for_optional_text(prompt: str, current_value: str) -> str:
    value = input(f"{prompt} [{current_value}]: ").strip()
    return value or current_value


def prompt_for_optional_int(prompt: str, current_value: int) -> int:
    value = input(f"{prompt} [{current_value}]: ").strip()
    return current_value if not value else int(value)


def prompt_for_optional_float(prompt: str, current_value: float) -> float:
    value = input(f"{prompt} [{current_value}]: ").strip()
    return current_value if not value else float(value)


def prompt_for_optional_condition(current_value: str) -> str:
    print(f"Valid conditions: {', '.join(sorted(VALID_CONDITIONS))}")
    return prompt_for_optional_text("Condition", current_value)


def choose_record_index(collection: RecordCollection, action_name: str) -> int | None:
    if collection.record_count() == 0:
        print(f"\nThere are no records to {action_name}.")
        return None

    print(f"\nChoose a record to {action_name}")
    print("-------------------------")
    print_records(collection.records)

    try:
        selected_number = int(input(f"Record number to {action_name}: ").strip())
    except ValueError:
        print("Please enter a valid record number.")
        return None

    index = selected_number - 1
    if index < 0 or index >= collection.record_count():
        print("That record number is out of range.")
        return None

    return index


def prompt_for_new_record() -> Record:
    return Record(
        title=prompt_for_text("Album title: "),
        artist=prompt_for_text("Artist: "),
        year=prompt_for_int("Release year: "),
        genre=prompt_for_text("Genre: "),
        condition=prompt_for_condition(),
        purchase_price=prompt_for_float("Purchase price: "),
        estimated_value=prompt_for_float("Estimated value: "),
        notes=input("Notes (optional): ").strip(),
    )


def prompt_for_updated_record(current_record: Record) -> Record:
    return Record(
        title=prompt_for_optional_text("Album title", current_record.title),
        artist=prompt_for_optional_text("Artist", current_record.artist),
        year=prompt_for_optional_int("Release year", current_record.year),
        genre=prompt_for_optional_text("Genre", current_record.genre),
        condition=prompt_for_optional_condition(current_record.condition),
        purchase_price=prompt_for_optional_float(
            "Purchase price",
            current_record.purchase_price,
        ),
        estimated_value=prompt_for_optional_float(
            "Estimated value",
            current_record.estimated_value,
        ),
        notes=prompt_for_optional_text("Notes", current_record.notes),
    )

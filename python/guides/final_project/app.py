from actions import (
    add_record,
    edit_record,
    filter_by_genre,
    load_records,
    save_records,
    search_by_artist,
    sell_record,
    view_records,
    view_stats,
)
from ui import pause_for_menu, print_menu


def main() -> None:
    collection = load_records()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_records(collection)
            pause_for_menu()
        elif choice == "2":
            add_record(collection)
            pause_for_menu()
        elif choice == "3":
            edit_record(collection)
            pause_for_menu()
        elif choice == "4":
            sell_record(collection)
            pause_for_menu()
        elif choice == "5":
            search_by_artist(collection)
            pause_for_menu()
        elif choice == "6":
            filter_by_genre(collection)
            pause_for_menu()
        elif choice == "7":
            view_stats(collection)
            pause_for_menu()
        elif choice == "8":
            save_records(collection)
            pause_for_menu()
        elif choice == "9":
            print("Goodbye. Keep spinning records.")
            break
        else:
            print("Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()

import os
from typing import List, Tuple

# File name for storing phonebook data
phonebook_file = 'phonebook.txt'


def display_page(page_num: int, page_size: int, entries: List[str]) -> None:
    """Display a page of entries from the phonebook."""
    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size
    for idx, entry in enumerate(entries[start_idx:end_idx], start=start_idx + 1):

        print(f"{idx}. {entry}")


def add_entry(name: str, phone_number: str) -> None:
    """Add a new entry to the phonebook."""
    with open(phonebook_file, 'a') as f:
        f.write(f"{name} - {phone_number}\n")
    print("Entry added successfully.")


def edit_entry(index: int, name: str, phone_number: str) -> None:
    """Edit an existing entry in the phonebook."""
    entries = []
    with open(phonebook_file, 'r') as f:
        entries = f.readlines()

    if 0 < index <= len(entries):
        entries[index - 1] = f"{name} - {phone_number}\n"

        with open(phonebook_file, 'w') as f:
            f.writelines(entries)
        print("Entry edited successfully.")
    else:
        print("Invalid entry index.")


def search_entries(query: str) -> None:
    """Search for entries in the phonebook based on a query."""
    results = []
    with open(phonebook_file, 'r') as f:
        for line in f:
            if query.lower() in line.lower():
                results.append(line.strip())
    if results:
        print("Search results:")
        for idx, entry in enumerate(results, start=1):
            print(f"{idx}. {entry}")
    else:
        print("Nothing found.")


def main() -> None:
    """Main program loop for interacting with the phonebook."""
    while True:
        print("\nPhonebook")
        print("1. Display entries")
        print("2. Add entry")
        print("3. Edit entry")
        print("4. Search entries")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            page_size = 10
            with open(phonebook_file, 'r') as f:
                entries = f.readlines()
            total_entries = len(entries)
            total_pages = (total_entries + page_size - 1) // page_size

            page_num = int(input(f"Enter page number (1 - {total_pages}): "))
            if 1 <= page_num <= total_pages:
                display_page(page_num, page_size, entries)
            else:
                print("Invalid page number.")

        elif choice == '2':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_entry(name, phone_number)

        elif choice == '3':
            index = int(input("Enter entry number to edit: "))
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            edit_entry(index, name, phone_number)

        elif choice == '4':
            query = input("Enter search query: ")
            search_entries(query)

        elif choice == '5':
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    if not os.path.exists(phonebook_file):
        with open(phonebook_file, 'w') as f:
            pass
    main()

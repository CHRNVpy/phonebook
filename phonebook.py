import os
from typing import List


class Phonebook:
    def __init__(self, filename: str = 'phonebook.txt'):
        self.filename = filename

    def display_page(self, page_num: int, page_size: int) -> None:
        """Display a page of entries from the phonebook."""
        entries = self._load_entries()
        start_idx = (page_num - 1) * page_size
        end_idx = start_idx + page_size
        for idx, entry in enumerate(entries[start_idx:end_idx], start=start_idx + 1):
            print(f"{idx}. {entry}")

    def add_entry(self, name: str, last_name: str, middle_name: str, organization: str,
                  phone_number: str, mobile: str) -> None:
        """Add a new entry to the phonebook."""
        with open(self.filename, 'a') as f:
            f.write(f"{last_name} - {name} - {middle_name} - {organization} - {phone_number} - {mobile}\n")
        print("Entry added successfully.")

    def edit_entry(self, index: int, name: str, last_name: str, middle_name: str, organization: str,
                   phone_number: str, mobile: str) -> None:
        """Edit an existing entry in the phonebook."""
        entries = self._load_entries()
        if 0 < index <= len(entries):
            entries[index - 1] = f"{last_name} - {name} - {middle_name} - {organization} - {phone_number} - {mobile}\n"
            self._save_entries(entries)
            print("Entry edited successfully.")
        else:
            print("Invalid entry index.")

    def search_entries(self, query: str) -> None:
        """Search for entries in the phonebook based on a query."""
        results = []
        entries = self._load_entries()
        for line in entries:
            if query.lower() in line.lower():
                results.append(line.strip())
        if results:
            print("Search results:")
            for idx, entry in enumerate(results, start=1):
                print(
                    f"{idx}. {entry}")
        else:
            print("Nothing found.")

    def _load_entries(self) -> List[str]:
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return f.readlines()

    def _save_entries(self, entries: List[str]) -> None:
        with open(self.filename, 'w') as f:
            f.writelines(entries)


def main():
    phonebook = Phonebook()

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
            page_num = int(input("Enter page number: "))
            phonebook.display_page(page_num, page_size)

        elif choice == '2':
            last_name = input("Enter last name: ")
            name = input("Enter name: ")
            middle_name = input("Enter middle name: ")
            organization = input("Enter organization: ")
            phone_number = input("Enter phone number: ")
            mobile_number = input("Enter mobile: ")
            phonebook.add_entry(name, last_name, middle_name, organization, phone_number, mobile_number)

        elif choice == '3':
            index = int(input("Enter entry number to edit: "))
            last_name = input("Enter last name: ")
            name = input("Enter name: ")
            middle_name = input("Enter middle name: ")
            organization = input("Enter organization: ")
            phone_number = input("Enter phone number: ")
            mobile_number = input("Enter mobile: ")
            phonebook.edit_entry(index, name, last_name, middle_name, organization, phone_number, mobile_number)

        elif choice == '4':
            query = input("Enter search query: ")
            phonebook.search_entries(query)

        elif choice == '5':
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()

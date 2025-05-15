def main():
    phone_book = {}

    while True:
        print("\n--- Phone Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            phone_book[name] = number
            print(f"Contact '{name}' added.")

        elif choice == '2':
            name = input("Enter contact name to search: ")
            if name in phone_book:
                print(f"{name}'s number is {phone_book[name]}")
            else:
                print("Contact not found.")

        elif choice == '3':
            name = input("Enter contact name to delete: ")
            if name in phone_book:
                del phone_book[name]
                print(f"Contact '{name}' deleted.")
            else:
                print("Contact not found.")

        elif choice == '4':
            if not phone_book:
                print("Phone book is empty.")
            else:
                print("\n--- All Contacts ---")
                for name, number in phone_book.items():
                    print(f"{name}: {number}")

        elif choice == '5':
            print("Exiting Phone Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

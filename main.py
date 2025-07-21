from utils.add import add_contact
from utils.search import search_contact
from utils.delete import delete_contact

CONTACT_FILE = "contacts.json"

def menu():
    while True:
        print("\n==== Contact Book ====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            if not name or not phone.isdigit() or '@' not in email:
                print("Invalid input. Please try again.")
            else:
                add_contact(name, phone, email, CONTACT_FILE)
        elif choice == "2":
            query = input("Enter name to search: ").strip()
            search_contact(query, CONTACT_FILE)
        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            delete_contact(name, CONTACT_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

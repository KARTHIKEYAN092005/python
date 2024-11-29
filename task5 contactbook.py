contacts = {}
def add_contact():
    """Add a new contact."""
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    """Display all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}")

def search_contact():
    """Search for a contact by name or phone number."""
    search_query = input("Enter Name or Phone Number to search: ")
    for name, details in contacts.items():
        if search_query.lower() in name.lower() or search_query == details['Phone']:
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            return
    print("Contact not found.")

def update_contact():
    """Update an existing contact."""
    name = input("Enter the Name of the contact to update: ")
    if name in contacts:
        print("Leave blank to keep the current value.")
        phone = input(f"Enter new Phone Number (current: {contacts[name]['Phone']}): ") or contacts[name]['Phone']
        email = input(f"Enter new Email (current: {contacts[name]['Email']}): ") or contacts[name]['Email']
        address = input(f"Enter new Address (current: {contacts[name]['Address']}): ") or contacts[name]['Address']
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    """Delete a contact."""
    name = input("Enter the Name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

def main():
    """Main menu for the Contact Book."""
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
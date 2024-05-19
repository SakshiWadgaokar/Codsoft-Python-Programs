# Initialize an empty list to store contacts
contacts = []

def add_contact():
    # Prompt user for contact details
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    # Create a dictionary for the new contact
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    # Add the contact to the list
    contacts.append(new_contact)
    print("Contact added successfully!")

def view_contacts():
    print("Contact List:")
    for contact in contacts:
        print(f"{contact['name']} - {contact['phone']}")

# Implement other functions (search, update, delete) similarly

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        # Implement other menu options here
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

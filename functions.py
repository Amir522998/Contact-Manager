import json
from contacts import contacts


def load_contacts():
    try:
        with open("data.json", "r") as contacts_file:
            contacts.extend(json.load(contacts_file))

    except FileNotFoundError:
        print("data.json not found")

    except json.JSONDecodeError:
        print("data.json is empty or invalid")

def save_contacts():
    with open("data.json", "w") as contacts_file:
        json.dump(contacts, contacts_file, indent=4)

def validate_contact(name, phone):
    if not name.isalpha() or not phone.isdigit() or len(phone) != 11:
        print("Invalid name or phone number!")
        return False

    return True

def add_contact(name, phone):

    if not validate_contact(name, phone):
        return

    for contact in contacts:
        if name == contact["name"] and phone == contact["phone"]:
            print("Contact already exists!")
            return

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    save_contacts()
    print("contact added")

def search_contact(name, phone):
    found = False
    for contact in contacts:
        if name.lower() in contact["name"].lower() and phone == contact["phone"]:
            print("contact found : ", name, contact["phone"])
            found = True

    if not found:
        print("contact not found")

def delete_contact(name, phone):
    for contact in contacts:
        if name == contact["name"] and phone == contact["phone"]:
            answer = input("Are you sure you want to delete this contact? (y/n): ")
            if answer.lower() == "y":
                contacts.remove(contact)
                save_contacts()
                print("contact deleted")
                return

            elif answer.lower() == "n":
                print("Delete cancelled")
                return
            else:
                print("Please enter y or n")
                return

    print("contact not found")

def show_contacts(sort_choice):

    if sort_choice == "1":
        sorted_contacts = sorted(
            contacts,
            key=lambda contact: contact["name"]
        )

        if not sorted_contacts:
            print("contact not found")
            return

        number = 1

        for contact in sorted_contacts:
            print(f"{number}. {contact['name']}")
            number += 1

    elif sort_choice == "2":
        sorted_contacts = sorted(
            contacts,
            key=lambda contact: contact["phone"]
        )

        if not sorted_contacts:
            print("contact not found")
            return

        number = 1

        for contact in sorted_contacts:
            print(f"{number}. {contact['phone']}")
            number += 1

    else:
        print("Invalid option!")

def edit_contact(name, phone, new_name,new_phone ):

    if not validate_contact(new_name, new_phone):
        return

    for contact in contacts:
        if name == contact["name"] and phone == contact["phone"]:
            for other_contact in contacts:
                if new_name == other_contact["name"] and other_contact != contact:
                    print("Contact already exists!")
                    return

            contact["phone"] = new_phone
            contact["name"] = new_name
            save_contacts()
            print("contact edited")
            return
    print("contact not found")
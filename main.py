from functions import (
    add_contact,
    search_contact,
    delete_contact,
    load_contacts,
    show_contacts,
    edit_contact
)
import os

load_contacts()

options = (
    "========================\n"
    "    CONTACT MANAGER\n"
    "========================\n"
    "1. Add contact\n"
    "2. Search contact\n"
    "3. Delete contact\n"
    "4. Show contacts\n"
    "5. Edit contact\n"
    "6. Exit"
)


while True:

    os.system("cls")
    try:
        choice = int(input(options + "\n\nChoose your option: \n"))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:

        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        add_contact(name, phone)
        input("Press Enter to continue...")

    elif choice == 2:

        name = (input("Search your name: "))
        phone = (input("Search your phone: "))
        search_contact(name, phone)
        input("Press Enter to continue...")

    elif choice == 3:

        name = (input("Delete your name: "))
        phone = (input("Delete your phone: "))
        delete_contact(name, phone)
        input("Press Enter to continue...")


    elif choice == 4:

        sort_choice = input(
            "1. Sort by name\n"
            "2. Sort by phone\n"
            "Choose: "
        )
        show_contacts(sort_choice)
        input("Press Enter to continue...")

    elif choice == 5:

        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        new_name = input("Enter your new name: ")
        new_phone = input("Enter your new phone: ")

        edit_contact(name,phone ,new_name, new_phone)

        input("Press Enter to continue...")

    elif choice == 6:

        print("Goodbye!")
        break

    else:

        print("Invalid option! Please choose between 1 and 6.")
        input("Press Enter to continue...")
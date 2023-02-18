# set the name of the phone book file
phone_book_file = "phone_book.txt"

# load phone book data from file
phone_book = {}
with open(phone_book_file, "r") as f:
    for line in f:
        name, number = line.strip().split(":")
        phone_book[name] = number

while True:
    print("Phone Book\n")

    # print the current phone book
    if phone_book:
        print("Contacts:")
        for name, number in phone_book.items():
            print(f"{name}: {number}")
        print()

    # prompt the user for action
    print("What would you like to do?")
    print("1. Add a new contact")
    print("2. Update an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    # add a new contact
    if choice == "1":
        name = input("Enter the name of the contact: ")
        number = input("Enter the phone number of the contact: ")
        phone_book[name] = number
        print(f"{name} has been added to the phone book.\n")

    # update an existing contact
    elif choice == "2":
        name = input("Enter the name of the contact: ")
        if name in phone_book:
            number = input("Enter the new phone number of the contact: ")
            phone_book[name] = number
            print(f"{name}'s phone number has been updated.\n")
        else:
            print(f"{name} is not in the phone book.\n")

    # delete a contact
    elif choice == "3":
        name = input("Enter the name of the contact: ")
        if name in phone_book:
            del phone_book[name]
            print(f"{name} has been deleted from the phone book.\n")
        else:
            print(f"{name} is not in the phone book.\n")

    # search for a contact
    elif choice == "4":
        name = input("Enter the name of the contact: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}\n")
        else:
            print(f"{name} is not in the phone book.\n")

    # quit the program
    elif choice == "5":
        # write the phone book data to the file
        with open(phone_book_file, "w") as f:
            for name, number in phone_book.items():
                f.write(f"{name}:{number}\n")

        print("Goodbye!")
        break

    # invalid choice
    else:
        print("Invalid choice. Please try again.\n")
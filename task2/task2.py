def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if contacts.get(name, -1) == -1:
            contacts[name] = phone
            return "Contact added."
        else:
            return "Contact was not added. Same name was added before. You can use change command"

    except ValueError:
        return "Contact was not added. Wrong number of arguments were sent"

def change_contact(args, contacts):
    try:
        name, new_phone = args
        if contacts.get(name, -1) == -1:
            return "Contact's number can't be changed as it is not our system"
        else:
            contacts[name] = new_phone
            return "Contact phone number was changed."

    except ValueError:
        return "Contact's number was not changed. Wrong number of arguments were sent"

def get_contact_phone(args, contacts):
    try:
        name = args[0]
        if contacts.get(name, -1) == -1:
            return f"Contact with name: {name} is not present in our system"
        else:
            return f"Contact with name: {name} has phone number: {contacts[name]}"

    except IndexError:
        return "No argument for contact name was provided"

def get_all_contacts(contacts):
    result = []
    for name, phone in contacts.items():
        result.append(f"Contact with name: {name} has phone number: {phone}")
    return ("\n").join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

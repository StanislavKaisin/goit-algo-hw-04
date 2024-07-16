CONTACT_NOT_FOUND = "Contact not found."
THERE_ARE_NO_CONTACTS = "There are no contacts."


def find_phone(name: str, contacts: dict[str, str]) -> str:
    phone = contacts.get(name)
    if not phone:
        return None
    return phone


def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: tuple[str, str], contacts: dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    old_phone = find_phone(name, contacts)
    print(f"old_phone = {old_phone}")
    if not old_phone:
        return CONTACT_NOT_FOUND
    contacts[name] = phone
    return "Contact updated." or f"Contact {name} not found."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0]
    phone = find_phone(name, contacts)
    if not phone:
        return CONTACT_NOT_FOUND
    return phone


def show_all(contacts: dict[str, str]) -> None:
    if not contacts:
        print(THERE_ARE_NO_CONTACTS)
        return
    for name, phone_number in contacts.items():
        print(f"{name}\t{phone_number}")


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
            print(show_phone(args, contacts))
        elif command == "show":
            show_all(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

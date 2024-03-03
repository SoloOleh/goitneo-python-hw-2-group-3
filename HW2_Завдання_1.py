def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide enough information."
    return inner

def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found!"

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error
def show_all(contacts):
    if contacts:
        return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
    else: # в умові завдання цього не було, проте я добавив по аналогії з іншими функціями
        return "No contacts saved."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
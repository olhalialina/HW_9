import sys


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
        except TypeError:
            return "Invalid number of arguments passed"
    return wrapper


contacts = {}


@input_error
def hello():
    return "How can I help you?"


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"added {name.capitalize()} and {phone}"


@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return f"{name.capitalize()} phone number has been changed {phone}"


@input_error
def phone_contact(name):
    result = ' '
    phone = contacts.get(name, "Contact not found.")
    return f"{name.capitalize()} : {phone}\n"


@input_error
def show_all_contacts():
    if contacts:
        result = ' '
        for name, phone in contacts.items():
            result += f"{name} : {phone}\n"
        return result
    else:
        return "No contacts found."


@input_error
def good_bye():
    return "Good bye!"


CONSOLE_COMMAND = {
    "hello": hello,
    "add": add_contact,
    "change": change_contact,
    "phone": phone_contact,
    "show_all": show_all_contacts,
    "exit": good_bye
}


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        args = sys.argv[2:] if len(sys.argv) > 2 else None
        func = CONSOLE_COMMAND.get(command)
        if func:
            if args:
                print(func(*args))
            else:
                print(func())

    while True:
        user_input = input("Enter command: ").lower()
        if user_input in ("good bye", "close", "exit"):
            print(CONSOLE_COMMAND["exit"]())
            break
        else:
            command_parts = user_input.split(maxsplit=1)
            cmd = command_parts[0].lower()
            args = command_parts[1] if len(command_parts) > 1 else None
            func = CONSOLE_COMMAND.get(cmd)
            if func:
                if args:
                    print(func(*args.split()))
                else:
                    print(func())
            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()


































    
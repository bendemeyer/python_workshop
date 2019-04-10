from modules.messages import get_welcome_message, get_goodbye_message


def print_welcome_message(name):
    print(get_welcome_message(name))


def print_goodbye_message(name):
    print(get_goodbye_message(name))


print_welcome_message("Ben")
print_goodbye_message("Ben")
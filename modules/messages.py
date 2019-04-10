def get_welcome_message(name):
    return "Welcome, {0}!".format(name)


def get_goodbye_message(name):
    return "Goodbye, {0}, we'll miss you!".format(name)


print(get_welcome_message("Ben"))
print(get_goodbye_message("Ben"))
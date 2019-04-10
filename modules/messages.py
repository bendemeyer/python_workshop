import requests
import datetime


def get_welcome_message(name):
    response = requests.get('http://localhost:5000/greeting/')
    greeting = response.json().get('greeting')
    time = datetime.datetime.now()
    return f"{greeting}, {name}! The current time is {time}"


def get_goodbye_message(name):
    return f"Goodbye, {name}, we'll miss you!"


if __name__ == '__main__':
    print(get_welcome_message('Monty'))
    print(get_goodbye_message('Monty'))
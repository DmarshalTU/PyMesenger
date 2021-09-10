# https://repl.it/@Levashov/messenger

# name = input('Как тебя зовут? ')
# print(f'Hello, {name}!')

import time

db = [
    {
        'text': 'Привет',
        'time': time.time(),
        'name': 'Nick'
    },
    {
        'text': 'Привет, Nick',
        'time': time.time(),
        'name': 'Jane'
    }
]

def print_message(message):
    # TODO beautify time
    print(message['time'], message['name'])
    print(message['text'])
    print()

def print_messages(db):
    for message in db:
        print_message(message)

def send_message(name, text):
    message = {
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)

def get_messages(after):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return messages


send_message('Nick', 'Привет')

messages = get_messages(0)
print_messages(messages)

send_message('Nick', 'Привет2')

messages = get_messages(messages[-1]['time'])
print_messages(messages)

messages = get_messages(messages[-1]['time'])
print_messages(messages)

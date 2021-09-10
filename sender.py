import requests

name = input('Введите имя: ')

while True:
    text = input('Введите текст: ')
    requests.post(
        'http://127.0.0.1:5000/send',
        json={'name': name, 'text': text}
    )

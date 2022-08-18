import requests
import json

TOKEN = '2052338771:AAHWqySU9KeCy3P_7i-2cLm3Fn78dLKG2RY'




def send_msg(chat_id: int, text: str):
    keyboard = {
        'keyboard': [
            [
                {'text': 'button 1'}, {'text': 'button 2'}
            ],
            [
                {'text': 'button 3'}, {'text': 'button 4'}
            ],
            [
                {'text': 'buttun 5'}
            ]
        ]
    }

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': keyboard
    }

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    r = requests.post(url, json=payload)

    print(r.json())

chat_id = 1258594598
text = 'test'

send_msg(chat_id, text)

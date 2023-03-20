import json
import requests

TOKEN = '5998789700:AAE7vbpNAU4sCdj66zZUg1mkH3cILb2T2gg'

prefix = 'https://api.telegram.org/bot'
key = TOKEN
geturl = prefix + key + '/getUpdates'
sendurl = prefix + key + '/sendMessage'
timeout = 60


class InlineKeyboardButton:
    def __init__(self):
        self.text = 'Button'


class InlineKeyboardMarkup:
    def __init__(self):
        self.keyboard = [InlineKeyboardButton().__getattribute__('text')]


def main():
    offset = 0
    while True:
        dt = dict(offset=offset, timeout=timeout)
        try:
            req = requests.post(geturl, data=dt, timeout=None).json()
        except ValueError:
            continue
        if not req['ok'] or not req['result']:
            continue

        for r in req['result'][:]:
            message = r['message']
            id = message['chat']['id']
            if 'text' in message:

                keyboard = json.dumps({'inline_keyboard': [
                    [{'text': 'Да', 'callback_data': '1'}, {'text': 'Нет', 'callback_data': '2'}],
                    [{'text': 'Google', 'url': 'www.google.ru'}]]})

                dt = dict(chat_id=id, text='reply', reply_markup=keyboard)
                print(requests.post(sendurl, data=dt).json())
            offset = r['update_id'] + 1


if __name__ == '__main__':
    main()

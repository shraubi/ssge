# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events


def get_telegram_client():
    # get your api_id, api_hash, token
    # from telegram as described above
    api_id = '18616861'
    api_hash = 'edf13b6cbabd4a2af6f34271e0b57aef'
    token = 'bot token'
    message = "Working..."

    # your phone number
    phone = 'YOUR_PHONE_NUMBER_WTH_COUNTRY_CODE'

    # creating a telegram session and assigning
    # it to a variable client
    client = TelegramClient('session', api_id, api_hash)

    # connecting and building the session
    client.connect()
    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or sent or your telegram id
    if not client.is_user_authorized():
        client.send_code_request(phone)

        # signing in the client
        client.sign_in(phone, input('Enter the code: '))
    return client



def send_message(message):
    client = get_telegram_client()

    try:
        # receiver user_id and access_hash, use
        # my user_id and access_hash for reference
        receiver = InputPeerUser(18616861, 'edf13b6cbabd4a2af6f34271e0b57aef')

        # sending message using telegram client
        client.send_message(receiver, message, parse_mode='html')
    except Exception as e:

        # there may be many error coming in while like peer
        # error, wrong access_hash, flood_error, etc
        print(e);

    # disconnecting the telegram session
    client.disconnect()

import requests

def send_msg(text):
   token = "5663097801:AAH8FJmqavokiPJoxg3H4XQVVtQuqYfhEJU"
   chat_id = '240372740'
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   print(url_req)
   results = requests.get(url_req)
   print(results.json())

send_msg("Hello there!")


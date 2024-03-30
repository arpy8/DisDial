import pytz
import json
import time
import requests
import datetime
import logging

from disdial.__user_name import main as __username_main
from disdial.__constants import API_URL, API_URL2, LOGS_FILE_PATH, JSON_FILE_PATH

_chat_token = json.load(open(JSON_FILE_PATH))['token']
_chat_headers = {
    'Authorization': _chat_token,
    'Content-Type': 'application/json',
}

logging.basicConfig(filename=LOGS_FILE_PATH, level=logging.INFO)

def get_time():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

def read_logs():
    with open(LOGS_FILE_PATH, "r") as f:
        return f.read()

def update_logs(message):
    with open(LOGS_FILE_PATH, "w") as f:
        f.write(message)

def get_last_message():
    return get_all_messages()[-1]

def get_all_messages():
    try:
        response = requests.get(API_URL2, headers=_chat_headers)
        response.raise_for_status()
        data = response.json()[::-1]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching messages: {e}")
        data = []
    return [x for x in data if x != ""]

def check_and_update_new_message():
    try:
        last_message = get_last_message()
    except IndexError:
        last_message = ""
        
    if last_message != read_logs():
        update_logs(last_message)
        return True
    else:
        return False
    
def send_message_to_server(message):
    current_time = get_time()
    username = __username_main()

    data = {
        'time': current_time,
        'username': username,
        'message': message,
    }

    try:
        response = requests.post(API_URL, json=data, headers=_chat_headers)
        response.raise_for_status()
        update_logs(f"[{current_time}] {username}: {data['message']}")
        return f"[{current_time}] {username}: {data['message']}"
    
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"   

def update_screen():
    print('\033c', end='')
    for msg in get_all_messages():
        print(msg)

def auto_update_screen(stop_event, interval_seconds=5):
    while not stop_event.is_set():
        new_message, _ = check_and_update_new_message()

        if new_message:
            print("New message detected. Updating screen...")
            update_screen()

        time.sleep(interval_seconds)

    print("Auto-update thread is exiting.")

def main():
    if check_and_update_new_message():
        try:
            update_logs(get_all_messages()[-1])
        except IndexError:
            pass
        return get_all_messages()
    else:
        return False

if __name__ == "__main__":
    main()
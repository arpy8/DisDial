from .__constants import *
from .__user_name import main as __username_main
from .__dependencies import requests, datetime, pytz, json, os

token = json.load(open(JSON_FILE_PATH))['token']
headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
}

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
    response = requests.get(API_URL2, headers=headers)
    data = response.json()[::-1]
    data = [x for x in data if data != ""]
    return data

def check_new_message():
    last_message = get_last_message()
    return (True, last_message) if last_message != read_logs() else (False, last_message)

def send_message_to_server(message):
    current_time = get_time()
    username = __username_main()
    
    data = {
            'time': current_time,
            'username': username,
            'message': message, 
            }
    
    response = requests.post(API_URL, json=data, headers=headers)
        
    if response.status_code == 200:
        update_logs(f"[{current_time}] {username}: {data['message']}")
        return f"[{current_time}] {username}: {data['message']}"
    else:
        return f"request failed : {response.status_code}"
        
def update_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for msg in get_all_messages():
        print(msg)


def main():
    if check_new_message()[0]:
        update_logs(get_all_messages()[-1])
        return get_all_messages()
    else: 
        return False
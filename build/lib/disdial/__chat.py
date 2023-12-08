from .__constants import *
from .__user_name import main as __username_main
from .__dependencies import requests, datetime, pytz

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
        response = requests.get(API_URL)
        data = response.json()
        last_message = data['message'] if data else None
        return last_message
    
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
    
    response = requests.post(API_URL, json=data)
        
    if response.status_code == 200:
        update_logs(f"[{current_time}] {username}: {data['message']}")
        return f"[{current_time}] {username}: {data['message']}"
        
    else:
        return f"request failed : {response.status_code}"
        
def main():
    if check_new_message()[0]:
        update_logs(get_last_message())
        return True, f"one new message found!\n{get_last_message()}"
    else: 
        return False, None
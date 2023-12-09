from .__utils import *
from .__constants import *

def get_username():
    try:
        with open(JSON_FILE_PATH, "r") as f:
            return json.load(f)["name"]
        
    except Exception as e:
        print(colored(f"Error setting username: {e}", "red"))

def set_username(username):
    try:
        with open(JSON_FILE_PATH, 'r') as f:
            data = json.load(f)
            
        data['name'] = username
        
        with open(JSON_FILE_PATH, 'w') as f:
            json.dump(data, f, indent=2)
            
        print(colored(f"username set to {username}", "green"))

    except Exception as e:
        print(colored(f"error setting username: {e}", "red"))

def main():
    name = get_username()
    
    if get_username() == "NULL":
        name = input("Please enter your name: ")
        set_username(name)
    
    return name
import json
from disdial.__utils import colored
from disdial.__constants import JSON_FILE_PATH

def get_username():
    try:
        with open(JSON_FILE_PATH, "r") as f:
            return json.load(f)["name"]
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(colored(f"Error decoding JSON: {e}", "red"))
        return None

def set_username(username):
    try:
        with open(JSON_FILE_PATH, 'r') as f:
            data = json.load(f)

        data['name'] = username.strip()

        with open(JSON_FILE_PATH, 'w') as f:
            json.dump(data, f, indent=2)

        print(colored(f"Username set to {username}", "green"))

    except FileNotFoundError:
        print(colored("JSON file not found.", "red"))
    except json.JSONDecodeError as e:
        print(colored(f"Error decoding JSON: {e}", "red"))
    except Exception as e:
        print(colored(f"Error setting username: {e}", "red"))

def main():
    username = get_username()

    if username is None or username == "NULL":
        username = input("Please enter your name: ")
        set_username(username)

    return username

if __name__ == "__main__":
    main()
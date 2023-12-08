import json 

JSON_FILE_PATH = "disdial/data/config.json"

def get_username():
    with open(JSON_FILE_PATH, "r") as f:
        return json.load(f)["name"]

def set_username(username):
    with open(JSON_FILE_PATH, "w") as f:
        json.dump({"name": username}, f)
        return "-> username set to {username}"

def main():
    name = get_username()
    
    if name == "NULL":
        name = input("Please enter your name: ")
        set_username(name)
    
    return name

print(main())
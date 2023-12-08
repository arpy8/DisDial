from .__utils import *
from .__constants import *

#         try:
#             startupinfo = subprocess.STARTUPINFO()
#             startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#             process = subprocess.Popen(command, startupinfo=startupinfo, stdout=subprocess.PIPE, 
#                                        stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=power_shell, text=True).stdout.read()
#             return str(process)+"\n"
        
#         except subprocess.CalledProcessError as e:
#                 return f"Error: {e}"

# def extract_name_from_cli():
#     command = ["systeminfo"]
#     sys_info = _run_command(command)
#     username = sys_info.split("\n")[4].split(":")[1].strip()

#     return username

def get_username():
    with open(JSON_FILE_PATH, "r") as f:
        return json.load(f)["name"]

def set_username(username):
    with open(JSON_FILE_PATH, "w") as f:
        json.dump({"name": username}, f)
        return "-> username set to {username}"

def main():
    name = get_username()
    
    if get_username() == "NULL":
        name = input("Please enter your name: ")
        set_username(name)
    
    return name
import argparse
import keyboard
import threading
from disdial.__utils import *
from disdial.__chat import main as __chat_main
from disdial.__user_name import main as check_username, set_username
from disdial.__chat import check_and_update_new_message, update_screen, send_message_to_server, get_all_messages

stop_event = threading.Event()

def process_input(message):
    if message[:2] == "-c":
        set_username(message[2:])
    elif message in ["rr", "rf", "-r", "rl", "clea", ""]:
        update_screen()
    elif message == "exit":
        exit(0)
    else:
        send_message_to_server(message)

def is_key_pressed(key):
    return keyboard.is_pressed(key)

def input_loop():
    temp_list = get_all_messages()
    try:
        update_screen()
        
        while True:
            new_message, local_message = check_and_update_new_message()
            if new_message:
                print('\033c', end='')
                temp_list.append(local_message)
                
                for msg in temp_list:
                    print(msg)
                
            time.sleep(0.2)
    
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit(0)
        
    except EOFError:
        pass

def main():
    try:
        parser = argparse.ArgumentParser(description="A terminal-based IRC-inspired package that enables users to chat on a single server with everyone.")
        parser.add_argument("-d", "--docs", action="store_true", help="documentation about the library.")
        args = parser.parse_args()

        if not any(vars(args).values()):
            check_username()
            load_animation()
            welcome_message()
            __chat_main()
            loading_animation2()
            
            input_loop()

        if args.docs:
            open_url("https://youtu.be/-p0a9BJTEvA")

    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit(0)

if __name__ == "__main__":
    main()
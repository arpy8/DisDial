import argparse
from disdial.__utils import *
from disdial.__chat import main as __chat_main
from disdial.__user_name import main as check_username, set_username
from disdial.__chat import update_screen, send_message_to_server, get_all_messages

def process_input(message):
    if message[:2] == "-c":
        set_username(message[2:])
    elif message in ["rr", "rf", "-r", "rl", "clea", ""]:
        update_screen()
    elif message == "exit":
        exit(0)
    else:
        send_message_to_server(message)
        update_screen()

def input_loop():
    try:
        while True:
            message = input(f"\n>> ")
            process_input(message)
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

            for message in get_all_messages():
                print(message)

            update_screen() 
            input_loop()

        if args.docs:
            open_url("https://youtu.be/-p0a9BJTEvA")

    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit(0)

if __name__ == "__main__":
    main()
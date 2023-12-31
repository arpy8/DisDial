from .__utils import *
from .__chat import main as __chat_main
from .__chat import check_new_message, update_screen, send_message_to_server, get_all_messages, auto_update_screen
from .__user_name import main as check_username, set_username

# def detect_change():
#     while 1:
#         update_screen()
#         time.sleep(2)

def main():
    try:
        parser = argparse.ArgumentParser(description="This is a library designed to enable one to chat from the CLI.")
        parser.add_argument("-d", "--docs", action="store_true", help="documentation about the library.")    
        args = parser.parse_args()
        
        if not any(vars(args).values()):
            check_username()
            
            load_animation()
            welcome_message()
            response = __chat_main()
            loading_animation2()

            for message in get_all_messages():
                print(message)

            update_screen() 
            while True:
                try:
                    message = input(f"\n>> ")
                    if message[:2] == "-c":
                        set_username(message[2:])
                        continue
                    if message in ["rr", "rf", "-r", "rl", "clea", ""]:
                        update_screen()
                        continue
                    if message == "exit":
                        exit(0)
                    send_message_to_server(message)
                    update_screen() 
                except EOFError:
                    break

        if args.docs:
            open_url("https://youtu.be/-p0a9BJTEvA")
            
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit(0)

if __name__ == "__main__":
    main()
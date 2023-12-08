from .__utils import *
from .__chat import main as start_chat
from .__chat import send_message_to_server
from .__user_name import main as check_username
from .__user_name import get_username

def main():
    parser = argparse.ArgumentParser(description="This is a library designed to enable one to chat from the CLI.")
    parser.add_argument("-d", "--docs", action="store_true", help="documentation about the library.")    
    args = parser.parse_args()
    
    if not any(vars(args).values()):
        check_username()
        
        load_animation()
        welcome_message()

        response = start_chat()
        
        if response[0]:
            print(response[1])
        else:
            print("No new messages.")
        
        message = input(f"[{get_username()}]: ")
        
        print(send_message_to_server(message))
        
    if args.docs:
        open_url("https://youtu.be/-p0a9BJTEvA")
    
if __name__ == "__main__":
    main()
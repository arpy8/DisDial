from __dependencies import *

def open_url(url):
    webbrowser.open(url)

def path_converter(file_name):
    return pkg_resources.resource_filename('disdial', file_name)

def welcome_message():
    print(colored("Welcome to Disdial!", "green"))

def load_animation():

    load_str = f"Loading... "
    ls_len = len(load_str)

    animation = [".(^-^)'", "-(^-^)-", "'(^-^).", "-(^-^)-", ".(^-^)'", "-(^-^)-", "'(^-^).", "-(^-^)-"]
    anicount = 0

    counttime = 0
    i = 0
    count = 0
    while count<10:
        time.sleep(0.1)

        load_str_list = list(load_str)

        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()

        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

        count+=1

    os.system("cls")
        
def load_time_animation(username, trigger):
    count = 0
    while not trigger.is_set():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)

        sys.stdout.write("\r[{}] {}:".format(current_time, username))
        sys.stdout.flush()

        count += 1

    sys.stdout.write("\r[{}]".format(current_time))
    sys.stdout.flush()

trigger = threading.Event()
animation_thread = threading.Thread(target=load_time_animation, args=("arpy8",trigger,))

def start_time_animation():
    animation_thread.start()

def stop_time_animation():
    trigger.set()
    animation_thread.join()
    
start_time_animation()
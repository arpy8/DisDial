from .__dependencies import *

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
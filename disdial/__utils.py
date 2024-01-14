import os
import time
import random
import webbrowser
import pkg_resources
from termcolor import colored


animations = [[".(^-^)'", "-(^-^)-", "'(^-^).", "-(^-^)-", ".(^-^)'", "-(^-^)-", "'(^-^).", "-(^-^)-"],
              ["▯▯▯▯ 25%", "▯▯▯▯▯▯▯▯ 50%", "▯▯▯▯▯▯▯▯ 70%", "\\"],
              ["", "", "", "", ""]
            ]


def open_url(url):
    webbrowser.open(url)

def path_converter(file_name):
    return pkg_resources.resource_filename('disdial', file_name)

def welcome_message():
    print(colored("Welcome to DisDial!\n", "green"))

def load_animation(pref="Loading... ", i=0):
    load_str = pref
    ls_len = len(load_str)

    animation = animations[i]
    anicount = 0

    counttime = 0
    i = 0
    count = 0

    while count < 10:
        time.sleep(0.1)

        load_str_list = list(load_str)

        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

        print("\r" + res + animation[anicount], end='', flush=True)

        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

        count += 1

    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation2():
    animations = [
                "24.3%  ▯▯▯▯▯▯", 
                "58.7% ▯▯▯▯▯▯▯▯▯▯▯▯", 
                "75.1% ▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯", 
                "99.9% ▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯"
                ]

    for animation in animations:
        print(animation, end='', flush=True)
        time.sleep(random.uniform(0.12, 0.25))
        print("\r", end='', flush=True)
        
    os.system('cls' if os.name == 'nt' else 'clear')
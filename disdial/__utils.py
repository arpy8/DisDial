import os
import time
import json
import random
import webbrowser
import pkg_resources
import pyautogui as pg
from termcolor import colored
from disdial.__constants import SETTINGS_PATH


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
    

def set_terminal_opacity(transparent: bool = True) -> str:
    print(f"{'Restoring' if not transparent else 'Modifying'} terminal opacity...")
    
    opacity_value = 0 if transparent else 100
    
    try:
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, 'r') as f:
                settings_content = json.load(f)
            
            if "opacity" not in settings_content["profiles"]["defaults"]:
                settings_content["profiles"]["defaults"]["opacity"] = opacity_value
                with open(SETTINGS_PATH, "w") as file: 
                    json.dump(settings_content, file)
                return "Opacity appended successfully."
                
            opacity = int(settings_content["profiles"]["defaults"]["opacity"])
            
            if opacity != opacity_value:
                settings_content["profiles"]["defaults"]["opacity"] = opacity_value
                with open(SETTINGS_PATH, "w") as file: 
                    json.dump(settings_content, file)
                return "Opacity updated successfully."
            else:
                return "Opacity already set to the desired value."
        else:
            return "Settings file not found."
        
    except Exception as e:
        return f"An exception occurred: {e}"

    
def modify_env(transparent: bool = True) -> None:
    set_terminal_opacity(transparent)
    
    print("\033[H\033[J")
    
    if transparent:
        pg.press('f11')
        time.sleep(0.05)
        pg.hotkey('fn', 'f11')
        time.sleep(0.05)
        pg.press('f11')
    else:
        pg.press('f11')
    
    print("\033[H\033[J")
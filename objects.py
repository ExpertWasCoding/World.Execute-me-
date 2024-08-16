import os
import sys
import time
import pygame
import time
import random
from tqdm import tqdm
def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("worldExecute.mp3")
    pygame.mixer.music.play()

def clear_terminal():
    # Detect the operating system and issue the appropriate clear command
    os.system('cls' if os.name == 'nt' else 'clear')


def typewriter(text, wait_time):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(wait_time/len(text))

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
ENDC = "\033[0m"  
WHITE = "\033[97m"
PURPLE = "\033[95m"


def loader():
     for _ in tqdm(range(100), desc="Parameter Initialization", unit="%", ascii=True, ncols=66):
        time.sleep(0.02)
def charging_bar():
    pbar = tqdm(range(21), unit="|", bar_format='{l_bar}{bar}{r_bar}')
    for i in pbar:
        time.sleep(0.5)
        if i == 0:
            pbar.set_description("Setting up new world")
        elif i == 7:
            pbar.set_description("Initializing")
        elif i == 11:
            pbar.set_description("Rendering")
        elif i == 15:
            pbar.set_description("Loading")
        elif i == 19:
            pbar.set_description("Done")
            
def charging_bar_boss():
    pbar = tqdm(range(26), unit="|", bar_format='{l_bar}{bar}{r_bar}')
    for i in pbar:
        time.sleep(0.5)
        pbar.set_description(f"Loading BOSS fight, {RED}opponent : GOD, {GREEN}objective : escape")

def START_SIMULATION():
        obj = """\033[32m \n________________________________________________________________________________________
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
*  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
. *      .   .    .  .     .  *      .      .        .     .-o--.   .    *  .
.  .        .     .     .      .    .     *      *   .   :O o O :      .     .
____   *   .    .      .   .           .  .   .      .    : O. Oo;    .   .
`. ````.---...___      .      *    .      .       .   * . `-.O-'  .     * . .
\_    ;   \`.-'```--..__.       .    .      * .     .       .     .        .
,'_,-' _,-'             ``--._    .   *   .   .  .       .   *   .     .  .
-'  ,-'                       `-._ *     .       .   *  .           .    .
    ,-'            _,-._            ,`-. .    .   .     .      .     *    .   .
    '--.     _ _.._`-.  `-._        |   `_   .      *  .    .   .     .  .    .
        ;  ,' ' _  `._`._   `.      `,-''  `-.     .    .     .    .      .  .
    ,-'   \    `;.   `. ;`   `._  _/\___     `.       .    *     .    . *
    \      \ ,  `-'    )        `':_  ; \      `. . *     .        .    .    *
    \    _; `       ,;               __;        `. .           .   .     . .
    '-.;        __,  `   _,-'-.--'''  \-:        `.   *   .    .  .   *   .
        )`-..---'   `---''              \ `.        . .   .  .       . .  .
___________________________________________________________________________________________\033[0m"""
        print(obj)
        
def print_glitch(text):
    for char in text:
        # Introduce randomness for the glitch effect
        if random.random() < 0.1:
            sys.stdout.write("\033[91m" + chr(random.randint(33, 126)) + "\033[0m")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
        
item1 = "NUTRIENTS"
item2 = "ANTI-OXIDANTS"
item3 = "ENJOYMENT and AFFECTION"
item4 = "EXISTENCE"
item5 = "TRUST"
item6 = "LOVE"

inventory_string = (
    f'"Item1": "{item1}", '
    f'"Item2": "{item2}", '
    f'"Item3": "{item3}", '
    f'"Item4": "{item4}", '
    f'"Item5": "{item5}"'
)
inventory_string1 = (
    f'"Item1": "{item1}", '
    f'"Item2": "{item2}", '
    f'"Item3": "{item3}", '
    f'"Item4": "{item4}", '
    f'"Item5": "{item5}", '
    f'"Item6": "{item6}"'
)
ending = """
 _ _ _  _  ___ _    __    _____ _____ __  _ _  ___  ___   _ _   _  ___ _   
| | | |/ \| o \ |  |  \  | __\ V / __/ _|| | ||_ _|| __| //| \_/ || __|\\  
| V V ( o )   / |_ | o ) | _| ) (| _( (_ | U | | | | _| || | \_/ || _|  |()
 \_n_/ \_/|_|\\___||__() |___/_n_\___\__||___| |_| |___||| |_| |_||___| |()
                                                         \\            //V 

CREATED BY EXPERT
MUSIC BY MILI 'WORLD.EXECUTE(ME);'
                                                                         
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
*  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
*  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
*  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
""" 

# Create the final formatted string
data_string = f'{{inventory: {inventory_string}}}'
data_string1 = f'{{inventory: {inventory_string1}}}'

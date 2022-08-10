import keyboard
import time
import mss
from PIL import Image, ImageStat

KEYPRESS = 0.1
CHANGEKEY = 0.4
SCREEN_LOCATION = {"top": 400, "left": 40, "width": 40, "height": 40}
COLOR_MINIMUM = 150
sct = mss.mss()


def keypress(key):
    time.sleep(CHANGEKEY)
    keyboard.press(key)
    time.sleep(KEYPRESS)
    keyboard.release(key)


def check_if_white():
    sct_img = sct.grab(SCREEN_LOCATION)
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    extrema = ImageStat.Stat(img).extrema
    return all(e[0] > COLOR_MINIMUM for e in extrema)


def lightning_dodge():
    last_is_white = False
    dodge_count = 0
    while True:
        is_white = check_if_white()
        if is_white and not last_is_white:
            keyboard.press('c')
            time.sleep(KEYPRESS)
            keyboard.release('c')
            dodge_count += 1
            print(f"{dodge_count}")
        last_is_white = is_white


print("============================")
print("FINAL FANTASTY X HD Tools v2")
print("============================\n")
print("====== SETUP ======")
print("Movement keys must be bound to WASD")
print("Confirm, Menu, and Cancel mapped to C, V, X respectively")
print("Yuna must be in 8th party slot for Yuna Party Heals to function correctly\n")
boosts = input("Do you want to have Boosts included in the script? (Type 'yes' or 'no'): ")

print("Press '1' to start Autobattler")
print("Press '2' to start Yuna Party Heal")
print("Press '3' to start  Lightning Dodger\n")
print("Press 'P' to Pause.")
print("Press 'Q' to Quit Program.")


while not keyboard.is_pressed('q'):
    if keyboard.is_pressed('q'):
        quit()
# AUTOBATTLER
    if keyboard.is_pressed('1'):
        if boosts.upper == "YES":
            keypress("f1")
            keypress("f1")
            keypress("f2")
            keypress("f3")
            keypress("f4")
        while not keyboard.is_pressed('p'):
            if keyboard.is_pressed('q'):
                if boosts.upper == "YES":
                    keypress("f1")
                    keypress("f2")
                    keypress("f3")
                    keypress("f3")
                    keypress("f4")
                quit()
            keyboard.press('c')
            keyboard.press('d')
            time.sleep(0.4)
            keyboard.release('d')
            keyboard.press('a')
            time.sleep(0.4)
            keyboard.release('a')
# YUNA PARTY HEAL
    if keyboard.is_pressed('2'):
        keypress("v")
        keypress("s")
        keypress("s")
        keypress("c")
        keypress("w")
        keypress("c")
        keypress("c")
        for heal in range(3):
            for cure in range(5):
                keypress("c")
            keypress("s")
        for back in range(3):
            keypress("x")
# LIGHTNING DODGER
    if keyboard.is_pressed('3'):
        if boosts.upper == "YES":
            keypress("f1")
            keypress("f1")
            keypress("f3")
            keypress("f3")
        while not keyboard.is_pressed('p'):
            lightning_dodge()
            if keyboard.is_pressed('q'):
                quit()

import ctypes
import os
from time import sleep
from threading import Event
from pynput import mouse, keyboard
from camera import save_victim_image
from arg_parser import args

screen_locked = Event()


def on_anything(*args):
    # Universal handler for any input
    lock_screen()
    return False


def lock_screen():
    if os.name is 'nt':  # Windows
        ctypes.windll.user32.LockWorkStation()
    else:  # Mac Os
        ctypes.CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login').SACLockScreenImmediate()
    save_victim_image()
    screen_locked.set()


keyboard_listener = keyboard.Listener(
    on_press=on_anything,
    on_release=on_anything)

mouse_listener = mouse.Listener(
    on_move=on_anything,
    on_click=on_anything,
    on_scroll=on_anything)

print("Program will be activated within {0} seconds...".format(args.activation_time))
sleep(args.activation_time)
keyboard_listener.start()
mouse_listener.start()
print("Protection activated!")

while True:
    sleep(0.2)
    if screen_locked.is_set():
        exit(0)

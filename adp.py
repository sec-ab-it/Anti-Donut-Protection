import ctypes
import os
from time import sleep
from threading import Event
from pynput import mouse, keyboard
from camera import save_victim_image

keyboard_controller = keyboard.Controller()

screen_locked = Event()


# Mouse handlers
def on_move(x, y):
    lock_screen()
    return False


def on_click(x, y, button, pressed):
    lock_screen()
    return False


def on_scroll(x, y, dx, dy):
    lock_screen()
    return False


# Keyboard handlers
def on_press(key):
    lock_screen()
    return False


def on_release(key):
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
    on_press=on_press,
    on_release=on_release)

mouse_listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)

print("Program will be activated within 5 seconds...")
sleep(5)
print("Protection activated!")

keyboard_listener.start()
mouse_listener.start()

while True:
    sleep(0.2)
    if screen_locked.is_set():
        exit(0)

# autoclick v0.1
# Built with assistance from ChatGPT
from pynput import keyboard, mouse
import threading
import time
import random

# Settings
min_delay = 0.03  # minimum delay
max_delay = 0.06  # maximum delay
long_delay_min = 0.10
long_delay_max = 0.15
button = mouse.Button.left  # left mouse button
hold_comma_key = keyboard.KeyCode(char=',')  # the comma key
hold_period_key = keyboard.KeyCode(char='.') # the period key

# State
mouse_controller = mouse.Controller()
holding_comma = False
holding_period = False

def clicker():
    while True:
        if holding_comma:
            print("Clicking comma...")
            mouse_controller.click(button)
            # Pick a random delay for each click
            time.sleep(random.uniform(min_delay, max_delay))
        elif holding_period:
            print("Clicking period...")
            mouse_controller.click(button)
            # Pick a random delay for each click
            time.sleep(random.uniform(long_delay_min, long_delay_max))
        else:
            print("Waiting...")
            time.sleep(0.01)

def on_press(key):
    global holding_comma
    global holding_period
    if key == hold_comma_key:
        holding_comma = True
        print("Holding key!")
    if key == hold_period_key:
        holding_period = True
        print("Holding key!")

def on_release(key):
    global holding_comma
    global holding_period
    if key == hold_comma_key:
        holding_comma = False
        print("Key Released!")
    if key == hold_period_key:
        holding_period = False
        print("Key Released!")

# Start the clicker thread
thread = threading.Thread(target=clicker)
thread.daemon = True
thread.start()

# Listen for key presses/releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

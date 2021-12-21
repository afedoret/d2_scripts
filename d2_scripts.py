from pynput.keyboard import Key, Controller
from pynput import keyboard
import time
import sys

def on_press(key):
	print(f"on press called, adding key {key}")
	# current.add(key)

def on_release(key):
	print("called on release")

	print(f"current before clear {current}")
	print(key)
	current.clear()
	print(f"current after clear {current}")
	# for things in current:
	# 	print(f"the keys in current are {things}")
	if key == keyboard.Key.esc:
		sys.exit()

##################################################################################
############################## Running Code ######################################
##################################################################################

current = set()
#keyboard = Controller()

with keyboard.Listener(on_press = on_press, on_release=on_release) as listener:
	listener.join()

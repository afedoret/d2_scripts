from pynput import keyboard
import sys

from pynput.keyboard import Key, Controller 


from pynput.mouse import Button
from pynput.mouse import Controller as mouse

import time

COMBINATIONS = [
	{keyboard.Key.shift, keyboard.KeyCode(char='A')},
	{keyboard.Key.shift, keyboard.KeyCode(char='B')},
	{keyboard.Key.shift, keyboard.KeyCode(char='C')},
	{keyboard.Key.ctrl , keyboard.KeyCode(char='C')}
]


def call_to_arms():

	cont.press('w')
	time.sleep(0.2)
	cont.release('w')

	time.sleep(0.5)
	cont.press('e')
	time.sleep(0.2)
	cont.release('e')
	right_click()

	time.sleep(0.5)
	cont.press('d')
	time.sleep(0.2)
	cont.release('d')
	right_click()

	time.sleep(0.5)
	cont.press('w')
	time.sleep(0.2)
	cont.release('w')
	print('complete')
	time.sleep(2)

def execute(COMBO):
	#listener.stop()
	if COMBO == 0:
		call_to_arms();
		print(0)
	elif COMBO == 1:
		print(1)
	elif COMBO == 2:
		sys.exit()
	else:
		print('a')#sys.exit()

	#listener.join()




def on_press(key):
	if any([key in COMBO for COMBO in COMBINATIONS]):
		current.add(key)
		if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
			print(get_index(current))
			execute(get_index(current))
			#current = set() 
	

def on_release(key):
	current.clear()
	if any([key in COMBO for COMBO in COMBINATIONS]):
		current.clear()
		print(f"the key {key} has been removed")

	for things in current:
		print(f'The remaining keys in current are: {things}')

	if key == keyboard.Key.esc:
		sys.exit()

def get_index(key):
	for iterations, COMBO in enumerate(COMBINATIONS):
		print(f"The Combo is {COMBO}")
		print(f"The key is {key}")
		if(COMBO == key):
			return iterations
	return null

def right_click():
	mouse.press(Button.right)
	time.sleep(0.1)
	mouse.release(Button.right)


##################################################################################
############################## Running Code ######################################
##################################################################################

current = set()
cont = Controller()
mouse = mouse()


with keyboard.Listener(on_press, on_release=on_release) as listener:
	listener.join()
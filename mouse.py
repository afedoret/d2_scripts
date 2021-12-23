
from pynput.mouse import Button
from pynput.mouse import Controller as mouse

mouse = mouse()

def right_click():
	mouse.press(Button.right)
	mouse.release(Button.right)

right_click()
print('yup')
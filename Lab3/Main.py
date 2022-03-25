from module.register import *
from module.login import *

while True:
	selector = input("If You Want to Register hit r, Login hit l, hit x to Exit: ")
	if selector == "r":
		regester()
	elif selector == "l":
		login()
	elif selector == "x":
		exit()



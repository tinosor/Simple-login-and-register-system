from colorama import Fore
import os
import random
import loginsystem

code5 = f"{random.randint(10000, 99999)}"
print(code5)

import keyboard
import time

verificationsuccesfull = False

code = ['_', '_', '_', '_', '_']


def verificationcode(verificationsuccesfull=False):
	while True:
		os.system('cls')
		time.sleep(0.1)
		print(''.join(code))
		try:
			event = keyboard.read_event()
			if event.name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
				if '_' in code:
					code[code.index('_')] = event.name
					os.system('cls')
			elif event.name == 'backspace':
				if any(char.isdigit() for char in code):
					for i in range(len(code) - 1, -1, -1):
						if code[i].isdigit():
							code[i] = '_'
							os.system('cls')
							break
			if code == [f'{code5[0]}', f'{code5[1]}', f'{code5[2]}', f'{code5[3]}', f'{code5[4]}']:
				os.system('cls')
				break
		except:
			os.system('cls')
			break


def register(email, password):
	while True:
		if 'gmail.com' not in email:
			os.system('cls')
			print(Fore.RED + "Incorrect email please use gmail")
			register(email=input(f"{Fore.GREEN}Email: "), password=input(f"Password: {Fore.RESET}"))
		elif 'gmail.com' in email:
			os.system('cls')
			print(f"{Fore.WHITE} Verification code send to email")
			verificationcode()
			time.sleep(3)
			with open('account.txt', 'a') as p:
				p.write(email + ':' + password)

			input(f"{Fore.RESET}{Fore.LIGHTGREEN_EX}Succesfully registered press any key to exit")
			quit()


test.login()

chien = 1
if chien == 0:
	register(email=input(f"{Fore.GREEN}Email: "), password=input(f"Password: {Fore.RESET}"))
	chien = chien + 1
else:
	quit()

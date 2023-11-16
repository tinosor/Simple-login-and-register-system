import re

found = 'False'


def check_word_in_file(file_path, email, password):
	with open(file_path, 'r') as file:
		contents = file.read()
		if re.search(r'\b{}\b'.format(f"{email}:{password}"), contents):
			return True
		else:
			return False


def login():
	email = input("Email: ")
	password = input("Password:  ")
	check_word_in_file(file_path='account.txt', email=f'{email}', password=f'{password}')
	if found:
		print("Succesfully login")
		quit()
	else:
		quit()


login()

import pyperclip
import re

data = pyperclip.paste()
lines = data.split('\n')


def Replacer(Info, Rules, X):  # Info represents the copied text to be edited
	regex = re.compile(fr'{Rules}')

	for i in range(len(lines)):
		mo = regex.search(lines[i])
		lines[i] = regex.sub(X, lines[i])  # x represents the data/text to be inserted

	Info = '\n'.join(lines)
	pyperclip.copy(Info)
	print(Info)


while True:
	rules = input('Kindly enter the Regular expression search rules: ')
	print(f'Rule is: {rules}')

	insert = input('\nKindly enter the replacement text: ')
	print(f'Found phrases shall be replaced with "{insert}", Confirm: Y/N ?')
	confirm = input()

	if confirm.lower() == 'y':
		Replacer(data, rules, insert)
		print('Success!')
		break
	else:
		print('Process Terminated!\n')
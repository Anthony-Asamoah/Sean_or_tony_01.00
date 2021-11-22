import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
	spam = lines[i]

print(f'\nCopied: \n{text}')

lines.sort()
text = '\n'.join(lines)
print(f'\nMod: \n{text}')

pyperclip.copy(text)
print(f'successfully copied to clipboard')

import pyperclip
import re

f = open("C:\\users\\dd\\Desktop\\requirements.txt", 'r')
data = f.read()
f.close()

print(data)
formatted_data = data.split('\n')

regex = re.compile(r'==((\d)*.)*')

for i in range(len(formatted_data)):
	formatted_data[i] = regex.sub('', formatted_data[i])

final_text = '\n'.join(formatted_data)

print(final_text)

pyperclip.copy(final_text)

f = open("C:\\users\\dd\\Desktop\\requirements.txt", 'w')
f.write(final_text)
f.close()

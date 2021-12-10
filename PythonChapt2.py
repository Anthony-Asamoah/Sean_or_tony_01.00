import re
import os
import openpyxl

# Pattern Matching without REGEX

# def isphonenum(info):
# 	if len(info) != 12:
# 		return False
# 	for i in range(0, 3):
# 		if not info[i].isdecimal():
# 			return False
# 	if info[3] != "-":
# 		return False
# 	for i in range(4, 7):
# 		if not info[i].isdecimal():
# 			return False
# 	if info[7] != '-':
# 		return False
# 	for i in range(8, 12):
# 		if not info[i].isdecimal():
# 			return False
# 	return True


# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
# 	chunk = message[i:i + 12]
# 	if isphonenum(chunk):
# 		print(f'number found: {chunk}')
# print('\nDone!')

######################################################################
# Pattern Matching With REGEX
# import re

# message = 'My line is 050-303-2976, or 055-864-2005.'

# phonenumregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # creating Regex object
# spam = phonenumregex.search(message)  # scanning through a given string
# print(f'\nNumber found: {spam.group()}')
# print(f'{spam.group(1)}, {spam.group(2)}')
# # or
# print(spam.groups())
#
# # using the multiple assign operator to label the groups
# areaCode, mainNum = spam.groups()
# print(f'\n{areaCode}, {mainNum}')

# message = "my line is (055) 303-2976"
#
# numSearch = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
# match = numSearch.search(message)
#
# print(f'Matched numbers: {match.group()}')


# showing precedence
# regex = re.compile(r'tony|toto')
# match = regex.search('Let\'s go see tony and toto today.')
# print(match.group())

# # searching for multiple words with the same prefix
# regex = re.compile(r'Bat(man|mobile|arang)')
# match = regex.search('see the Batman for more info...')
#

# regex = re.compile(r'bat(wo)?man')
# matchobj1 = regex.search('hey look at batman')
# matchobj2 = regex.search('hey thats batwoman')
# print(matchobj1.group())
# print(matchobj2.group())
#

# regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# matchobj1 = regex.search('My number is 415-555-4242')
# matchobj2 = regex.search('My number is 555-4242')
# print(matchobj1.group(), matchobj2.group())

# regex = re.compile(r'bat(wo)*man')
# matchobj0 = regex.search('The adventures of catwoman')
# matchobj1 = regex.search('The adventures of batman')
# matchobj2 = regex.search('The adventures of batwoman')
# matchobj3 = regex.search('The adventures of batwowowowoman')
#
# print(f'{matchobj1.group()}, {matchobj2.group()}, {matchobj3.group()}')
# print(f'nothing found: {matchobj0 is None}')

# the '+' operator requires at least one match to be valid unline the '*' operator
# which can find a match in the string without the specific occurance in brackets,
# like the '?' operator
# regex = re.compile('bat(wo)+man')
# mo1 = regex.search('Adventures of batman')
# mo2 = regex.search('Adv of batwoman')
# mo3 = regex.search('the adv of batwowowoman')
# print(f'{mo2.group()}, {mo3.group()}')
# if mo1 is None:
# 	print(True)
# else:
# 	print(False)

# # scanning for a specific number of repetiions...
# haRegex = re.compile(r'(Ha){3}')
# mo1 = haRegex.search('HaHaHa')
# mo2 = haRegex.search('Ha')
#
# print(mo1.group())
# try:
# 	print(mo2.group())
# except AttributeError:
# 	print('No value found')

# greedyregex, nongreedyregex = re.compile(r'(lo){3,6}'), re.compile(r'(lo){3,6}?')
# mo1, mo2 = greedyregex.search('lololololololol'), nongreedyregex.search('lololololololol')
# print(f'For greedy matching: {mo1.group()}.\nFor nongreedy matching: {mo2.group()}')

# Using the findall method which returns all matched objects as a list of strings instead of
# single matched object as a 'group()'

# numregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# groupnumregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#
# mo = numregex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())
# print(numregex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# print('')
# mo = groupnumregex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(f'Area code: {mo.group(1)}, Main number: {mo.group(2)}')
# print(groupnumregex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# text = 'coconut grapes salad and chicken, i want to sleep but fire is on the kitchen. razors blades and scissors echo' \
# 	   'as the witcher slaughters the butcher\'s butcher.'
#
# regex = re.compile(r'Sleep', re.IGNORECASE)
# matchedobject = regex.search(text)
#
# print('Matched Objects: ', matchedobject.group())
#
# findall = regex.findall(text)
# print('Findall:', findall)
#
# regex = re.compile(r'and (\w)\w+')
#
# matchedobject = regex.search(text)
#
# newtext = regex.sub(r'\1***', text)
#
# print(newtext)

#
# regex = re.compile(r'.*', re.IGNORECASE | re.VERBOSE | re.DOTALL)
# try:
# 	matchedobject = regex.search(text)
#
# 	print(matchedobject.group())
#
# except AttributeError:
# 	print("Null")


# #! python3
# # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
#
# import pyperclip, re
# from datetime import datetime
#
# #Phone Number Regex.
# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\)) # area code
# (\s|-|\.)? # separator
# (\d{3}) # first 3 digits
# (\s|-|\.)? # separator
# (\d{4}) # last 4 digits
# (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
# )''', re.VERBOSE)
#
# # Email regex.
# emailRegex = re.compile(r'''
# (\S+) # local part
# (@\S+)  # domain
# ''', re.VERBOSE)
#
# # Find matches in clipboard text.
# text = str(pyperclip.paste())
# matchedEmails = emailRegex.findall(text)
# matchedPhoneNums = phoneRegex.findall(text)
#
# # Arrange and format emails and numbers as a string
# dateobject = datetime.now()
# date = dateobject.strftime('%c')
#
# All_Info = f'{date}'
#
# emails = ""
# for i in range(len(matchedEmails)):
# 	emails += "".join(matchedEmails[i]) + "\n"
# if len(emails) < 1:
# 	print("No emails found")
#
# phoneNumbers = ''
# for i in range(len(matchedPhoneNums)):
# 	phoneNumbers += str(matchedPhoneNums[i][0]) + "\n"
# if len(phoneNumbers) < 1:
# 	print("No Phone Numbers found")
#
# if len(phoneNumbers) or len(emails) > 0:
# 	# join emails and phone numbers into one string
# 	if len(phoneNumbers) > 0:
# 		All_Info += "\n\n" + " Phone Numbers ".center(50, '=') + "\n" + phoneNumbers
#
# 	if len(emails) > 0:
# 		All_Info += "\n\n" + " Emails ".center(50, "=") + "\n" + emails
#
# 	# Copy results to the clipboard if numbers or emails were found.
# 	pyperclip.copy(All_Info)
#
# 	#print emails
# 	print("\n", All_Info)
#
# else:
# 	print('Nothing to copy; Operation aborted!')


# ################ Working with Files ################

# import os


# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
#
# for i in myFiles:
# 	print(os.path.join('C:\\users\\programs\\', i))

# print(os.getcwd())
#
# os.chdir(r'C:\users\dd\desktop')
# file = open("words.txt", "a")
# file.write('Appended!')
# file.close()

# os.chdir(r'C:\users\dd\Desktop')
# os.makedirs("Spam\Temp\Temp2")

# print(os.path.abspath('.'))

# dir = os.getcwd()  ############## variable holding directory

# print(os.path.split(os.getcwd()))
# print(dir.split(os.path.sep))

# print(os.path.getsize(dir),'bytes')
# print(os.listdir(dir))

# Net_size = 0
# for dirs in os.listdir(dir):
# 	size = os.path.getsize(dirs)
# 	Net_size += size
# 	print(f'dir: {dirs}', f'{size}bytes')
#
# print(f'\nTotal Size: {Net_size}bytes')

# print(f'is dir "{dir}": ', os.path.isdir(dir))
# print(f'exists "{dir}": ', os.path.exists(dir))
# print('is dir "random": ',  os.path.isdir('C:\\some_random_folder'))
# print('is file "random": ', os.path.isfile(os.path.join(dir, "some_random_file")))
# print(f'is file "{os.path.join(dir, "Temp3.py")}": ', os.path.isfile(os.path.join(dir, 'Temp3.py')))


# import os
# import shelve
# import pprint
#
# dir = os.path.join('C:\\', 'users', 'dd', 'desktop')

# file = open(os.path.join(dir, 'spam.txt'), 'w')
# file.write('Hola')
# file.close()

# file = open(os.path.join(dir, 'spam.txt'), 'a')
# file.write('\nNewlineeee')
# file.close()
#
# file = open(os.path.join(dir, 'spam.txt'), 'r')
# for i in file.readlines():
# 	print(i)
# file.close()

# print(dir)

##### using Shelve
# spam = ['cainemvhzc','cvwkxam', 'fullclip', 'kangaroo', 'fullclip']

# # creating a new shelf value (note:values are saved and retrieved just like dicts
# file = shelve.open(os.path.join(dir, 'DB1', 'Shelve'))
# file['spam'] = spam
# file.close()

# Reading from a shelve file
# file = shelve.open(os.path.join(dir, 'DB1', 'shelve'))
# print(list(file['spam']), '\n')
#
# for i in range(len(file['spam'])):
# 	print(file['spam'][i])
#
# file.close()

# # using keys() & values() & items(), just like with a dict/hashmap
# file = shelve.open(os.path.join(dir, 'DB1', 'shelve'))
# print('Using items(): ',list(file.items()))
# print('Using Keys: ', list(file.keys()))
# print('Using Values: ', list(file.values()))
# file.close()

# creating a .py file that can be later imported as a module
# spam = [dict(one='koko', two='tombrown', three='oblayoo'), dict(one='koose', two='buffloaf', three='bread')]
# formatted_spam = 'spam = ' + pprint.pformat(spam)
# file = open(os.path.join(dir, 'spam.py'),'w')
# file.write(formatted_spam)
# file.close()

# file = open(os.path.join(dir, 'spam.py'), 'r')
# print(file.read())
# file.close()

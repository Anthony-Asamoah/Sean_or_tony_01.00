import re


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
#


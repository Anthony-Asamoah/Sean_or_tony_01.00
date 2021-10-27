"""
def hello():
    print('Howdy')
    print('Hello')

hello()
hello()
"""

"""
def hello(name):
    print('Hello ' + name)

hello('Tony')
hello('Alice')

print("What's your name?")
name=input()
hello(name)
"""

"""
import random

def getanswer(ansnum):
    if ansnum == 1:
        return 'It is certain'

    elif ansnum == 2:
        return "It is deccidedly so"

    elif ansnum == 3:
        return "Right"

    elif ansnum == 4:
        return "Wrong"

    elif ansnum == 5:
        return "Try again later"

    elif ansnum == 6:
        return "Concentrate"

    elif ansnum == 7:
        return "I say Nay!"

    elif ansnum == 8:
        return "not good"

    elif ansnum == 9:
        return "Verry doubtful"



print(getanswer(random.randint(1,9)))

"""

"""
print('hello ', end ='')
print('world')

print('cats', 'dogs', 'mice', sep=', ')
"""

"""
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
"""

"""
def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
"""

"""
def spam(div):
    try:
        return 42 / div
    except ZeroDivisionError:
        print("Error: Invalid Argument!")


print(spam(2))
print(spam(9))
print(spam(6))
print(spam(0))
print(spam(1))
print(spam(3.4))
print(spam(7))
"""

"""
import random

SecretNum = random.randint(1, 100)
print('Ive got a number between one and a hundred')

for guessestaken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < SecretNum:
        print('a bit too ittle')

    elif guess > SecretNum:
        print('a bit too much')

    else: break

if guess == SecretNum:
    print('Good Job! you got it in ' + str(guessestaken) + ' shots.')

else:
    print('Nope, the number was ' + str(SecretNum))
    
"""

"""
####################################### Homework, aced! ######################################
def collatz(number):
    if number % 2 == 0:     # even numbers
        number = number / 2
        print(number)
        return number

    elif number % 2 == 1:   # odd numbers
        number = 3 * number + 1
        print(number)
        return number


print("enter an integer")

try:
    num = input()   # receive input

    num = int(num)  # Convert to Int

    while num > 1:  
        num = collatz(num)


except ValueError:
    print('Error: You may only enter integers.')
####################################################################################
"""

"""
l1 = ['cat', 'mouse', 'dog', 'chicken', 'coconut']
l2 = ['a', 'b', 'c', 'd', 'e']
print(l1)

# adding to lists
print(l1 + l2)
print(l1*2 + l2 * 3)

"""

"""
L1 = ['cat', 'mouse', 'dog', 'chicken', 'coconut']
print(L1)

# delete from a list
def dellist(num):
    num = int(num)
    del L1[num]
    print(L1)


dellist(3)
dellist(2)
"""

"""
catnames = []
while True:
    print("Enter a Cat's name " + str(len(catnames)) + " or enter nothing to stop. :")
    name = input()

    if name == '':
        break

    catnames = catnames + [name]

print('The names of your ' + str(len(catnames)) + ' cats are; ')
for name in catnames:
    print(' ' + name)
"""

"""
sppl = ['soap', 'tuna', 'spag', 'sausages','milk', 'water', 'bread']
for i in range(len(sppl)):
    print('# ' + str(i) + ' in supplies list is: ' + sppl[i])
"""

"""
list = ['bob', 'malik', 'toto', 'spade']
print('enter your pets name: ')
pet = input()

if pet not in list:
    print('Sorry, cant find your guy')

else:
    print("Got a " + pet + "!")
"""

"""
cat = ['fat', 'dark', 'calm']
size, color, mood = cat

print(color)
"""

"""
import random

list = [
    'It is so',
    'Most definately',
    'Right',
    'Yes',
    'Hmm, Check again',
    'i disagree',
    'No',
    'Doubtful',
    'Outlook not good'
]

print(list[random.randint(0, len(list) -1)])

"""

"""
pets = ('dog','cat','chicken')
animals = ['reptiles', 'mammals', 'amphibian', 'other']

pets = list(pets)
print(pets)

animals = tuple(animals)
print(animals)

listed = 'hello'
listed = list(listed)
print(listed)

"""

"""
def cars(fuel):
    fuel.append('fill')

spam = [1,2,3]
cars(spam)

print(spam)

"""

"""
import copy

alist = [1,2,3,4,5,6]
blist = copy.copy(alist)

blist[1] = 42

print(alist)
print(blist)
"""

'''
##################################### HOMEWORK #########################
def stringer(alist):
    alist = alist + []

    for i in range(len(alist)-1):
        print(str(alist[i]), end = ", ")
        i +=1
    print('and ' + str(alist[-1]))


############### TO MANUALLY ENTER A LIST ##################
alist = []
while True:

    print('Add to list or leave blank to complete: ')
    item = input()

    if item == '':
        break

    alist = alist + [item]


print('The list includes;')
stringer(alist)
'''

# grid = [['.', '.', '.', '.', '.', '.'],
#  ['.', 'O', 'O', '.', '.', '.'],
#  ['O', 'O', 'O', 'O', '.', '.'],
#  ['O', 'O', 'O', 'O', 'O', '.'],
#  ['.', 'O', 'O', 'O', 'O', 'O'],
#  ['O', 'O', 'O', 'O', 'O', '.'],
#  ['O', 'O', 'O', 'O', '.', '.'],
#  ['.', 'O', 'O', '.', '.', '.'],
#  ['.', '.', '.', '.', '.', '.']]
#
# for j in range(len(grid[0])):
#     for i in range(len(grid)):
#         print(grid[i][j], end='')
#     print('')


'''
var = '#'

for i in range(8):
    print(var * i)
'''

#
# black = '# '
# white = ' '
#
# for i in range(4):
#     print((black + white) * 4)
#     print((white + black) * 4)
#

# size = 8
# board = ' '
#
# for y in range(size):
#     for x in range(size):
#         if(x+y) % 2 == 0:
#             board += " "
#         else:
#             board += "#"
#     board += "\n"
#
# print(board)


# print('\n\nWelcome to the Palindrome Checker V1.0\n')
#
# while True:
#     print('kindly enter a word: ')
#     word = input()
#     print('Reverse: ' + word[::-1])
#
#     if word == word[::-1]:
#         print("\nword is a palindome")
#     else:
#         print("\nword is not a palindrome")
#

# mycat = {'name': 'Murzik', 'size': 'Medium', 'color': 'ginger'}
# # mycat['name'] = input()
#
# print(mycat['name'] + ' has ' + mycat['color'] + ' colored fur and is ' + mycat['size'] + ' in size')


# birthdays = {'joe': 'june 20th', 'kobby': 'april 12th', 'mercy': 'december 2nd'}
#
# while True:
#     print('Enter a name to check for date of birth:')
#     name = input()
#
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + ' is ' + name + '\'s birthday.')
#
#     else:
#         print('No info found for ' + name + '\nWhat\'s their birthday?')
#         dob = input()
#         birthdays[name] = dob
#         print('\nDatabase updated')
#
#
# spam = {'Fname': 'Tony', 'Lname': 'Asamoah', 'age': '22'}
#
# for values in spam.values():
#     print(values)
#
# for items in spam.items():
#     print(items)
#
# for keys in spam.keys():
#     print(keys)
#
# for keys, vals in spam.items():
#     print('key: ' + keys + ', Value: ' + vals)
#
# print(spam.get('Fname', 'null') + ' is ' + str(spam.get('age', 0)))
#
# spam.setdefault('Color', 'cream')
# print(spam)
#
# import pprint
#
# text = 'onomatopoeia and paprica make a good nonsense'
# index = {}
# for letter in text:
#     index.setdefault(letter, 0)
#     index[letter] = index[letter] + 1
#
# pprint.pprint(index)
# print(pprint.pformat(index))
#
# theBoard = {'1': ' ', '2': ' ', '3': ' ',
#          '4': ' ', '5': ' ', '6': ' ',
#          '7': ' ', '8': ' ', '9': ' '}
#
# def show(board):
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
# turn = 'X'
#
# for i in range(9):
#     show(theBoard)
#     print('Player ' + turn + ' Kindly play...')
#     move = input()
#     theBoard[move] = turn
#
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
#
#
# show(theBoard)
#
# Guests = {'Alice': {'Chicken': 10, 'Coke': 2},
#            'Tony': {'Pizza': 5, 'Kvacc': 10, 'Coke': 2},
#            'Kevin': {'Coke': 3, 'Pie': 5},
#            'Mary': {'Pizza': 2, 'Chicken': 5}}
#
# def netfood(name, item):
#     food = 0
#     for k, v in name.items():
#         food = food + v.get(item, 0)
#
#     return food
#
# print('Amount of food:')
# print(' - Chicken ' + str(netfood(Guests, 'Chicken')))
# print(' - Coke ' + str(netfood(Guests, 'Coke')))
# print(' - Pizza ' + str(netfood(Guests, 'Pizza')))
# print(' - Pie ' + str(netfood(Guests, 'Pie')))
# print(' - Kvacc ' + str(netfood(Guests, 'Kvacc')))
#
# spam = {'cat': 'murzik', 'color': 'red'}
#
# if 'cat' in spam:
#     print('True')
# else:
#     print('false')
#
#
# def displayInventory(inventory):
# 	print("\n", "Inventory:".center(30, "="))
# 	item_total = 0
#
# 	for k, v in inventory.items():
# 		print(f'{k.ljust(10)} {v}')
# 		item_total += v
#
# 	print(f"\nTotal number of items: {item_total}")
#
#
# def addToInv(Inventory, loot):
# 	for item in range(len(loot)):
# 		Inventory.setdefault(loot[item], 0)
# 		Inventory[loot[item]] = Inventory[loot[item]] + 1
#
#
# def newloot(loot):
# 	count = {}
# 	for item in loot:
# 		count.setdefault(item, 0)
# 		count[item] = count[item] + 1
#
# 	print(f'New loot: {count}')
#
#
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#
# addToInv(stuff, dragonLoot)
# displayInventory(stuff)
# newloot(dragonLoot)

# print(r'\n So this is a raw string...\n If you barb' + '\nignoring all backslashes and escape characters')

# print('''
# Okay
#
# So lets try the triple quote, multiline distin
# apparently, it's working :)
#
# lmao
# ''')


# print('Enter name: ')
# name = input()
#
# print(name.upper())


# # Taking in the info
# print('\nKindly input the following details;')
#
# print('\nName: ')
# name = input()
#
# print('\nYear of Birth: ')
# birthYear = input()
#
# print('\nAddress: ')
# address = input()
#
# print('\nPhone/Contact number: ')
# contact = input()
#
# currentYear = 2021
#
# # Calculating age
# age = currentYear - int(birthYear)
#
# print('\nPerson Details:\n\nName: ' + name + '\nAge: ' + str(age) + '\nAddress: '
# + address + '\nContact: ' + contact)
#
#
#
# Accepting User data
# print('\nKindly enter the following details;')
#
# print('\nName: ')
# name = input()
#
# print('\nContact (Must be not more or less than Ten(10) digits): ')
# Contact = input()
# # Check for validity, digits must not be less or more than 10
# if len(str(Contact)) != 10:
#     print('\nYou must input a valid Phone number consisting of Ten(10) digits')
#     Contact = input()
#
# print('\nNational Card Number: ')
# IDNum = input()
#
# # Working with the Currencies
# USD = 1.00
# Euro = 0.85
# Pound = 0.73
# Yuan = 6.46
# Rand = 14.28
# Cedi = 6.06
# Converted = ''
#
# # User Choosing a Currency
#
# print('\nMake a selection by inputting the number assigned to an option\n')
# print('1. USD\n'
#       '2. Euro\n'
#       '3. Pound\n'
#       '4. Yuan\n'
#       '5. Rand\n'
#       '6. Cedi\n')
#
# print('Kindly select the  currency to be converted: ')
# Base = int(input())
#
# while True:
#
#     if Base == 1:
#         # Converting from USD
#         print("\n\n"
#               '1. USD-Euro\n'
#               '2. USD-Pound\n'
#               '3. USD-Yuan\n'
#               '4. USD-Rand\n'
#               '5. USD-Cedi\n')
#
#         Second = int(input())
#         if Second == 1:
#             print('\nHow much USD?')
#             amt = float(input())
#             ans = (amt * USD) * Euro
#             Converted = str(amt) + ' USD = ' + str(ans) + ' Euro'
#             break
#
#         elif Second == 2:
#             print('\nHow much USD?')
#             amt = float(input())
#             ans = (amt * USD) * Pound
#             Converted = str(amt) + ' USD = ' + str(ans) + ' Pound'
#             break
#
#         elif Second == 3:
#             print('\nHow much USD?')
#             amt = float(input())
#             ans = (amt * USD) * Yuan
#             Converted = str(amt) + ' USD = ' + str(ans) + ' Yuan'
#             break
#
#         elif Second == 4:
#             print('\nHow much USD?')
#             amt = float(input())
#             ans = (amt * USD) * Rand
#             Converted = str(amt) + ' USD = ' + str(ans) + ' Rand'
#             break
#
#         elif Second == 5:
#             print('\nHow much USD?')
#             amt = float(input())
#             ans = (amt * USD) * Cedi
#             Converted = str(amt) + ' USD = ' + str(ans) + ' Cedi'
#             break
#
#     elif Base == 2:
#         # Converting from Euro
#         print("\n\n"
#               '1. Euro-USD\n'
#               '2. Euro-Pound\n'
#               '3. Euro-Yuan\n'
#               '4. Euro-Rand\n'
#               '5. Euro-Cedi\n')
#
#         Second = int(input())
#         if Second == 1:
#             print('\nHow much Euro?')
#             amt = float(input())
#             ans = (amt * Euro) * USD
#             Converted = str(amt) + ' Euros = ' + str(ans) + ' USD'
#             break
#
#         elif Second == 2:
#             print('\nHow much Euro?')
#             amt = float(input())
#             ans = (amt * Euro) * Pound
#             Converted = str(amt) + ' Euros = ' + str(ans) + ' Pounds'
#             break
#
#         elif Second == 3:
#             print('\nHow much Euro?')
#             amt = float(input())
#             ans = (amt * Euro) * Yuan
#             Converted = str(amt) + ' Euros = ' + str(ans) + ' Yuan'
#             break
#
#         elif Second == 4:
#             print('\nHow much Euro?')
#             amt = float(input())
#             ans = (amt * Euro) * Rand
#             Converted = str(amt) + ' Euros = ' + str(ans) + ' Rand'
#             break
#
#         elif Second == 5:
#             print('\nHow much Euro?')
#             amt = float(input())
#             ans = (amt * Euro) * Cedi
#             Converted = str(amt) + ' Euro = ' + str(ans) + ' Cedis'
#             break
#
#     elif Base == 3:
#         # Converting from Pound
#         print("\n\n"
#               '1. Pound-USD\n'
#               '2. Pound-Euro\n'
#               '3. Pound-Yuan\n'
#               '4. Pound-Rand\n'
#               '5. Pound-Cedi\n')
#
#         Second = int(input())
#         if Second == 1:
#             print('\nHow much Pound?')
#             amt = float(input())
#             ans = (amt * Pound) * USD
#             Converted = str(amt) + ' Pound = ' + str(ans) + ' USD'
#             break
#
#         elif Second == 2:
#             print('\nHow much Pound?')
#             amt = float(input())
#             ans = (amt * Pound) * Euro
#             Converted = str(amt) + ' Pound = ' + str(ans) + ' Euro'
#             break
#
#         elif Second == 3:
#             print('\nHow much Pound?')
#             amt = float(input())
#             ans = (amt * Pound) * Yuan
#             Converted = str(amt) + ' Pound = ' + str(ans) + ' Yuan'
#             break
#
#         elif Second == 4:
#             print('\nHow much Pound?')
#             amt = float(input())
#             ans = (amt * Pound) * Rand
#             Converted = str(amt) + ' Pound = ' + str(ans) + ' Rand'
#             break
#
#         elif Second == 5:
#             print('\nHow much Pound?')
#             amt = float(input())
#             ans = (amt * Pound) * Cedi
#             Converted = str(amt) + ' Pound = ' + str(ans) + ' Cedis'
#             break
#
#     elif Base == 4:
#         # Converting from Yuan
#         print("\n\n"
#               '1. Yuan-USD\n'
#               '2. Yuan-Pound\n'
#               '3. Yuan-Euro\n'
#               '4. Yuan-Rand\n'
#               '5. Yuan-Cedi\n')
#
#         Second = int(input())
#         if Second == 1:
#             print('\nHow much Yuan?')
#             amt = float(input())
#             ans = (amt * Yuan) * USD
#             Converted = str(amt) + ' Yuan = ' + str(ans) + ' USD'
#             break
#
#         elif Second == 2:
#             print('\nHow much Yuan?')
#             amt = float(input())
#             ans = (amt * Yuan) * Pound
#             Converted = str(amt) + ' Yuan = ' + str(ans) + ' Pounds'
#             break
#
#         elif Second == 3:
#             print('\nHow much Yuan?')
#             amt = float(input())
#             ans = (amt * Yuan) * Yuan
#             Converted = str(amt) + ' Yuan = ' + str(ans) + ' Euros'
#             break
#
#         elif Second == 4:
#             print('\nHow much Yuan?')
#             amt = float(input())
#             ans = (amt * Yuan) * Rand
#             Converted = str(amt) + ' Yuan = ' + str(ans) + ' Rands'
#             break
#
#         elif Second == 5:
#             print('\nHow much Yuan?')
#             amt = float(input())
#             ans = (amt * Yuan) * Cedi
#             Converted = str(amt) + ' Yuan = ' + str(ans) + ' Cedis'
#             break
#
#     elif Base == 5:
#         # Converting from Rand
#         print("\n\n"
#               '1. Rand-USD\n'
#               '2. Rand-Pound\n'
#               '3. Rand-Yuan\n'
#               '4. Rand-Euro\n'
#               '5. Rand-Cedi\n')
#
#         Second = int(input())
#         if Second == 1:
#             print('\nHow much Rand?')
#             amt = float(input())
#             ans = (amt * Rand) * USD
#             Converted = str(amt) + ' Rand = ' + str(ans) + ' USD'
#             break
#
#         elif Second == 2:
#             print('\nHow much Rand?')
#             amt = float(input())
#             ans = (amt * Rand) * Pound
#             Converted = str(amt) + ' Rand = ' + str(ans) + ' Pounds'
#             break
#
#         elif Second == 3:
#             print('\nHow much Rand?')
#             amt = float(input())
#             ans = (amt * Rand) * Yuan
#             Converted = str(amt) + ' Rand = ' + str(ans) + ' Yuan'
#             break
#
#         elif Second == 4:
#             print('\nHow much Rand?')
#             amt = float(input())
#             ans = (amt * Rand) * Rand
#             Converted = str(amt) + ' Rand = ' + str(ans) + ' Euros'
#             break
#
#         elif Second == 5:
#             print('\nHow much Rand?')
#             amt = float(input())
#             ans = (amt * Rand) * Cedi
#             Converted = str(amt) + ' Rand = ' + str(ans) + ' Cedis'
#             break
#
#     elif Base == 6:
#         # Converting from Cedi
#         print("\n\n"
#               '1. Cedi-USD\n'
#               '2. Cedi-Pound\n'
#               '3. Cedi-Yuan\n'
#               '4. Cedi-Rand\n'
#               '5. Cedi-Euro\n')
#
#         Second = int(input())
#         if Second == 1:
#             print('\nHow much Cedi?')
#             amt = float(input())
#             ans = (amt * Cedi) * USD
#             Converted = str(amt) + ' Cedi = ' + str(ans) + ' USD'
#             break
#
#         elif Second == 2:
#             print('\nHow much Cedi?')
#             amt = float(input())
#             ans = (amt * Cedi) * Pound
#             Converted = str(amt) + ' Cedi = ' + str(ans) + ' Pounds'
#             break
#
#         elif Second == 3:
#             print('\nHow much Cedi?')
#             amt = float(input())
#             ans = (amt * Cedi) * Yuan
#             Converted = str(amt) + ' Cedi = ' + str(ans) + ' Yuan'
#             break
#
#         elif Second == 4:
#             print('\nHow much Cedi?')
#             amt = float(input())
#             ans = (amt * Cedi) * Rand
#             Converted = str(amt) + ' Cedi = ' + str(ans) + ' Rands'
#             break
#
#         elif Second == 5:
#             print('\nHow much Cedi?')
#             amt = float(input())
#             ans = (amt * Cedi) * Cedi
#             Converted = str(amt) + ' Cedi = ' + str(ans) + ' Euros'
#             break
#
# # Printing User data and conversion
# print('\nUser Details:\n'
#       '_____________________________________')
# print('\nName: ' + name + '\nContact: ' + str(Contact) + '\nNational Card #: ' + IDNum +
#       '\n_____________________________________\nConversion: ' + Converted)
#
# print(r"trying another raw string with no escape characters\n like you barb?")

# print("so let's try and make something" + 'with e\'scape characters')

# print('Test\'s are interesting')

# def checker():
#     while True:
#         print('Name please? ')
#
#         name = input()
#         name = name.lower()
#
#         if 'anthony' in name:
#             break
#
#         else:
#             print('Sorry, IDK who TF you are!')
#
#     print('welcome ' + name[0].upper() + name[1:])
#
# checker()
#

# while True:
#     print('\nKindly enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#
#     print('only figures are accepted!')
#
#
# while True:
#     print('\nkindly enter a new password:')
#     pwd = input()
#     if pwd.isalpha():
#         break
#
#     print('Password must contain a mixture of letters and numbers!')


# code to change roman numerals to numbers
# unfortunately, works only with the first three numerals for now
#
# def refactorer(sentence):
#     list1 = ['1', '2', '3']
#
#     if 'i.' in sentence:
#         temp0 = sentence.index('i.')
#         temp = sentence[(1 + temp0):]
#         sentence = sentence[:temp0] + list1[0] + temp
#
#         if 'ii.' in sentence:
#             temp0 = sentence.index('ii.')
#             temp = sentence[(2 + temp0):]
#             sentence = sentence[:temp0] + list1[1] + temp
#
#             if 'iii.' in sentence:
#                 temp0 = sentence.index('iii.')
#                 temp = sentence[(3 + temp0):]
#                 sentence = sentence[:temp0] + list1[2] + temp
#
#     print('\nRefactored:\n' + sentence)
#
#
# print('\nenter a sentence:')
# sentnc = input()
#
# refactorer(sentnc)


# while True:
#
# 	user = 'anthony'
# 	password = 'onetwo3'
# 	print('\nUsername? ')
# 	spam = input()
# 	spam = spam.lower()
#
# 	if spam != user:
# 		print('Invalid Username')
# 		continue
#
# 	while True:
# 		print('\nWelcome, ' + user + '.\nKindly enter your password: ')
# 		pwd = input()
#
# 		if pwd != password:
# 			print('Invalid Password')
# 			continue
#
# 		break
#
# 	break
#
# print('\nYou have successfully logged in.')

# a function to utilize various string methods
#
#
# def tester(var):
# 	print('\n----------------------------------------')
# 	print("Testing for: ", var, '\n', sep='\t')
#
# 	print('ISUPPER: ', str(var.isupper()), sep='\t\t')
# 	print('UPPER: ', var.upper(), sep='\t\t\t')
# 	print('islower: ', str(var.islower()), sep='\t\t')
# 	print('lower: ', var.lower(), sep='\t\t\t')
# 	print('IsTitle: ', str(var.istitle()), sep='\t\t')
# 	print('Title: ', var.title(), sep='\t\t\t')
# 	print('Capitalize: ', var.capitalize(), sep='\t')
# 	print('isalnum: ', var.isalnum(), sep='\t\t')
# 	print('isalpha: ', var.isalpha(), sep='\t\t')
# 	print('isdecimal: ', var.isdecimal(), sep='\t\t')
# 	print('isspace: ', var.isspace(), sep='\t\t')
# 	print('isidentifier: ', var.isidentifier(), sep='\t')
#
#
# x = 'Hello World'
# y = "abcd123"
# z = '123'
#
# tester(x)
# tester(y)
# tester(z)

# # join method
# print('-'.join(['cats', 'dogs', 'tatas']))

# # split method
# print('Hello World, I am Tony'.split())
#
# List1 = 'Hello world, i am tony'.split(',')
# print(List1)
#
#
# text = '''Hey Babu,
# i hope you've been good?
# just wanted to check up..
# its been quite a while.
# anyways, call me when you have some time.
#
# sincerely,
# Tony'''
#
# text1 = text.split('\n')
# print(text1)

# # formatting text with center, left and right.
#
# print('Helloooo'.rjust(20))
# print('Hello?'.rjust(20))
# print('Hi'. ljust(10), 'Sup')
# print('Lol'.center(10, '-'), 'ony3')

# def printPicnic(itemsDIct, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for x, y in itemsDIct.items():
#         print(x.ljust(leftWidth, '.') + str(y).rjust(rightWidth))
#
#
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 10000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# # # stripping off whitespaece from a string
# spam = '    Hello world     '
# print('main string: ', spam)
# print(spam.strip().center(30, '-'))
# print(spam.lstrip().center(30, '-'))
# print(spam.rstrip().center(30, '-'))
#
# # note how the order of characters in the argument doesnt matter.
# # the characters passed in the argument are stripped from either ends of the string.
# spam = 'spamspamspambeaconspameggs'
# print('-----------------------------\n', spam.strip('psam'))
#
# import pyperclip
#
# print(pyperclip.paste())

# import pyperclip
# text = pyperclip.paste()
#
# lines = text.split('\n')
# for i in range(len(lines)):
# 	lines[i] = '* ' + lines[i]
#
# text = '\n'.join(lines)
# print(text)
# pyperclip.copy(text)

# Strings
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
# 			 ['Alice', 'Bob', 'Carol', 'David'],
# 			 ['dogs', 'cats', 'moose', 'goose']]
#
#
# def printtable(data):
# 	colwidth = [0] * len(data)
#
# 	# finding the maxlength of data in each column
# 	for i in range(len(colwidth)):
# 		for v in data[i]:
# 			if len(v) > colwidth[i]:
# 				colwidth[i] = len(v)
# 	# print(f'\nMax number of chars in the table are: {colwidth} ')
#
# 	print('\n', "List Items".center(colwidth[0] + colwidth[1] + colwidth[2], "*"))
# 	for i in range(len(data[0])):
# 		for v in range(len(data)):
# 			print(f'{data[v][i].ljust(colwidth[v])}', end=' ')
# 		print('')
#
#
# printtable(tableData)


# End of python Basics :)
print('Congratulations!!!!!!\n')

completed = {
	'Intro': ['variables', 'data types', 'expressions'],
	'Control flow': ['if, while & for loops', 'break and continue statements'],
	'data types': ['string', 'integer', 'float', 'boolean'],
	'functions': {
		'basic functions': ['print()', 'input()', 'len()'],
		'converters': ['int()', 'str()', 'float()'],
		'defining functions': ['def statement', 'arguments', 'return value', 'scopes']
	},

}

rspace = 20
lspace = 30

print('Python Topics'.center(lspace + rspace, "="))
for k, v in list(completed.items())[:3]:
	print(k.ljust(lspace, '.') + str(v).rjust(rspace, '='))

print('\n', 'Functions'.center(rspace + lspace, '.'))
for x, y in completed["functions"].items():
	print(x.ljust(lspace, '.') + str(y).rjust(rspace, '='))

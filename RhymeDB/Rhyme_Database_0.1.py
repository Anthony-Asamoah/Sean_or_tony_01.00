#! python

import os
import pprint
import re
import string

found_as_string = " "

def StartRDB():
	def rhymeValidator():
		while True:
			valid_input = True
			rhyme = str(input("\nKindly enter the rhyme you need.\n\t-> ")).lower()
			for letter in range(len(rhyme)):
				if rhyme[letter] not in string.ascii_letters or rhyme[letter] == 0:
					valid_input = False
			if not rhyme:
				valid_input = False

			if not valid_input:
				print("invalid input! Type in only english letters.")
				continue
			else:
				break

		return rhyme

	def find_rhymes(dictionary_path, rhyme_string):
		dictionary = open(dictionary_path, "r")
		all_text = dictionary.readlines()
		dictionary.close()
		print("searching...\n")

		temp = " ".join(all_text)

		regex = re.compile(f'\\w*{rhyme_string}\\s')
		found = regex.findall(temp)

		found = set(found)
		found = sorted(found)
		count = 0
		global found_as_string
		try:
			found_as_string += '-'.center(30, '-') + "\n"
			for words in found:
				found_as_string += f'{words}\n'.capitalize()
				count += 1
			found_as_string += '-'.center(30, '-') + "\n"
			print(found_as_string.center(30, '-'))
			print(f"{count} words found with '{rhyme_string}'")

			return count, rhyme_string, found_as_string
		except TypeError:
			print("\nNo matching rhymes found!")
			found += "Null"
			found_as_string += f'None for {rhyme_string}'
			
	rhyme = rhymeValidator()
	save_path = 'C:/users/dd/desktop/'  # default Path
	dictionary_path = "./words.txt"  # default Path for english dictionary
	count, rhyme_string, found_as_string = find_rhymes(dictionary_path, rhyme)

	return count, rhyme_string, found_as_string, save_path


def save_function(count, rhyme_string, save_path, found_as_string):
	saveTo = open(os.path.join(save_path, 'Found_Rhymes.txt'), 'w')
	saveTo.write(f'{" " * 30}{count} words found ending in "{rhyme_string}"\n\n')
	saveTo.write(found_as_string)
	saveTo.close()
	print(f"\nResults saved as 'Found_Rhymes.txt' in {save_path}")
	return True


while True:
	count, rhyme_string, found_as_string, save_path = StartRDB()

	print("\nAnother rhyme?", end=' ')

	while True:
		restart = input("reply with 'y'/'n'\n\t-> ")
		if restart:
			if restart.lower() == 'y' or 'n':
				if restart.lower() == 'y':
					Restart = True
					break
				if restart.lower() == 'n':
					Restart = False
					break
				else:
					Restart = False
					continue
			else:
				print("Invalid Input!\n")
				continue
		else:
			print("Invalid Input!\n", end=' ')

			continue
	if Restart:
		continue
	else:
		save_function(count, rhyme_string, save_path, found_as_string)
		print("\n\tThank you, goodbye...")
		break

# Todo: Get a better dictionary
# Todo: update 'found_as_string' per each iteration
# Todo: restructure entire code

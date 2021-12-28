# Practice Project 1
# Number Guessing game

# try to guess a randomly picked number in Seven tries

from random import randint
import re

# Game Begins ##########################################################
error = "\nInvalid input! Kindly enter an integer between one (1) & Hundred (100)"


def GuessingGame(hints_left):
	computer_number = randint(1, 100)

	print("\nIve got a number in mind, it's a number from one (1) to a hundred (100)\n"
		  , "Can you guess what it is...?")
	playing = True
	numbercheck = re.compile(r'\d+')

	while playing:
		while hints_left > -1 and playing:
			print(f"{hints_left} Hints Left")
			user_input = input("\n\tType 'exit' to quit or Hit enter after\n\ttyping here--> ")

			if not user_input:
				print(error)
				continue
			elif user_input.lower() == 'exit':
				playing = False
				break

			User_number = numbercheck.findall(user_input)
			try:
				user_number = int(User_number[0])
			except IndexError:
				print("\nKindly include an integer or 'exit'...")
				continue
			if 0 > len(User_number) > 1:
				print("\nplease enter only one instance of a number...")
				continue
			elif user_number > computer_number and user_number in range(1,100):
				print(f'\nOops, {user_number} is too high.')
				hints_left -= 1
			elif user_number < computer_number and user_number in range(1,100):
				print(f'\nSorry, {user_number} is a little too low:')
				hints_left -= 1
			elif user_number == computer_number:
				if hints_left > 5:
					print('\nThat\'s it! we do think alike :)')
				elif hints_left < 6:
					print('\nSpot on! But that was a lotta guessing...')
				playing = False
				break
			else:
				if user_number not in range(1, 100):
					print(error)
					continue

				break

		if playing:
			print("\nOut of Hints! Guess we don't think alike :("
				  , f"\nThe number was {computer_number}")
			break
		elif not playing:
			break

	return count


# Game Ends ##########################################################

print("\nWelcome to the number guessing game :)\nLets see if you and i think alike?")
count = 0
while True:
	if count > 2:
		print(f"{count} Games Playes!\n")
	replay = input("reply  with 'y' or 'n\n\t->").lower()
	if not replay:
		print("\nInvalid Input!")
		continue
	elif replay not in ['y', 'n']:
		print("\nInvalid Input!")
		continue
	elif replay == 'y':
		count += GuessingGame(7)
		print(f"\n\nPlay Again?")
	elif replay == 'n':
		break

print('\n\nThanks for your time...')

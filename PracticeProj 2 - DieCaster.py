from random import randint

counter = 0

def dice():
	side = randint(1,6)
	return side


print("\nThrow a die?")

while True:
	throw = input("\nReply with 'y' or 'n'\n\t-> ").lower()

	if throw in ['y','n']:
		if throw == "y":
			die = dice()
			counter += 1
			print(
				"\n\n\n",
				"".center(10, '='),
				f" < {die} > ".center(25, '-'),
				"".center(10,'='), f"\n\nRound{counter}. Go again?"
				)
			continue
		else:
			break
	else:
		print("\nInvalid Input!")
		continue

print("Goodbye...")

from random import randint


def dice():
	side = randint(1,6)
	return side


print("Throw a die?")

while True:
	throw = input("\nReply with 'y' or 'n'\n\t-> ").lower()

	if throw in ['y','n']:
		if throw == "y":
			die = dice()
			print(f"<{die}> side up!\n\nThrow another?")
			continue
		else:
			break
	else:
		print("Invalid Input!")
		continue

print("Goodbye...")

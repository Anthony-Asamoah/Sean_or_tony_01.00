# a simple program to print the fibo sequence
# and draw an x,y graph


import matplotlib.pyplot as plt
import numpy as np


def main():
	Sequence = []
	x, y = 0, 1
	z = 0
	while True:
		for i in range(5):
			Sequence.append(z)
			z = x + y
			x = y
			y = z
		print(f'Sequence: {Sequence}', end='')

		stop = input(f'\nPrint five(5) more? Y/N: ')

		if 'n' in stop.lower():
			break

	ypoints = np.array(Sequence)

	plt.plot(ypoints, ".:r")

	plt.title("Fibo graph")
	plt.grid(axis="y")

	plt.show()


if __name__ == '__main__':
	main()

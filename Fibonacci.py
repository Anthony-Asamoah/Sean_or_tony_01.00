# a simple program to print the fibo sequence
# and draw an x,y grapyh

from typing import Sequence
import matplotlib.pyplot as plt
import numpy as np

Sequence = [0, 1]
x, y = 0, 1

while True:
	for i in range(5):

		x = y
		y = x + y
		Sequence.append(x)

	print(f'Sequence: {Sequence}', end='')

	stop = input(f'\nPrint five(5) more? Y/N: ')

	if stop.lower() =='n':
		break


ypoints = np.array(Sequence)

plt.plot(ypoints, ".:r")

plt.title("Fibo graph")
plt.grid(axis= "y")

plt.show()
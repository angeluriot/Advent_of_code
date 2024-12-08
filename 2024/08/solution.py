import math
import numpy as np

with open('2024/08/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

map = np.array([list(line) for line in data])
antinodes = np.zeros(map.shape, dtype=int)
symbols = np.unique(map).tolist()
symbols.remove('.')

for symbol in symbols:
	positions = np.argwhere(map == symbol)

	for i in range(positions.shape[0]):
		for j in range(positions.shape[0]):
			if i == j:
				continue

			antinode = positions[i] + (positions[i] - positions[j])

			if antinode[0] >= 0 and antinode[0] < antinodes.shape[0] and antinode[1] >= 0 and antinode[1] < antinodes.shape[1]:
				antinodes[antinode[0], antinode[1]] = 1

total = np.sum(antinodes)

with open('2024/08/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

for symbol in symbols:
	positions = np.argwhere(map == symbol)

	for i in range(positions.shape[0]):
		for j in range(positions.shape[0]):
			if i == j:
				continue

			vector = positions[i] - positions[j]
			vector //= math.gcd(vector[0], vector[1])
			antinode = positions[i].copy()

			while antinode[0] >= 0 and antinode[0] < antinodes.shape[0] and antinode[1] >= 0 and antinode[1] < antinodes.shape[1]:
				antinodes[antinode[0], antinode[1]] = 1
				antinode += vector

total = np.sum(antinodes)

with open('2024/08/output_2.txt', 'w') as f:
	f.write(str(total))

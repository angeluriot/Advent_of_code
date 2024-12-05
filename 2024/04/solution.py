import numpy as np

with open('2024/04/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

grid = np.pad(np.array([list(d) for d in data]), ((0, 4), (0, 4)))
dir_to_idx = {-1: np.flip(np.arange(4, dtype=int)), 0: np.zeros(4, dtype=int), 1: np.arange(4, dtype=int)}
directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
indices = [(dir_to_idx[x], dir_to_idx[y]) for x, y in directions]
nb = 0

for x in range(grid.shape[0] - 3):
	for y in range(grid.shape[1] - 3):
		nb += len([0 for xs, ys in indices if ''.join(grid[(x + xs).tolist(), (y + ys).tolist()]) == 'XMAS'])

with open('2024/04/output_1.txt', 'w') as f:
	f.write(str(nb))

# Part 2

dir_to_idx = {-1: np.flip(np.arange(3, dtype=int)) - 1, 1: np.arange(3, dtype=int) - 1}
directions_1 = [(1, 1), (-1, -1)]
directions_2 = [(1, -1), (-1, 1)]
indices_1 = [(dir_to_idx[x], dir_to_idx[y]) for x, y in directions_1]
indices_2 = [(dir_to_idx[x], dir_to_idx[y]) for x, y in directions_2]
nb = 0

for x in range(1, grid.shape[0] - 1):
	for y in range(1, grid.shape[1] - 1):
		if all(any(''.join(grid[(x + xs).tolist(), (y + ys).tolist()]) == 'MAS' for xs, ys in indices) for indices in [indices_1, indices_2]):
			nb += 1

with open('2024/04/output_2.txt', 'w') as f:
	f.write(str(nb))

import numpy as np

with open('2024/10/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

map = np.array([[int(cell) for cell in list(line)] for line in data])
starts = np.argwhere(map == 0)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
trails = [[] for _ in range(len(starts))]

def search(position, start_i):
	if map[position[0], position[1]] == 9:
		trails[start_i].append(position)
		return

	for x, y in directions:
		new_position = (position[0] + x, position[1] + y)

		if (
			0 <= new_position[0] < map.shape[0] and 0 <= new_position[1] < map.shape[1]
			and map[new_position[0], new_position[1]] - map[position[0], position[1]] == 1
		):
			search(new_position, start_i)

for i, start in enumerate(starts):
	search(tuple(start), i)

total = sum(len(set(trail)) for trail in trails)

with open('2024/10/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

total = sum(len(trail) for trail in trails)

with open('2024/10/output_2.txt', 'w') as f:
	f.write(str(total))

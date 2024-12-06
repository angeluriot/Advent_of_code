import numpy as np

with open('2024/06/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

map = np.transpose(np.array([list(line) for line in data]), (1, 0))
position = [int(index[0]) for index in np.where(map == '^')]
map[position[0], position[1]] = 'X'
direction_i = 0
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

while True:
	direction = directions[direction_i]
	next_position = (position[0] + direction[0], position[1] + direction[1])

	if next_position[0] < 0 or next_position[0] >= map.shape[0] or next_position[1] < 0 or next_position[1] >= map.shape[1]:
		break

	if map[next_position[0], next_position[1]] == '#':
		direction_i = (direction_i + 1) % 4
	else:
		position = next_position
		map[position[0], position[1]] = 'X'

visited = np.count_nonzero(map == 'X')

with open('2024/06/output_1.txt', 'w') as f:
	f.write(str(visited))

# Part 2

object_positions = [(int(x), int(y)) for x, y in zip(*np.where(map == 'X'))]
map = np.transpose(np.array([list(line) for line in data]), (1, 0))
start_position = [int(index[0]) for index in np.where(map == '^')]
obstructions = 0

for x, y in object_positions:
	copy = map.copy()
	copy[x, y] = '#'
	position = start_position.copy()
	copy[position[0], position[1]] = '0'
	direction_i = 0

	while True:
		direction = directions[direction_i]
		next_position = (position[0] + direction[0], position[1] + direction[1])

		if next_position[0] < 0 or next_position[0] >= copy.shape[0] or next_position[1] < 0 or next_position[1] >= copy.shape[1]:
			break

		if copy[next_position[0], next_position[1]] == str(direction_i):
			obstructions += 1
			break

		if copy[next_position[0], next_position[1]] == '#':
			direction_i = (direction_i + 1) % 4
		else:
			position = next_position
			copy[position[0], position[1]] = str(direction_i)

with open('2024/06/output_2.txt', 'w') as f:
	f.write(str(obstructions))

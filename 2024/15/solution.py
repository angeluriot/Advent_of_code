import numpy as np

with open('2024/15/input.txt', 'r') as f:
	data = f.read()

# Part 1

moves = list(data.split('\n\n')[1].replace('\n', ''))
directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
map = np.transpose(np.array([list(line) for line in data.split('\n\n')[0].splitlines()]), (1, 0))
position = tuple(np.argwhere(map == '@').tolist()[0])
elements = {position: '@'}
elements.update({tuple(box): 'O' for box in np.argwhere(map == 'O').tolist()})
elements.update({tuple(wall): '#' for wall in np.argwhere(map == '#').tolist()})

def move_element(position, direction):
	if position not in elements:
		return True

	if elements[position] == '#':
		return False

	next_position = (position[0] + direction[0], position[1] + direction[1])

	if not move_element(next_position, direction):
		return False

	elements[next_position] = elements[position]
	elements.pop(position)

	return True

for move in moves:
	direction = directions[move]

	if move_element(position, direction):
		position = (position[0] + direction[0], position[1] + direction[1])

total = sum([element[0] + 100 * element[1] for element in elements if elements[element] == 'O'])

with open('2024/15/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

map_data = data.split('\n\n')[0].replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.').splitlines()
map = np.transpose(np.array([list(line) for line in map_data]), (1, 0))
position = tuple(np.argwhere(map == '@').tolist()[0])
elements = {position: '@'}
elements.update({tuple(box): '[' for box in np.argwhere(map == '[').tolist()})
elements.update({tuple(box): ']' for box in np.argwhere(map == ']').tolist()})
elements.update({tuple(wall): '#' for wall in np.argwhere(map == '#').tolist()})
total = 0

def move_big_element(position, direction, check = False, apply = False):
	if position not in elements:
		return True

	if elements[position] == '#':
		return False

	positions = [position]

	if direction[0] == 0:
		if elements[position] == '[':
			positions.append((position[0] + 1, position[1]))
		elif elements[position] == ']':
			positions.append((position[0] - 1, position[1]))

	if check and any([not move_big_element((p[0] + direction[0], p[1] + direction[1]), direction, check=True) for p in positions]):
		return False

	if apply:
		for p in positions:
			next_p = (p[0] + direction[0], p[1] + direction[1])
			move_big_element(next_p, direction, apply=True)
			assert next_p not in elements
			elements[next_p] = elements[p]
			elements.pop(p)

	return True

for move in moves:
	direction = directions[move]

	if move_big_element(position, direction, check=True, apply=True):
		position = (position[0] + direction[0], position[1] + direction[1])

total = sum([element[0] + 100 * element[1] for element in elements if elements[element] == '['])

with open('2024/15/output_2.txt', 'w') as f:
	f.write(str(total))

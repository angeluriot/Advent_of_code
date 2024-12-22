import numpy as np

with open('2024/21/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
numeric_keypad = np.array([['7', '4', '1', ' '], ['8', '5', '2', '0'], ['9', '6', '3', 'A']])
directional_keypad = np.array([[' ', '<'], ['^', 'v'], ['A', '>']])
keypads = [numeric_keypad, directional_keypad]

def get_all_paths(keypad, start, end):
	if start == end:
		return ['A']

	distance_x = end[0] - start[0]
	distance_y = end[1] - start[1]
	path = ''

	if distance_x > 0:
		path = path + ('>' * distance_x)
	elif distance_x < 0:
		path = path + ('<' * abs(distance_x))

	if distance_y > 0:
		path = path + ('v' * distance_y)
	elif distance_y < 0:
		path = path + ('^' * abs(distance_y))

	paths = []

	if path == path[::-1]:
		return [path + 'A']

	if keypad[end[0], start[1]] != ' ':
		paths.append(path + 'A')

	if keypad[start[0], end[1]] != ' ':
		paths.append(path[::-1] + 'A')

	return paths

def get_all_paths_sequence(keypad, sequence):
	paths = ['']
	position = tuple(np.argwhere(keypad == 'A')[0].tolist())

	for key in sequence:
		next = tuple(np.argwhere(keypad == key)[0].tolist())
		local_paths = get_all_paths(keypad, position, next)
		temp = []

		for path in paths:
			for local_path in local_paths:
				temp.append(path + local_path)

		paths = temp
		position = next

	return paths

def get_shortest_size(keypad, sequence, depth):
	if sequence in memory[depth]:
		return memory[depth][sequence]

	if depth == 0:
		memory[depth][sequence] = len(sequence)
		return len(sequence)

	if sequence.count('A') == 1:
		actions_list = get_all_paths_sequence(keypad, sequence)
		min_size = None

		for actions in actions_list:
			size = get_shortest_size(directional_keypad, actions, depth - 1)

			if min_size is None or size < min_size:
				min_size = size

		memory[depth][sequence] = min_size
		return min_size

	parts = sequence.split('A')

	if len(parts) > 0 and parts[-1] == '':
		parts = parts[:-1]

	parts = [part + 'A' for part in parts]
	nb_actions = 0

	for part in parts:
		nb_actions += get_shortest_size(keypad, part, depth)

	memory[depth][sequence] = nb_actions
	return nb_actions

memory = [{} for _ in range(4)]
total = 0

for sequence in data:
	shortest = get_shortest_size(numeric_keypad, sequence, 3)
	total += shortest * int(sequence[:-1])

with open('2024/21/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

memory = [{} for _ in range(27)]
total = 0

for sequence in data:
	shortest = get_shortest_size(numeric_keypad, sequence, 26)
	total += shortest * int(sequence[:-1])

with open('2024/21/output_2.txt', 'w') as f:
	f.write(str(total))

import random

with open('2024/24/input.txt', 'r') as f:
	data = f.read()

# Part 1

init_wires = {}
init_connections = {}

for line in data.split('\n\n')[0].splitlines():
	name, value = line.split(': ')
	init_wires[name] = int(value)

for line in data.split('\n\n')[1].splitlines():
	connection, output = line.split(' -> ')
	input_1, operator, input_2 = connection.split(' ')
	init_connections[output] = {'op': operator, '1': input_1, '2': input_2}

	for wire in [input_1, input_2, output]:
		if wire not in init_wires:
			init_wires[wire] = None

wires = init_wires.copy()
connections = init_connections.copy()

def get_value(wire, wires, connections):
	if wires[wire] is not None:
		return wires[wire]

	connection = connections[wire]

	if connection['op'] == 'OR':
		value = get_value(connection['1'], wires, connections) | get_value(connection['2'], wires, connections)
	elif connection['op'] == 'AND':
		value = get_value(connection['1'], wires, connections) & get_value(connection['2'], wires, connections)
	else:
		value = get_value(connection['1'], wires, connections) ^ get_value(connection['2'], wires, connections)

	wires[wire] = value
	return value

def get_output(wires, connections):
	for wire in wires:
		wires[wire] = get_value(wire, wires, connections)

	i = 0
	output = ''

	while True:
		wire = 'z' + str(i).zfill(2)

		if wire not in wires:
			break

		output += str(wires[wire])
		i += 1

	return output

output = get_output(wires, connections)
output_size = len(output)
input_size = output_size - 1
output = int(output[::-1], 2)

with open('2024/24/output_1.txt', 'w') as f:
	f.write(str(output))

# Part 2

wires = init_wires.copy()
connections = init_connections.copy()

def get_previous_connections(wire, connections, depth):
	if wire not in connections or depth == 0:
		return set()

	connection = connections[wire]
	p_connections = set([wire])
	p_connections.update(get_previous_connections(connection['1'], connections, depth - 1))
	p_connections.update(get_previous_connections(connection['2'], connections, depth - 1))

	return p_connections

def get_first_error_i(connections):
	min_i = None

	for _ in range(100):
		wires = init_wires.copy()
		x_rand = bin(random.randint(0, 2**input_size - 1))[2:].zfill(input_size)[::-1]
		y_rand = bin(random.randint(0, 2**input_size - 1))[2:].zfill(input_size)[::-1]

		for i in range(input_size):
			wires['x' + str(i).zfill(2)] = int(x_rand[i])
			wires['y' + str(i).zfill(2)] = int(y_rand[i])

		target = bin(int(x_rand[::-1], 2) + int(y_rand[::-1], 2))[2:].zfill(output_size)[::-1]
		output = get_output(wires, connections)

		for i in range(output_size):
			if output[i] != target[i]:
				if min_i is None or i < min_i:
					min_i = i
				break

	return min_i

fixed_connections = connections.copy()
swaps = []
i = get_first_error_i(connections)

while i is not None:
	wire = 'z' + str(i).zfill(2)
	previous = list(get_previous_connections(wire, connections, 3))
	new_i = False

	for first in previous:
		for second in connections.keys():
			if first == second:
				continue

			test_connections = fixed_connections.copy()
			test_connections[first], test_connections[second] = test_connections[second], test_connections[first]

			try:
				next_i = get_first_error_i(test_connections)
			except RecursionError:
				next_i = -1

			if next_i is None or next_i > i:
				fixed_connections = test_connections.copy()
				swaps.extend([first, second])
				new_i = True
				break

		if new_i:
			break

	i = next_i

with open('2024/24/output_2.txt', 'w') as f:
	f.write(','.join(sorted(swaps)))

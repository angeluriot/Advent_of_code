with open('2024/17/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

program = list(map(int, data[4].split(': ')[1].split(',')))
init_variables = {
	'a': int(data[0].split(': ')[1]),
	'b': int(data[1].split(': ')[1]),
	'c': int(data[2].split(': ')[1]),
	'pointer': 0
}
combo = {
	0: lambda: 0, 1: lambda: 1, 2: lambda: 2, 3: lambda: 3,
	4: lambda: variables['a'], 5: lambda: variables['b'], 6: lambda: variables['c']
}

variables = init_variables.copy()
output = []

def instruction(id, operand):
	match id:
		case 0:
			variables['a'] = int(variables['a'] / (2 ** combo[operand]()))
			variables['pointer'] += 2
		case 1:
			variables['b'] = variables['b'] ^ operand
			variables['pointer'] += 2
		case 2:
			variables['b'] = combo[operand]() % 8
			variables['pointer'] += 2
		case 3:
			if variables['a'] != 0:
				variables['pointer'] = operand
			else:
				variables['pointer'] += 2
		case 4:
			variables['b'] = variables['b'] ^ variables['c']
			variables['pointer'] += 2
		case 5:
			output.append(combo[operand]() % 8)
			variables['pointer'] += 2
		case 6:
			variables['b'] = int(variables['a'] / (2 ** combo[operand]()))
			variables['pointer'] += 2
		case 7:
			variables['c'] = int(variables['a'] / (2 ** combo[operand]()))
			variables['pointer'] += 2

while variables['pointer'] < len(program) - 1:
	instruction(program[variables['pointer']], program[variables['pointer'] + 1])

with open('2024/17/output_1.txt', 'w') as f:
	f.write(','.join(map(str, output)))

# Part 2

def get_register_a(previous, first = False):
	for i in range(2 ** 6 if first else 2 ** 3):
		variables['a'] = init_variables['a']
		variables['b'] = init_variables['b']
		variables['c'] = init_variables['c']
		variables['pointer'] = 0
		output.clear()
		test_a = previous + bin(i)[2:].zfill(0 if first else 3)
		variables['a'] = int(test_a, 2)

		while variables['pointer'] < len(program) - 1:
			instruction(program[variables['pointer']], program[variables['pointer'] + 1])

		if output == program:
			return int(test_a, 2)

		if len(output) <= len(program) and output == program[-len(output):]:
			possible_a = get_register_a(test_a, False)

			if possible_a is not None:
				return possible_a

	return None

register_a = get_register_a('', True)

with open('2024/17/output_2.txt', 'w') as f:
	f.write(str(register_a))

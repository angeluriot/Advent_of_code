with open('2024/19/input.txt', 'r') as f:
	data = f.read()

# Part 1

towels = set(data.split('\n\n')[0].split(', '))
designs = data.split('\n\n')[1].splitlines()

def is_possible(design):
	if design in towels:
		return True

	for i in range(1, len(design)):
		if design[:i] in towels and is_possible(design[i:]):
			return True

	return False

total = len([design for design in designs if is_possible(design)])

with open('2024/19/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

memory = {}

def nb_arrangements(design):
	if design in memory:
		return memory[design]

	nb = 0

	if design in towels:
		nb = 1

	for i in range(1, len(design)):
		if design[:i] in towels:
			nb += nb_arrangements(design[i:])

	memory[design] = nb

	return nb

total = sum([nb_arrangements(design) for design in designs])

with open('2024/19/output_2.txt', 'w') as f:
	f.write(str(total))

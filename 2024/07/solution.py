with open('2024/07/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

equations = [{'result': int(equation.split(': ')[0]), 'values': [int(value) for value in equation.split(': ')[1].split(' ')]} for equation in data]
total = 0

for equation in equations:
	simplifieds = [equation['values'].copy()]

	while len(simplifieds[0]) > 1:
		initial_length = len(simplifieds)
		for i in range(initial_length):
			simplifieds.append([simplifieds[i][0] * simplifieds[i][1]] + simplifieds[i][2:])
			simplifieds[i] = [simplifieds[i][0] + simplifieds[i][1]] + simplifieds[i][2:]

	simplifieds = [simplified[0] for simplified in simplifieds]

	if equation['result'] in simplifieds:
		total += equation['result']

with open('2024/07/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

total = 0

for equation in equations:
	simplifieds = [equation['values'].copy()]

	while len(simplifieds[0]) > 1:
		initial_length = len(simplifieds)
		for i in range(initial_length):
			simplifieds.append([simplifieds[i][0] * simplifieds[i][1]] + simplifieds[i][2:])
			simplifieds.append([int(f'{simplifieds[i][0]}{simplifieds[i][1]}')] + simplifieds[i][2:])
			simplifieds[i] = [simplifieds[i][0] + simplifieds[i][1]] + simplifieds[i][2:]

	simplifieds = [simplified[0] for simplified in simplifieds]

	if equation['result'] in simplifieds:
		total += equation['result']

with open('2024/07/output_2.txt', 'w') as f:
	f.write(str(total))

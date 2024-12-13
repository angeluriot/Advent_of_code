import re

with open('2024/13/input.txt', 'r') as f:
	data = f.read()

# Part 1

machines = []

for machine in data.split('\n\n'):
	button_a, button_b, prize = machine.split('\n')[:3]

	machines.append({
		'a': tuple(map(int, re.findall(r'\d+', button_a))),
		'b': tuple(map(int, re.findall(r'\d+', button_b))),
		'prize': tuple(map(int, re.findall(r'\d+', prize))),
	})

def get_total():
	total = 0

	for machine in machines:
		nb_a = (machine['prize'][1] * machine['b'][0] - machine['prize'][0] * machine['b'][1]) / (machine['a'][1] * machine['b'][0] - machine['a'][0] * machine['b'][1])
		nb_b = (machine['prize'][0] - nb_a * machine['a'][0]) / machine['b'][0]

		if nb_a >= 0 and nb_b >= 0 and nb_a.is_integer() and nb_b.is_integer():
			total += int(nb_a) * 3 + int(nb_b)

	return total

total = get_total()

with open('2024/13/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

for i, machine in enumerate(machines):
	machines[i]['prize'] = (machine['prize'][0] + 10000000000000, machine['prize'][1] + 10000000000000)

total = get_total()

with open('2024/13/output_2.txt', 'w') as f:
	f.write(str(total))

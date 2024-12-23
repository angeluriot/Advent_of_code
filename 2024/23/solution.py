with open('2024/23/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

computers = {}

for link in data:
	connection = link.split('-')
	computers[connection[0]] = computers.get(connection[0], []) + [connection[1]]
	computers[connection[1]] = computers.get(connection[1], []) + [connection[0]]

groups = set()

for computer, linked in computers.items():
	for i in range(len(linked)):
		for j in range(len(linked)):
			if i != j and linked[i] in computers[linked[j]]:
				group = sorted([computer, linked[i], linked[j]])
				groups.add(f'.{group[0]}.{group[1]}.{group[2]}')

total = len([group for group in groups if '.t' in group])

with open('2024/23/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

groups = [[c] for c in list(computers.keys())]

for computer, linked in computers.items():
	for group in groups:
		if all([c in linked for c in group]):
			group.append(computer)

groups.sort(key=lambda x: len(x), reverse=True)
password = ','.join(sorted(groups[0]))

with open('2024/23/output_2.txt', 'w') as f:
	f.write(password)

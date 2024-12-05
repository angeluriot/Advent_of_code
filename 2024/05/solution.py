from functools import cmp_to_key

with open('2024/05/input.txt', 'r') as f:
	data = f.read()

# Part 1

updates = [[int(page) for page in update.split(',')] for update in data.split('\n\n')[1].splitlines()]
rules = [[int(page) for page in rule.split('|')] for rule in data.split('\n\n')[0].splitlines()]
before = {}

for rule in rules:
	before[rule[1]] = before.get(rule[1], []) + [rule[0]]

total = 0

for update in updates:
	if all(update[i + 1] not in before.get(update[i], []) for i in range(len(update) - 1)):
		total += update[int(len(update) / 2)]

with open('2024/05/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

total = 0

for update in updates:
	if any(update[i + 1] in before.get(update[i], []) for i in range(len(update) - 1)):
		total += sorted(update, key=cmp_to_key(lambda x, y: 1 if y in before.get(x, []) else -1))[int(len(update) / 2)]

with open('2024/05/output_2.txt', 'w') as f:
	f.write(str(total))

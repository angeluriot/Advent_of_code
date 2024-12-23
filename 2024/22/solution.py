with open('2024/22/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

def mix(secret, value):
	return secret ^ value

def prune(secret):
	return secret % 16777216

def next(secret):
	secret = mix(secret, secret * 64)
	secret = prune(secret)

	secret = mix(secret, int(secret / 32))
	secret = prune(secret)

	secret = mix(secret, secret * 2048)
	secret = prune(secret)

	return secret

prices = []
changes = []
total = 0

for secret in map(int, data):
	prices.append([])
	changes.append([])

	for _ in range(2000):
		temp = int(str(secret)[-1])
		secret = next(secret)
		prices[-1].append(temp)
		changes[-1].append(int(str(secret)[-1]) - temp)

	total += secret

with open('2024/22/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

totals = {}

for i in range(len(changes)):
	memory = set()

	for j in range(4, 2000):
		sequence = tuple(changes[i][j - 4:j])

		if sequence not in memory:
			totals[sequence] = totals.get(sequence, 0) + prices[i][j]
			memory.add(sequence)

total = max(totals.values())

with open('2024/22/output_2.txt', 'w') as f:
	f.write(str(total))

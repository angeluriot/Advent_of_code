with open('2024/09/input.txt', 'r') as f:
	data = f.read()

# Part 1

disk_map = [int(value) for value in data[:-1]]
disk = []
id = 0

for i, value in enumerate(disk_map):
	if i % 2 == 0:
		disk.extend([id] * value)
		id += 1
	else:
		disk.extend([-1] * value)

compacted_disk = disk.copy()

for i in range(len(compacted_disk)):
	if i >= len(compacted_disk):
		break

	if compacted_disk[i] == -1:
		for j in range(len(compacted_disk) - 1, -1, -1):
			if i >= len(compacted_disk):
				break

			if compacted_disk[j] >= 0:
				compacted_disk[i] = compacted_disk[j]
				compacted_disk.pop()
				break

			compacted_disk.pop()

total = sum([i * value for i, value in enumerate(compacted_disk)])

with open('2024/09/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

structured_disk = []
id = 0

for i, value in enumerate(disk_map):
	if i % 2 == 0:
		structured_disk.append([id] * value)
		id += 1
	elif value > 0:
		structured_disk.append([-1] * value)

for i in range(len(structured_disk)):
	if i >= len(structured_disk):
		break

	if structured_disk[i][0] == -1:
		for j in range(len(structured_disk) - 1, i, -1):
			if i >= len(structured_disk) or -1 not in structured_disk[i]:
				break

			if structured_disk[j][0] >= 0 and structured_disk[i].count(-1) >= len(structured_disk[j]):
					start = structured_disk[i].index(-1)
					structured_disk[i][start:start + len(structured_disk[j])] = structured_disk[j]
					structured_disk[j] = [-2] * len(structured_disk[j])

			if j == len(structured_disk) - 1 and structured_disk[j][0] == -1:
				structured_disk.pop()

compacted_disk = [value for sublist in structured_disk for value in sublist]
total = sum([i * max(value, 0) for i, value in enumerate(compacted_disk)])

with open('2024/09/output_2.txt', 'w') as f:
	f.write(str(total))

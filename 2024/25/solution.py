import numpy as np

with open('2024/25/input.txt', 'r') as f:
	data = f.read()

# Part 1

locks = []
keys = []

for schema in data.split('\n\n'):
	np_schema = np.transpose(np.array([list(row) for row in schema.splitlines()]), (1, 0))
	heights = []

	for x in range(np_schema.shape[0]):
		heights.append(np.count_nonzero(np_schema[x, :] == '#'))

	if np.count_nonzero(np_schema[:, 0] == '#') == 0:
		keys.append(heights)
	else:
		locks.append(heights)

total = 0

for lock in locks:
	for key in keys:
		if all([lock[i] + key[i] <= 7 for i in range(len(lock))]):
			total += 1

with open('2024/25/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

# 🎅

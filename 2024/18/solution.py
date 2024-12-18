import numpy as np

with open('2024/18/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

size = (71, 71)
grid = np.full(size, '.')
scores = np.full(size, -1, dtype=int)
start = (0, 0)
end = (size[0] - 1, size[1] - 1)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(1024):
	x, y = tuple(map(int, data[i].split(',')))
	grid[x, y] = '#'

def fill_scores(x, y, current=0):
	if scores[x, y] != -1 and scores[x, y] <= current:
		return

	scores[x, y] = current

	for direction in directions:
		dx, dy = x + direction[0], y + direction[1]

		if dx >= 0 and dx < size[0] and dy >= 0 and dy < size[1] and grid[dx, dy] != '#':
			fill_scores(dx, dy, current + 1)

fill_scores(start[0], start[1])
min_steps = scores[end[0], end[1]]

with open('2024/18/output_1.txt', 'w') as f:
	f.write(str(min_steps))

# Part 2

def fill(x, y):
	if visited[x, y]:
		return

	visited[x, y] = True

	for direction in directions:
		dx, dy = x + direction[0], y + direction[1]

		if dx >= 0 and dx < size[0] and dy >= 0 and dy < size[1] and grid[dx, dy] != '#':
			fill(dx, dy)

for i in range(1024, len(data)):
	x, y = tuple(map(int, data[i].split(',')))
	grid[x, y] = '#'
	visited = np.full(size, False)

	fill(start[0], start[1])

	if not visited[end[0], end[1]]:
		blocker = (x, y)
		break

with open('2024/18/output_2.txt', 'w') as f:
	f.write(f'{blocker[0]},{blocker[1]}')

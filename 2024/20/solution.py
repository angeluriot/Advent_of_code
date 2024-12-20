import numpy as np

with open('2024/20/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

grid = np.transpose(np.array([list(line) for line in data]), (1, 0))
scores = np.full((grid.shape[0], grid.shape[1], 2), -1, dtype=int)
start = tuple(np.argwhere(grid == 'S')[0].tolist())
end = tuple(np.argwhere(grid == 'E')[0].tolist())
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def fill_scores(x, y, z, current=0):
	if scores[x, y, z] != -1 and scores[x, y, z] <= current:
		return

	scores[x, y, z] = current

	for direction in directions:
		dx, dy = x + direction[0], y + direction[1]

		if grid[dx, dy] != '#':
			fill_scores(dx, dy, z, current + 1)

fill_scores(start[0], start[1], 0)
fill_scores(end[0], end[1], 1)
min_legit = scores[end[0], end[1], 0]

def get_nb_cheats(steps, min_save):
	total = 0

	for x_1 in range(1, grid.shape[0] - 1):
		for y_1 in range(1, grid.shape[1] - 1):
			if grid[x_1, y_1] != '#' and scores[x_1, y_1, 0] != -1 and scores[x_1, y_1, 0] < min_legit - min_save:
				for x_2 in range(x_1 - steps, x_1 + steps + 1):
					for y_2 in range(y_1 - steps, y_1 + steps + 1):
						distance = abs(x_1 - x_2) + abs(y_1 - y_2)

						if (
							0 <= x_2 < grid.shape[0] and
							0 <= y_2 < grid.shape[1] and
							2 <= distance <= steps and
							grid[x_2, y_2] != '#' and
							scores[x_2, y_2, 0] != -1 and
							scores[x_1, y_1, 0] + distance + scores[x_2, y_2, 1] <= min_legit - min_save
						):
							total += 1

	return total

nb_cheats = get_nb_cheats(2, 100)

with open('2024/20/output_1.txt', 'w') as f:
	f.write(str(nb_cheats))

# Part 2

nb_cheats = get_nb_cheats(20, 100)

with open('2024/20/output_2.txt', 'w') as f:
	f.write(str(nb_cheats))

import numpy as np
import sys

sys.setrecursionlimit(10_000)

with open('2024/16/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

maze = np.transpose(np.array([list(line) for line in data]), (1, 0))
scores = np.full((maze.shape[0], maze.shape[1], 4), -1, dtype=int)
start = tuple(np.argwhere(maze == 'S')[0].tolist())
end = tuple(np.argwhere(maze == 'E')[0].tolist())
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def fill_scores(x, y, direction_i = 0, current_score = 0):
	if scores[x, y, direction_i] != -1 and scores[x, y, direction_i] <= current_score:
		return

	scores[x, y, direction_i] = current_score

	nexts = [
		(x, y, (direction_i - 1) % 4, 1000),
		(x, y, (direction_i + 1) % 4, 1000),
		(x + directions[direction_i][0], y + directions[direction_i][1], direction_i, 1)
	]

	for dx, dy, d_i, to_add in nexts:
		if maze[dx, dy] != '#':
			fill_scores(dx, dy, d_i, current_score + to_add)

fill_scores(start[0], start[1])
min_score = min(list(filter(lambda x: x != -1, scores[end[0], end[1], :].flatten().tolist())))

with open('2024/16/output_1.txt', 'w') as f:
	f.write(str(min_score))

# Part 2

paths = np.full(scores.shape, 0, dtype=int)

def fill_paths(x, y, direction_i):
	if paths[x, y, direction_i] == 1:
		return

	paths[x, y, direction_i] = 1
	inverse_direction = directions[(direction_i + 2) % 4]

	nexts = [
		(x, y, (direction_i - 1) % 4),
		(x, y, (direction_i + 1) % 4),
		(x + inverse_direction[0], y + inverse_direction[1], direction_i)
	]

	for dx, dy, d_i in nexts:
		if scores[dx, dy, d_i] != -1 and scores[dx, dy, d_i] < scores[x, y, direction_i]:
			fill_paths(dx, dy, d_i)

for direction_i in range(4):
	if scores[end[0], end[1], direction_i] == min_score:
		fill_paths(end[0], end[1], direction_i)

nb_path_tiles = np.sum(np.clip(paths.sum(axis=2), 0, 1))

with open('2024/16/output_2.txt', 'w') as f:
	f.write(str(nb_path_tiles))

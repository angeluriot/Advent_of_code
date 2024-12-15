import numpy as np

with open('2024/14/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

init_robots = []
x_size = 101
y_size = 103

for line in data:
	position_x, position_y = tuple(map(int, line.split(' ')[0][2:].split(',')))
	velocity_x, velocity_y = tuple(map(int, line.split(' ')[1][2:].split(',')))
	init_robots.append({'position': (position_x, position_y), 'velocity': (velocity_x, velocity_y)})

robots = [robot.copy() for robot in init_robots]

for _ in range(100):
	for robot in robots:
		robot['position'] = (
			(robot['position'][0] + robot['velocity'][0]) % x_size,
			(robot['position'][1] + robot['velocity'][1]) % y_size
		)

parts = [0, 0, 0, 0]

for robot in robots:
	if robot['position'][0] < x_size // 2 and robot['position'][1] < y_size // 2:
		parts[0] += 1
	elif robot['position'][0] < x_size // 2 and robot['position'][1] > y_size // 2:
		parts[1] += 1
	elif robot['position'][0] > x_size // 2 and robot['position'][1] < y_size // 2:
		parts[2] += 1
	elif robot['position'][0] > x_size // 2 and robot['position'][1] > y_size // 2:
		parts[3] += 1

total = parts[0] * parts[1] * parts[2] * parts[3]

with open('2024/14/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

min_std = None
min_std_i = 0

robots = [robot.copy() for robot in init_robots]

for i in range(10_000):
	for robot in robots:
		robot['position'] = (
			(robot['position'][0] + robot['velocity'][0]) % x_size,
			(robot['position'][1] + robot['velocity'][1]) % y_size
		)

	std = np.std([robot['position'][0] for robot in robots]) + np.std([robot['position'][1] for robot in robots])

	if min_std is None or std < min_std:
		min_std = std
		min_std_i = i

with open('2024/14/output_2.txt', 'w') as f:
	f.write(str(min_std_i + 1))

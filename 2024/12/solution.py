import numpy as np

with open('2024/12/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

map = np.array([list(row) for row in data])
plants = {(x, y) for x in range(map.shape[0]) for y in range(map.shape[1])}
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
regions = []

def get_region(x, y, region = None):
	if region is None:
		region = {}

	region[(x, y)] = {direction: 1 for direction in directions}
	plants.discard((x, y))

	for dx, dy in directions:
		next_x, next_y = x + dx, y + dy

		if 0 <= next_x < map.shape[0] and 0 <= next_y < map.shape[1] and map[next_x, next_y] == map[x, y]:
			region[(x, y)][(dx, dy)] = 0

			if (next_x, next_y) not in region:
				get_region(next_x, next_y, region)

	return region

while len(plants) > 0:
	x, y = plants.pop()
	regions.append(get_region(x, y))

total = sum([len(region) * sum([sum(plant.values()) for plant in region.values()]) for region in regions])

with open('2024/12/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

normals = {(0, 1): (1, 0), (1, 0): (0, 1), (0, -1): (1, 0), (-1, 0): (0, 1)}
region_sides = []

for region in regions:
	for (x, y), plant in region.items():
		for direction, side in plant.items():
			if side == 1 and region.get((x + normals[direction][0], y + normals[direction][1]), {}).get(direction, 0) != 0:
				plant[direction] = -1

total = sum([len(region) * sum([sum([max(direction, 0) for direction in plant.values()]) for plant in region.values()]) for region in regions])

with open('2024/12/output_2.txt', 'w') as f:
	f.write(str(total))

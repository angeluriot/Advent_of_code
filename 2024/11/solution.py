with open('2024/11/input.txt', 'r') as f:
	data = f.read()

# Part 1

stones = [int(stone) for stone in data.split(' ')]

for i in range(25):
	temp = []

	for stone in stones:
		if stone == 0:
			temp.append(1)
		elif len(str(stone)) % 2 == 0:
			temp.append(int(str(stone)[:len(str(stone)) // 2]))
			temp.append(int(str(stone)[len(str(stone)) // 2:]))
		else:
			temp.append(stone * 2024)

	stones = temp

total = len(stones)

with open('2024/11/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

stones_dict = {int(stone): 1 for stone in data.split(' ')}

for i in range(75):
	temp = {}

	if stones_dict.get(0, 0) > 0:
		temp[1] = stones_dict[0]
		stones_dict.pop(0)

	for stone_i, nb in stones_dict.items():
		size = len(str(stone_i))

		if size % 2 == 0:
			left = int(str(stone_i)[:size // 2])
			right = int(str(stone_i)[size // 2:])
			temp[left] = temp.get(left, 0) + nb
			temp[right] = temp.get(right, 0) + nb
		else:
			temp[stone_i * 2024] = temp.get(stone_i * 2024, 0) + nb

	stones_dict = temp

total = sum(stones_dict.values())

with open('2024/11/output_2.txt', 'w') as f:
	f.write(str(total))

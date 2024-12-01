with open('2024/01/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

left_list = []
right_list = []

for line in data:
	left, right = line.split('   ')
	left_list.append(int(left))
	right_list.append(int(right))

left_list.sort()
right_list.sort()
distance = 0

for i in range(len(left_list)):
	distance += abs(left_list[i] - right_list[i])

with open('2024/01/output_1.txt', 'w') as f:
	f.write(str(distance))

# Part 2

similarity = 0

for l in left_list:
	similarity += l * len([r for r in right_list if l == r])

with open('2024/01/output_2.txt', 'w') as f:
	f.write(str(similarity))

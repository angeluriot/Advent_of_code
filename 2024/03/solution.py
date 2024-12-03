import re

with open('2024/03/input.txt', 'r') as f:
	data = f.read()

# Part 1

muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
total = sum([eval(mul[3:].replace(',', '*')) for mul in muls])

with open('2024/03/output_1.txt', 'w') as f:
	f.write(str(total))

# Part 2

do_parts = ''

for i, part in enumerate(data.split("don't()")):
	if i == 0:
		do_parts += part
	elif 'do()' in part:
		do_parts += ''.join(part.split('do()')[1:])

muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', do_parts)
total = sum([eval(mul[3:].replace(',', '*')) for mul in muls])

with open('2024/03/output_2.txt', 'w') as f:
	f.write(str(total))

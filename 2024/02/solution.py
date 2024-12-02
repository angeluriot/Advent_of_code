with open('2024/02/input.txt', 'r') as f:
	data = f.read().splitlines()

# Part 1

reports = [[int(level) for level in report.split(' ')] for report in data]
nb_safe = 0

for report in reports:
	diffs = [report[i] - report[i + 1] for i in range(len(report) - 1)]

	if all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs):
		nb_safe += 1

with open('2024/02/output_1.txt', 'w') as f:
	f.write(str(nb_safe))

# Part 2

nb_safe = 0

for report in reports:
	for i in range(len(report)):
		truncated = report[:i] + report[i + 1:]
		diffs = [truncated[i] - truncated[i + 1] for i in range(len(truncated) - 1)]

		if all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs):
			nb_safe += 1
			break

with open('2024/02/output_2.txt', 'w') as f:
	f.write(str(nb_safe))

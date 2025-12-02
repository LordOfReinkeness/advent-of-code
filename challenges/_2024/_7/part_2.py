from alive_progress import alive_bar

from challenges._2024._7.input_parse import parse_input

def get_correct_sum(current_sum, target, remaining, operations_string):
	if current_sum > target:
		return False, ''

	if len(remaining) == 0:
		if current_sum == target:
			return True, operations_string
		else:
			return False, ''

	options, solutions, next_i = [], [], remaining.pop(0)

	opt, sol = get_correct_sum(current_sum + next_i, target, remaining.copy(), operations_string + ' + ' + str(next_i))
	options.append(opt)
	solutions.append(sol)

	opt, sol = get_correct_sum(current_sum * next_i, target, remaining.copy(), operations_string + ' * ' + str(next_i))
	options.append(opt)
	solutions.append(sol)

	opt, sol = get_correct_sum(int(str(current_sum) + str(next_i)), target, remaining.copy(), operations_string + ' || ' + str(next_i))
	options.append(opt)
	solutions.append(sol)

	for i in range(3):
		if options[i]:
			return True, solutions[i]

	return False, ''

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 7 part 1 goes here

	out = 0
	for line in data:
		start = line[1].pop(0)
		opt, sol = get_correct_sum(start, line[0], line[1], str(start))
		if opt:
			out += line[0]
			print('{}: {}'.format(line[0], sol))

	return out

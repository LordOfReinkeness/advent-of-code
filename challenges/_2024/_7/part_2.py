from alive_progress import alive_bar

from challenges._2024._7.input_parse import parse_input

def get_solutions_strings(array):
	if len(array) > 1:
		out = []
		subarray = get_solutions_strings(array[1:])
		for line in subarray:
			out.append('{} + {}'.format(str(array[0]), line ))
			out.append('{} * {}'.format(str(array[0]), line ))
			out.append('{} || {}'.format(str(array[0]), line ))

		return out
	else:
		return [str(array[0])]


def eval_string(line: str, target):
	line = line.split(' ')

	if int(line[0]) > target:
		return target + 1

	if len(line) == 1:
		return str(int(line[0]))

	if line[1] == '+':
		n = ' '.join([str(int(line[0]) + int(line[2]))] + line[3:])
		return eval_string(n ,target)
	elif line[1] == '*':
		n = ' '.join([str(int(line[0]) * int(line[2]))] + line[3:])
		return eval_string(n ,target)
	elif line[1] == '||':
		i = eval_string(' '.join(line[2:]), target)
		return int('{}{}'.format(str(line[0]), str(i)))

def main(data):
	data = parse_input(data)
	valid_sols = [156, 190, 192, 292, 3267, 7290]
	# Your challenges for AOC 2024 day 7 part 1 goes here

	out = 0
	i = 0
	for line in data:
		i += 1
		print('Done {}/{}'.format(i, len(data)))

		solution_strings = get_solutions_strings(line[1])

		for option in solution_strings:
			eval_int = eval_string(option, line[0])
			if int(line[0]) == int(eval_int):
				out += line[0]
				break

	return out

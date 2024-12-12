from challenges._2024._7.input_parse import parse_input

def get_correct_sum(data, summe, pos, target):
	if summe > target:
		return 0

	if pos == len(data):
		if summe == target:
			return 1
		else:
			return 0

	return get_correct_sum(data, summe + data[pos], pos + 1, target) + get_correct_sum(data, summe * data[pos], pos + 1, target)

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 7 part 1 goes here

	out = 0
	for line in data:
		# print('{} has {} solutions'.format(str(line), get_correct_sum(line[1], line[1][0], 1, line[0])))
		if get_correct_sum(line[1], line[1][0], 1, line[0]) > 0:
			out += line[0]

	return out

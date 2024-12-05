from challenges._2024._5.input_parse import parse_input

def get_middle_member(sequence):
	if len(sequence) % 2 != 0:
		return sequence[int((len(sequence)-1)/2)]

	print('Sequence is not even')
	return 0

def main(data):
	rules_graph, sequences = parse_input(data)
	# Your challenges for AOC 2024 day 5 part 1 goes here
	out = 0

	for sequence in sequences:
		prev = sequence[0]
		in_order = True
		for step in sequence[1:]:
			if not rules_graph[prev].has_next(step):
				# print('{} is not directly after {}'.format(step, prev))
				in_order = False
				# print('Sequence not in order: {}'.format(sequence))
				break

			prev = step

		if in_order:
			# print('Sequence in order: {}'.format(sequence))
			out += get_middle_member(sequence)


	return out

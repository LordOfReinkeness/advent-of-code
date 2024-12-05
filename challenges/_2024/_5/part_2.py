from challenges._2024._5.input_parse import parse_input

def get_middle_member(sequence):
	if len(sequence) % 2 != 0:
		return sequence[int((len(sequence)-1)/2)]

	print('Sequence is not even')
	return 0

def sort_list(rules_graph, sequence):
	i = 0
	while i < len(sequence) - 1:
		if rules_graph[sequence[i]].has_next(sequence[i + 1]):
			i += 1
		else:
			elem = sequence.pop(i)
			for j in range(i, len(sequence)):
				if rules_graph[sequence[j]].has_next(elem):
					sequence.insert(j+1, elem)
					i = 0
					break

	return sequence

def is_sorted(rules_graph, sequence):
	prev = sequence[0]
	for step in sequence[1:]:
		if not rules_graph[prev].has_next(step):
			return False

		prev = step

	return True


def main(data):
	rules_graph, sequences = parse_input(data)
	# Your challenges for AOC 2024 day 5 part 1 goes here
	out = 0

	for sequence in sequences:
		if not is_sorted(rules_graph, sequence):
			sorted_list = sort_list(rules_graph, sequence)
			out += get_middle_member(sorted_list)

	return out

from itertools import permutations

from challenges._2024._2.input_parse import parse_input

def is_save(arr):
	prev = arr[0]
	asc = True
	dec = True
	for i in arr[1:]:
		if i <= prev:
			asc = False
		if i >= prev:
			dec = False

		if not (0 < abs(prev - i) < 4):
			return False
		prev = i

	return (asc and not dec) or (dec and not asc)

def permutation_save(arr):
	if is_save(arr):
		return True
	else:
		permutations = []
		for i in range(len(arr)):
			tmp = arr.copy()
			tmp.pop(i)
			permutations.append(tmp)

		for p in permutations:
			if is_save(p):
				return True

		return False



def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 2 part 2 goes here
	out = 0

	for line in data:
		if permutation_save(line):
			out += 1

	return out

import numpy as np

from challenges._2024._8.input_parse import parse_input

def main(data):
	data, interference_field = parse_input(data)
	# Your challenges for AOC 2024 day 8 part 1 goes here
	frequencies = {}
	for y in range(len(data)):
		for x in range(len(data[y])):

			if data[y][x] != '.':
				if data[y][x] not in frequencies:
					frequencies[data[y][x]] = []

				frequencies[data[y][x]].append([x, y])

	for frequency in frequencies:
		for freq1 in frequencies[frequency]:
			for freq2 in frequencies[frequency]:
				if freq1 != freq2:
					interference = [freq2[0] - freq1[0] + freq2[0], freq2[1] - freq1[1] + freq2[1]]
					if interference[0] > -1 and interference[1] > -1:
						try:
							interference_field[interference[1]][interference[0]] = '#'
						except IndexError:
							pass

	out = 0
	for line in interference_field:
		for c in line:
			if c == '#':
				out += 1

	return out

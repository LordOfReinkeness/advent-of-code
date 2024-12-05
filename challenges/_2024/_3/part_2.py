import functools
import operator
import re

from challenges._2024._3.input_parse import parse_input

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 3 part 2 goes here
	regex = "mul\((\d*,\d*)\)|(do\(\))|(don't\(\))"
	matches = re.findall(regex, data)

	do = True
	out = 0

	for match in matches:
		if match[1] != '':
			do = True
			continue
		elif match[2] !='':
			do = False
			continue

		if do:
			out += functools.reduce(operator.mul, [int(numeric_string) for numeric_string in match[0].split(',')], 1)

	return out

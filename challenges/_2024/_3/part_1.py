import functools
import operator
import re

from challenges._2024._3.input_parse import parse_input

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 3 part 1 goes here
	regex_pattern = 'mul\((\d*,\d*)\)'

	matches = re.findall(pattern=regex_pattern, string=data)
	out = 0
	for match in matches:
		out += functools.reduce(operator.mul, [int(numeric_string) for numeric_string in match.split(',')], 1)

	return out

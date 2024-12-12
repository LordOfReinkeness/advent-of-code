def parse_input(data):
	return [list(line) for line in data.strip().split('\n')], [['.' for l in list(line)] for line in data.strip().split('\n')]

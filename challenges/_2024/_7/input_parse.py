def parse_input(data):
	return [[int(line.split(': ')[0]), [int(c) for c in line.split(': ')[1].split(' ')]] for line in data.strip().split('\n')]

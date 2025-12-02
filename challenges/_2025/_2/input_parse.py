def parse_input(data: str):
	return [[int(x) for x in line.split('-')] for line in data.strip().split(',')]

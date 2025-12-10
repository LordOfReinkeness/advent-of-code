def parse_input(data: str):
	return [[int(elem) for elem in line] for line in data.strip().split('\n')]

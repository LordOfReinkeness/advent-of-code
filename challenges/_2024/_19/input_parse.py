def parse_input(data: str):
	return data.strip().split('\n\n')[0].split(', '), [line for line in data.strip().split('\n\n')[1].split('\n')]

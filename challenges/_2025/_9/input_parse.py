import numpy as np

def parse_input(data: str):
	return [np.array(([int(elem) for elem in line.split(',')])) for line in data.strip().split('\n')]

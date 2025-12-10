import numpy as np

def parse_input(data: str):
	return np.array([list(line) for line in data.strip().split('\n')])

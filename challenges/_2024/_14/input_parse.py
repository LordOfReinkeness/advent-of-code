import numpy as np


def parse_input(data: str):
	return [
		[
			np.array([int(c) for c in line.split(' ')[0].split('=')[1].split(',')]),
			np.array([int(c) for c in line.split(' ')[1].split('=')[1].split(',')])
		] for line in data.strip().split('\n')
	]
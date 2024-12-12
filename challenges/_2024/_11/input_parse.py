from functools import cache

def parse_input(data: str):
	return [int(elem) for elem in data.strip().split('\n')[0].split(' ')]

@cache
def expand(elem, times):
	if times == 0: return 1
	if elem == 0:return expand(1, times - 1)
	elif len(str(elem)) % 2 == 0:
		return (expand(int(str(elem)[:int(len(str(elem)) / 2)]), times - 1)
				+ expand(int(str(elem)[int(len(str(elem)) / 2):]), times - 1))
	return expand(elem * 2024, times - 1)
import copy, os, time
from alive_progress import  alive_bar
from challenges._2024._6.input_parse import parse_input


def print_matrix(matrix):
	# Move the cursor to the top-left corner
	os.system('cls' if os.name == 'nt' else 'clear')
	for row in matrix:
		print(" ".join(f"{val:0}" for val in row))
	time.sleep(0.075)


def has_loop(data, output=False):
	# Your challenges for AOC 2024 day 6 part 1 goes here

	data = copy.deepcopy(data)
	guard_chars = ['^', '>', 'v', '<']
	guard_moves = {
		'^': [0, -1],
		'>': [1, 0],
		'v': [0, 1],
		'<': [-1, 0]
	}
	guard_trail = {
		'^': '|',
		'>': '-',
		'v': '|',
		'<': '-'
	}
	guard = []

	## get guard
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] not in ['.', '#', 'O']:
				guard = [data[y][x], [x, y]]
				break
		else:
			continue

		break

	turning_points = []
	has_turned = False
	guard_prev = guard[1]

	# move guard
	while True:
		# draw guard
		data[guard[1][1]][guard[1][0]] = guard[0]

		# draw guard path
		if not has_turned:
			data[guard_prev[1]][guard_prev[0]] = guard_trail[guard[0]]

		# draw turning points
		for turning_point in turning_points:
			turning_point = [int(point) for point in turning_point.split(':')]
			if data[turning_point[1]][turning_point[0]] not in guard_chars:
				data[turning_point[1]][turning_point[0]] = '+'

		if output:
			print_matrix(data)

		guard_direction = guard_moves[guard[0]]
		guard_next = [guard[1][0] + guard_direction[0], guard[1][1] + guard_direction[1]]
		guard_prev = guard[1]

		# check if guard walks out
		if -1 < guard_next[1] < len(data) and -1 < guard_next[0] < len(data[0]):

			# guard hits obstacle
			if data[guard_next[1]][guard_next[0]] == '#' or data[guard_next[1]][guard_next[0]] == 'O':
				guard[0] = guard_chars[(guard_chars.index(guard[0]) + 1) % len(guard_chars)]

				if data [guard[1][1] + guard_moves[guard[0]][1]] [guard[1][0] + guard_moves[guard[0]][0]] in ['O', '#']:
					guard[0] = guard_chars[(guard_chars.index(guard[0]) + 1) % len(guard_chars)]

				has_turned = True
				turning_point_id = '{}:{}'.format(guard[1][0],guard[1][1])

				if turning_point_id in turning_points:
					if output:
						time.sleep(2)
					return True
				else:
					turning_points.append(turning_point_id)

			# guard can walk
			else:
				guard[1] = guard_next
				has_turned = False

		else:
			if output:
				time.sleep(2)
			return False


def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 6 part 2 goes here
	out = 0

	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x] not in ['^', '#']:
				new_obstacle_map = copy.deepcopy(data)
				new_obstacle_map[y][x] = 'O'

				if has_loop(new_obstacle_map, True):
					out += 1

	return out

from copy import deepcopy
from challenges._2024._21.input_parse import parse_input

keypads =[
	[['7', '8', '9'],['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']],
	[[None, '^', 'A'], ['<', 'v', '>']]
]

keypad_lookup_tables = [
	{'7': [0, 0], '8': [1, 0], '9': [2, 0], '4': [0, 1], '5': [1, 1], '6': [2, 1], '1': [0, 2], '2': [1, 2], '3': [2, 2], '0': [1, 3], 'A': [2, 3]},
	{'^': [1, 0], 'A': [2, 0], '<': [0, 1], 'v': [1, 1], '>': [2, 1]}
]

test_solutions = {
	'029A': '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A',
	'980A': '<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A',
	'179A': '<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A',
	'456A': '<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A',
	'379A': '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'
}


def get_moves_to_key(start_key: str, end_key: str, keypad_id):

	if start_key == end_key:
		return 'A'

	start_coordinates = keypad_lookup_tables[keypad_id][start_key]
	end_coordinates = keypad_lookup_tables[keypad_id][end_key]

	out = ''

	# chek if z mmovements hits None
	hit_none = False

	if start_coordinates[0] != end_coordinates[0]:
		x_tmp = start_coordinates[0]
		x_move = int((end_coordinates[0] - start_coordinates[0]) / abs(end_coordinates[0] - start_coordinates[0]))
		while x_tmp != end_coordinates[0]:
			x_tmp += x_move

			if keypads[keypad_id][start_coordinates[1]][x_tmp] is None:
				hit_none = True
				break
	# X-Achsis moves if not hotting None
	if not hit_none:
		x_move = int(end_coordinates[0] - start_coordinates[0])
		if x_move > 0:
			out += '>' * abs(x_move)
		elif x_move < 0:
			out += '<' * abs(x_move)

	# Y-Axis moves can be done in one step
	y_move = int(end_coordinates[1] - start_coordinates[1])
	if y_move > 0:
		out += 'v' * abs(y_move)
	elif y_move < 0:
		out += '^' * abs(y_move)

	# if None was hit, move X-Axchsis now
	if hit_none:
		x_move = int(end_coordinates[0] - start_coordinates[0])
		if x_move > 0:
			out += '>' * abs(x_move)
		elif x_move < 0:
			out += '<' * abs(x_move)


	return out + 'A'

def display_moves(moves):

	# print('Proposed Solution:\t{}'.format(test_solutions[moves[0]]))

	for index in range(len(moves[3])):

		if moves[3][index] != 'A':
			moves[2] = moves[2][:index] + ' ' + moves[2][index:]

		if moves[2][index] != 'A':
			moves[1] = moves[1][:index] + ' ' + moves[1][index:]

		if moves[1][index] != 'A':
			moves[0] = moves[0][:index] + ' ' + moves[0][index:]

	for i in reversed(moves):
		print('\t\t\t\t\t{}'.format(i))

	print('Length of solution: {}\n'.format(len(moves[-1])))


def main(data):
	data = parse_input(data)
	out = 0
	# Your challenges for AOC 2024 day 21 part 1 goes here

	for line in data:
		keypress_history = [line]
		keys_to_press = line
		for keypad_id in [0, 1, 1]:

			resulting_robot_movements = ''
			position_on_keypad = 'A'

			for nexy_key in keys_to_press:
				resulting_robot_movements += get_moves_to_key(position_on_keypad, nexy_key, keypad_id)
				position_on_keypad = nexy_key

			keys_to_press = resulting_robot_movements
			keypress_history.append(resulting_robot_movements)

		display_moves(deepcopy(keypress_history))

		out += len(keys_to_press) * int(''.join(line)[:-1])

	return out

from challenges._2024._9.input_parse import parse_input

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 9 part 1 goes here

	## make disk image
	disk_image = []
	for i in range(int((len(data)+1)/2)):
		disk_image += [str(i)] * data[i*2]
		try:
			disk_image += ['.'] * data[(i*2)+1]
		except IndexError:
			pass

	## compact
	first_block_id = 0
	last_block_id = len(disk_image) - 1
	while True:
		# find first unset block
		while disk_image[first_block_id] != '.':
			first_block_id += 1

		# find last set block
		while disk_image[last_block_id] == '.':
			last_block_id -= 1

		if first_block_id >= last_block_id:
			break

		disk_image[first_block_id] = disk_image[last_block_id]
		disk_image[last_block_id] = '.'

	# calculate hash
	disk_image = [int(j) for j in [i for i in disk_image if i != '.']]
	out = 0
	for i in range(len(disk_image)):
		new = i * disk_image[i]
		out += new

	return out

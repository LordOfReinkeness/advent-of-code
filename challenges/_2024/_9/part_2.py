from challenges._2024._9.input_parse import parse_input

def main(data):
	data = parse_input(data)
	# Your challenges for AOC 2024 day 9 part 2 goes here

	## make disk image
	disk_image = []
	last_index = 0
	for ind in range(int((len(data)+1)/2)):
		disk_image.append([ind, data[ind * 2]])
		last_index = ind
		try:
			if data[(ind*2)+1] > 0:
				disk_image.append([-1, data[(ind*2)+1]])
		except IndexError:
			pass

	## compress
	try:

		i = len(disk_image) - 1
		while i > -1:
			i = len(disk_image) - 1

			while disk_image[i][0] != last_index:
				i -= 1

			last_index -= 1

			# find first fitting space
			for j in range(i):
				if disk_image[j][0] == -1 and disk_image[j][1] >= disk_image[i][1]:
					obj = disk_image.pop(i)
					disk_image.insert(i,[-1, obj[1]])
					free_space = disk_image.pop(j)
					disk_image.insert(j, obj)

					if free_space[1] > obj[1]:
						disk_image.insert(j+1, [-1, free_space[1] - obj[1]])

					break

	except IndexError:
		pass

	expanded_disk_image = []
	for line in disk_image:
		c = '.' if line[0] == -1 else str(line[0])
		expanded_disk_image += [c] * line[1]

	out = 0
	for i in range(len(expanded_disk_image)):
		if expanded_disk_image[i] != '.':
			out += i * int(expanded_disk_image[i])

	return out

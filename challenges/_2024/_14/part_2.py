import os
import time
import numpy as np
import matplotlib.pyplot as plt
from challenges._2024._14.input_parse import parse_input

room_size = np.array([101, 103])
max_iter = 20000

class Robot:

	def __init__(self, position: np.array, velocity: np.array):
		self.position = position
		self.velocity = velocity

	def move(self):
		self.position = (self.position + self.velocity) % room_size

def main(data):

	data = parse_input(data)
	# Your challenges for AOC 2024 day 14 part 1 goes here
	robots = []
	for row in data:
		robots.append(Robot(row[0], row[1]))

	for i in range(7570, 7581):

		for robot in robots:
			robot.move()

		room = [[0 for p in range(room_size[0])] for line in range(room_size[1])]

		for robot in robots:
			room[robot.position[1]][robot.position[0]] += 1

		variances = []
		for row in room:
			variances.append(np.array(row).var())
		print('{}:{}'.format(i, np.array(variances).mean()))

	return 0
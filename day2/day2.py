""" Day 2."""
from pathlib import Path

# Load inputs
position = [0, 0]
inputs = []
for line in Path('input.txt').read_text().split('\n'):
    inputs.append(tuple(line.split(' ')))

# Part one
for direction in inputs:
    if direction[0] == 'forward':
        position[0] += int(direction[1])
    if direction[0] == 'up':
        position[1] -= int(direction[1])
    if direction[0] == 'down':
        position[1] += int(direction[1])
    # print (str(direction) + ' ' + str(position))

result = position[0] * position[1]
print(f"Day 2 part 1: {result}")

# Part two
aim = 0
for i in inputs:
    direction = i[0]
    value = int(i[1])
    if direction == 'forward':
        position[0] += value
        position[1] = position[1] + aim * value
    if direction == 'down':
        aim += value
    if direction == 'up':
        aim -= value
    # print(str(direction) + ' ' + str(position))

result = position[0] * position[1]
print(f"Day 2 part 2: {result}")

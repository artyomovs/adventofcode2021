""" Day 2."""
from pathlib import Path

# Load inputs
position = [0, 0]
inputs = []
for line in Path('input.txt').read_text().split('\n'):
    inputs.append(tuple(line.split(' ')))

for direction in inputs:
    if direction[0] == 'forward':
        position[0] += int(direction[1])
    if direction[0] == 'up':
        position[1] -= int(direction[1])
    if direction[0] == 'down':
        position[1] += int(direction[1])
    print (str(direction) + ' ' + str(position))

multiply = position[0] * position[1]
print(multiply)
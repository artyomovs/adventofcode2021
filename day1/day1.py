""" Day1. """
from pathlib import Path

# Load inputs
inputs = []
for i in Path('input.txt').read_text().split():
    inputs.append(int(i))

# Part one
increased = 0
for i in range(1, len(inputs)):
    if int(inputs[i]) >= int(inputs[i-1]):
        increased += 1

print(increased)

# Part two
increased = 0
for i in range(0, len(inputs) - 3):
    if sum(inputs[i:i+3]) < sum(inputs[i+1:i+4]):
        increased += 1

print(increased)

"Advent of code 2021, day 3."
from pathlib import Path

inputs = []
for line in Path("input.txt").read_text().splitlines():
    inputs.append(line)

print("Part One")
symbols = {}
for line in inputs:
    for i in range(0, len(line)):
        if line[i] == '0':
            delta = -1
        else:
            delta = 1
        symbols.update({f'{i}': symbols.get(f'{i}', 0) + delta})
    # print(line)
    # print(symbols)

gamma_rate_binary = ''.join(map(str, [0 if s < 0 else 1 for s in symbols.values()]))
epsilon_rate_binary = gamma_rate_binary.replace('0', '2').replace('1', '0').replace('2', '1')
print(f"gamma rate binary: {gamma_rate_binary}")
print(f"epsilon rate binary {epsilon_rate_binary}")
gamma_rate = int(gamma_rate_binary.encode(), 2)
epsilon_rate = int(epsilon_rate_binary.encode(), 2)
print(f"result: {gamma_rate * epsilon_rate}")


def get_most_common(list_numbers, position):
    delta = 0
    for line in list_numbers:
        increment = 1 if int(line[position]) == 1 else -1
        delta += increment
    #print(f"delta: {delta}")
    return 1 if delta >= 0 else 0


print("Part two")
position = 0
# print("Oxygen")
# print(inputs)
inputs_source = list(inputs)
#Calculate oxygen
while True:
    if position > len(inputs[0]):
        position = 0
    most_common = get_most_common(inputs, position)
    inputs_new = []

    for line in inputs:
        if line[position] == str(most_common):
            inputs_new.append(line)
    inputs = inputs_new
    position += 1
    # print(f"pos={position} most_common={most_common} new inputs={str(inputs)}")
    if len(inputs) == 1:
        break
oxygen_generator = int(inputs[0].encode(), 2)

#Calculate CO2
inputs = list(inputs_source)
position = 0
# print("CO2")
# print(inputs)
while True:
    if position > len(inputs[0]):
        position = 0
    less_common = get_most_common(inputs, position) ^ 1
    inputs_new = []

    for line in inputs:
        if line[position] == str(less_common):
            inputs_new.append(line)
    inputs = inputs_new
    position += 1
    # print(f"pos={position} less_common={less_common} new inputs={str(inputs)}")
    if len(inputs) == 1:
        break

co2_scrubber_rating = int(inputs[0].encode(), 2)

print(f"oxygen generator rating: {oxygen_generator}")
print(f"CO2 scrubber rating: {co2_scrubber_rating}")
print(f"life support rating = {oxygen_generator * co2_scrubber_rating}")
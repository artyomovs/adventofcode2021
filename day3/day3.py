"Advent of code 2021, day 3."
from pathlib import Path

inputs = []
for line in Path("input.txt").read_text().splitlines():
    inputs.append(line)


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

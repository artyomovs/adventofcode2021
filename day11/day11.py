from pathlib import Path
from sys import argv

STEP_FLASHES = []
COUNT_FLASHES = 0
ALL_FLASHES_STEP = 0

def read_input(filename="input.txt"):
    inputs = []
    file_inputs = Path(filename).read_text().splitlines()
    for line in file_inputs:
        row = []
        for elem in line:
            row.append(int(elem))
        inputs.append(row)
    return inputs

def get_filename(args):
    if "example" in args:
        return "input_example.txt"
    else:
        return "input.txt"



def nice_print_array(A, descripton="array:"):
    print(descripton)
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in A]))


def get_count_of_flashes(inputs):
    flashes_count = 0
    for line in inputs:
        for elem in line:
            if elem == 0:
                flashes_count += 1
    return flashes_count


def if_all_flashed(inputs):
    for line in inputs:
        for elem in line:
            if elem != 0:
                return False
    return True

def make_step_part_one(inputs, step_number=0):
    global STEP_FLASHES
    global COUNT_FLASHES
    global ALL_FLASHES_STEP
    flashed = []
    for i in range(0, len(inputs)):
        for j in range(0, len(inputs[i])):
            inputs[i][j] += 1
            if inputs[i][j] == 10:
                inputs[i][j] = 0
                flashed.append((i, j))
    if flashed:
        STEP_FLASHES = list(flashed)
        inputs = make_flashes(inputs, flashed)
    COUNT_FLASHES += get_count_of_flashes(inputs)

    if ALL_FLASHES_STEP == 0 and if_all_flashed(inputs):
        ALL_FLASHES_STEP = step_number


def if_out_of_border(elem, i, j):
    if elem[0] < 0 or elem[1] < 0 or elem[0] > len(inputs) - 1 or elem[1] > len(inputs[0]) - 1 or (elem[0] == i and elem[1] == j):
        return True
    else:
        return False

def get_adjacents(i, j):
    neighbors = []
    for i_diff in range(-1, 2):
        for j_diff in range(-1, 2):
            neighbors.append(((i + i_diff), (j + j_diff)))
    new_neighbors = [elem for elem in neighbors if not(if_out_of_border(elem, i, j))]
    return new_neighbors


def make_flashes(inputs, flashes):
    new_flashes = []
    for f in flashes:
        neighbors = get_adjacents(f[0], f[1])
        for n in neighbors:
            if n not in STEP_FLASHES:
                inputs[n[0]][n[1]] += 1
            if inputs[n[0]][n[1]] == 10:
                inputs[n[0]][n[1]] = 0
                new_flashes.append(n)
                STEP_FLASHES.append(n)
    if new_flashes:
        inputs = make_flashes(inputs, new_flashes)
    return inputs



def count_flashes_part_one(inputs, count_of_steps=100):
    for i in range (1, count_of_steps+1):
        make_step_part_one(inputs, i)
    print(f"{COUNT_FLASHES=}")


def find_first_all_flashes_step(inputs, count_of_steps=1000):
    global ALL_FLASHES_STEP
    ALL_FLASHES_STEP = 0
    for i in range (1, count_of_steps):
        make_step_part_one(inputs, i)
        if ALL_FLASHES_STEP != 0:
            return True
    return False

if __name__ == "__main__":
    filename = get_filename(argv)
    inputs = read_input(filename)

    #Part one
    nice_print_array(inputs, "before steps")
    count_flashes_part_one(inputs, 100)

    # Part two
    inputs = read_input(filename)
    if find_first_all_flashes_step(inputs, count_of_steps=1000):
        print(f"{ALL_FLASHES_STEP=}")
    else:
        print("Not flashed")

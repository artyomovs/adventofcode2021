from pathlib import Path
from sys import argv

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
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))


def make_step_part_one(inputs, step_number=0):
    flashed = []
    for i in range(0, len(inputs)):
        for j in range(0, len(inputs[i])):
            inputs[i][j] += 1
            if inputs[i][j] == 10:
                inputs[i][j] = 0
                flashed.append((i, j))
    # nice_print_array(inputs, f"")
    print(f"{step_number=} {flashed=}")
    initial_flashes = list(flashed)
    if flashed:
        inputs = make_flashes(inputs, flashed, initial_flashes)
    nice_print_array(inputs, f"{step_number = }")


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
    # print(neighbors)
    new_neighbors = [elem for elem in neighbors if not(if_out_of_border(elem, i, j))]
    return new_neighbors
    # print(new_neighbors)


def make_flashes(inputs, flashes, initial_flashes):
    new_flashes = []
    for f in flashes:
        neighbors = get_adjacents(f[0], f[1])
        for n in neighbors:
            # nice_print_array(inputs, f"{n=}")
            if n not in initial_flashes:
                inputs[n[0]][n[1]] += 1
            if inputs[n[0]][n[1]] == 10:
                inputs[n[0]][n[1]] = 0
                new_flashes.append(n)
    if new_flashes:
        print(f"{new_flashes=}")
        inputs = make_flashes(inputs, new_flashes, initial_flashes)
    return inputs



def count_flashes(inputs, count_of_steps=100):

    for i in range (1, count_of_steps+1):
        make_step_part_one(inputs, i)


if __name__ == "__main__":
    filename = get_filename(argv)
    inputs = read_input(filename)
    nice_print_array(inputs, "before steps")
    count_flashes(inputs, 2)

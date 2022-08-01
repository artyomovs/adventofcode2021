from pathlib import Path
from sys import argv

BASIN = []
LOW_POINTS = []

def read_input(filename="input.txt"):
    return Path(filename).read_text().splitlines()

def get_filename(args):
    if "example" in args:
        return "input_example.txt"
    else:
        return "input.txt"

# def get_low_points_of_line(line):
#     low_points = []
#     print(line)
#     for i in range(0, len(line)):
#         left = 1 if i == 0 else int(line[i-1])
#         right = 1 if i == len(line) - 1 else int(line[i + 1])
#         # print(f"left = {left} right = {right} i = {i}")
#         if int(line[i]) < left and int(line[i]) < right:
#             low_points.append(line[i])
#     print(low_points)

def calculate_low_points_part_one(inputs):
    global LOW_POINTS
    low_points = []
    for i in range (0, len(inputs)):
        line = inputs[i]
        for j in range (0, len(line)):
            elem = int(line[j])
            up = 9 if i == 0 else int(inputs[i-1][j])
            down = 9 if i == len(inputs) - 1 else int(inputs[i+1][j])
            left = 9 if j == 0 else int(line[j-1])
            right = 9 if j == len(line) - 1 else int(line[j + 1])
            if elem < up and elem < down and elem < right and elem < left:
                low_points.append(elem + 1)
                LOW_POINTS.append((i, j))
            # print(f"{i=} {j=} {elem=} {up=} {down=} {")
    print(sum(low_points))


def get_adjacent(inputs, i, j, direction):
    result = 9
    if direction == "left" and j > 0:
        return int(inputs[i][j-1]), i, j-1
    elif direction == "right" and j < len(inputs[i]) - 1:
        return int(inputs[i][j+1]), i, j + 1
    elif direction == "up" and i > 0:
        return int(inputs[i-1][j]), i-1, j
    elif direction == "down" and i < len(inputs) - 1:
        return int(inputs[i+1][j]), i+1, j

    return result, -1, -1


def get_point_basin(inputs, i, j):
    global BASIN
    elem = int(inputs[i][j])
    for direction in ["left", "up", "right", "down"]:
        adjacent, new_i, new_j = get_adjacent(inputs, i, j, direction)
        if adjacent > elem and adjacent != 9:
            print(f"{elem=} {direction=} {adjacent=}")
            BASIN.append((new_i, new_j))
            get_point_basin(inputs, new_i, new_j)
            # return 1
    # return basin_list


def get_basins_count(inputs):
    global LOW_POINTS
    global BASIN
    basins_sizes = []
    print(LOW_POINTS)

    for point in LOW_POINTS:
        BASIN = []
        get_point_basin(inputs, point[0], point[1])
        count = len(set(BASIN))
        basins_sizes.append(count + 1)
    
    basins_sizes.sort()
    max_3 = basins_sizes[len(basins_sizes) - 3:]
    result = max_3[0] * max_3[1] * max_3[2]


    print(basins_sizes)
    print(result)

if __name__ == "__main__":
    filename = get_filename(argv)
    inputs = read_input(filename)
    calculate_low_points_part_one(inputs)

    get_basins_count(inputs)
    # print(inputs)
    # basin = []





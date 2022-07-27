from pathlib import Path
from pprint import pprint

def read_input(filename="input.txt"):
    return list(map(int, Path(filename).read_text().split(",")))


def allign_by_position(coordinates, position, part=1):
    cost = 0
    for c in coordinates:
        if part == 1:
            cost = cost + abs(c - position)
        if part == 2:
            cost = cost + calculate_fuel_consumption_part_two(c, position)
    return cost

def calculate_fuel_consumption_part_two(c1, c2):
    sum = 0
    for i in range(1, abs(c2 - c1) + 1):
        sum = sum + i
    return sum

if __name__== "__main__":
    coordinates = read_input()
    costs = []
    ## Part one
    for position in range(min(coordinates), max(coordinates) + 1):
        if position in coordinates:
            cost = allign_by_position(coordinates, position)
            costs.append(cost)
            # pprint(f"Position {position}, cost {cost}")
    print(f"Part one. Minimal cost: {min(costs)}")


    ## Part two
    costs = []
    for position in range(min(coordinates), max(coordinates) + 1):
        if position in coordinates:
            cost = allign_by_position(coordinates, position, 2)
            costs.append(cost)
            # pprint(f"Position {position}, cost {cost}")
    print(f"Part two. Minimal cost: {min(costs)}")

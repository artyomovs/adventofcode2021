from pprint import pprint
from pathlib import Path
import sys

INPUTS = Path('input.txt').read_text().splitlines()

def parse_line(line):
    """ Parse line into two coordinates """
    line_borders = {}
    points = line.replace(" -> ", "|").split("|")
    point1 = list(map(int, points[0].split(',')))
    point2 = list(map(int, points[1].split(',')))
    line_borders["x_min"] = int(point1[0]) if point1[0] < point2[0] else int(point2[0])
    line_borders["x_max"] = int(point1[0]) if point1[0] > point2[0] else int(point2[0])
    line_borders["y_min"] = int(point1[1]) if point1[1] < point2[1] else int(point2[1])
    line_borders["y_max"] = int(point1[1]) if point1[1] > point2[1] else int(point2[1])

    # print(f"{line}: {line_borders}")
    return point1, point2, line_borders

def if_straight_line(point1, point2):
    """Say yes if this line is vertical or horizontal"""

    result = False
    if point1[0] == point2[0] or point1[1] == point2[1]:
        result = True
    else:
        result = False
    return result

def set_up_new_borders(line_borders, global_borders):
    if line_borders["x_min"] < global_borders["x_min"]:
        global_borders["x_min"] = line_borders["x_min"]
    if line_borders["y_min"] < global_borders["y_min"]:
        global_borders["y_min"] = line_borders["y_min"]
    if line_borders["x_max"] > global_borders["x_max"]:
        global_borders["x_max"] = line_borders["x_max"]
    if line_borders["y_max"] > global_borders["y_max"]:
        global_borders["y_max"] = line_borders["y_max"]


def get_direction(point1, point2):
    """ Whethe the line is vertical(v) or horizontal(h). Also put in the sorted order. """

    direction = None
    new_point1 = []
    new_point2 = []
    if point1[0] == point2[0]:
        direction = "v"
        if point1[1] < point2[1]:
            new_point1 = point1
            new_point2 = point2
        else:
            new_point1 = point2
            new_point2 = point1
    if point1[1] == point2[1]:
        direction = "h"
        if point1[0] < point2[0]:
            new_point1 = point1
            new_point2 = point2
        else:
            new_point1 = point2
            new_point2 = point1
    return new_point1, new_point2, direction

def get_lines_overlaps(board):
    """ Get count of at least lwo lines overlaps. """
    overlaps = 0
    for line in board:
        for element in line:
            if isinstance(element, int):
                if element > 1:
                    overlaps += 1
    return overlaps

def is_diagonal(point1, point2):
    """ Determine if line at 45 degree between two points """
    if abs(point1[0] - point2[0]) == abs(point1[1] - point2[1]):
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    global_borders = parse_line(INPUTS[0])[2]
    # print(global_borders)
    straight_lines = []
    diagonal_lines = []
    board = []
    # Get only straight lines and edge coordinates
    for line in INPUTS:
        point1, point2, line_borders = parse_line(line)
        if if_straight_line(point1=point1, point2=point2):
            set_up_new_borders(line_borders, global_borders)
            point1, point2, direction = get_direction(point1, point2)
            straight_lines.append({"point1": point1, "point2": point2, "direction": direction})
        elif is_diagonal(point1, point2):
            diagonal_lines.append({"point1": point1, "point2": point2})


    # Fill board according to the edge coordinates
    for y in range(0, global_borders["y_max"]+2):
        line = []
        for x in range(0, global_borders["x_max"]+2):
            line.append(0)
        board.append(line)

    # Fill with . out of borders space (before x_min and y_min)
    if global_borders["y_min"] > 0:
        for y in range(0, global_borders["y_min"]):
            for x in range(0, global_borders["x_max"]):
                board[y][x] = "."

    if global_borders["x_min"] > 0:
        for y in range(0, global_borders["y_max"]):
            for x in range(0, global_borders["x_min"]):
                board[y][x] = "."

    # Fill board with coordinated from input
    # pprint(straight_lines)
    # print(global_borders)
    # print(len(board))

    for line in straight_lines:
        point1 = line.get("point1")
        point2 = line.get("point2")

        if line.get("direction") == "v":
            x = point1[0]
            for y in range(point1[1], point2[1]+1):
                board[y][x] = int(board[y][x]) + 1
        else:
            y = point1[1]
            for x in range(point1[0], point2[0]+1):
                board[y][x] = int(board[y][x]) + 1
        # pprint(board)

    # pprint(board)
    overlaps = get_lines_overlaps(board)
    print(f"Count of overlaps with vertical and horizontal: {overlaps}")

    # Part two - add diagonal lines
    for line in diagonal_lines:
        point1 = line.get("point1")
        point2 = line.get("point2")

        # print(line)
        for x in range(min(point1[0],point2[0]), max(point1[0],point2[0]) + 1):
            for y in range(min(point1[1],point2[1]), max(point1[1],point2[1]) + 1):
                if is_diagonal(point1=point1, point2=[x,y]):
                    # print(f"x={x}, y={y}")
                    board[y][x] = int(board[y][x]) + 1
    overlaps = get_lines_overlaps(board)
    print(f"Count of overlaps including diagonal: {overlaps}")
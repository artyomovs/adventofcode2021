from pathlib import Path
from pprint import pprint

BOARDS = []
LINES = Path('input.txt').read_text().splitlines()
NUMBERS = LINES.pop(0).split(',')
# pprint(lines)

board = []
for line in LINES:
    if not line:
        if len(board) > 0:
            BOARDS.append(board)
        board = []
    else:
        board.append([int(number) for number in line.split(' ') if number])

BOARDS.append(board)
BOARDS_2 = list(BOARDS)


# Part one
print("Part one")
def mark_appeared_numbers(_number):
    for i in range(0, len(BOARDS)):
        for j in range(0, len(BOARDS[i])):
            BOARDS[i][j] = list(map(lambda x: float(x) if x == _number else x, BOARDS[i][j]))


def get_win_board():
    for _board in BOARDS:
        for i in range(0, len(_board)):
            if all(isinstance(line[i], float) for line in _board):
                return _board
            if all(isinstance(_number, float) for _number in _board[i]):
                return _board
    return False

def remove_win_board():
    # remove_win_board if more than one
    for_delete = []
    if len(BOARDS) > 1:
        for j in range(0, len(BOARDS)):
            for i in range(0, len(BOARDS[j])):
                if all(isinstance(line[i], float) for line in BOARDS[j]):
                    for_delete.append(BOARDS[j])
                if all(isinstance(_number, float) for _number in BOARDS[j][i]):
                    for_delete.append(BOARDS[j])
        for del_elem in for_delete:
            if del_elem in BOARDS:
                BOARDS.remove(del_elem)
    return False

def get_sum_unmarked(board):
    sum_numbers = 0
    for line in board:
        for number in line:
            if isinstance(number, int):
                sum_numbers += number
    return sum_numbers

for number in NUMBERS:
    mark_appeared_numbers(int(number))
    win_board = get_win_board()
    if isinstance(win_board, list):
        print("WIN puzzle: ")
        pprint(win_board)
        sum_unmarked = get_sum_unmarked(win_board)
        print(f"Sum of unmarked numbers: {sum_unmarked}, current number: {number}")
        final_score = sum_unmarked * int(number)
        print(f"final score: {final_score}")
        break

print("Part two")
BOARDS = list(BOARDS_2)
for number in NUMBERS:
    mark_appeared_numbers(int(number))
    remove_win_board()
    if len(BOARDS) == 1:
        win_board = get_win_board()
        if isinstance(win_board, list):
            pprint("Last win puzzle: ")
            pprint(win_board)
            sum_unmarked = get_sum_unmarked(win_board)
            final_score = sum_unmarked * int(number)
            print(f"Sum of unmarked numbers: {sum_unmarked}, current number: {number}, final score: {final_score}")
            break


from pathlib import Path
from sys import argv

OPEN_BRACETS = ["[", "(", "<", "{"]
CLOSE_BRACETS = ["]", ")", ">", "}"]
SYMBOLS_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

SYMBOLS_SCORE_PART_TWO = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

BRACETS = {"[":"]", "(": ")", "<": ">", "{": "}"}


def read_input(filename="input.txt"):
    return Path(filename).read_text().splitlines()

def get_filename(args):
    if "example" in args:
        return "input_example.txt"
    else:
        return "input.txt"

def check_compiance_character(chunk, symbol):
    result = False
    if symbol in OPEN_BRACETS:
        chunk.append(symbol)
        result = True
    else:
        if BRACETS.get(chunk.pop()) == symbol:
            result = True
        else:
            result = False
    return result, chunk


def get_reverse_bracets_chunk(chunk):
    reversed_chunk = []
    for c in reversed(chunk):
        reversed_chunk.append(BRACETS.get(c))
    return reversed_chunk

def get_score_for_incomplete_chunk(chunk):
    reversed_chunk = get_reverse_bracets_chunk(chunk)
    score = 0
    for c in reversed_chunk:
        score = score * 5 + SYMBOLS_SCORE_PART_TWO.get(c)
    return score


def check_line_for_closed_bracets(line):
    chunk = []
    result = {
        "corrupted": False,
        "incomplete": False,
        "corrupted_symbol": ""
    }

    for i in line:
        compliant, chunk = check_compiance_character(chunk, i)
        if not compliant:
            result["corrupted_symbol"] = i
            result["corrupted"] = True
            break

    if compliant and len(chunk) > 0:
        result["incomplete"] = True
    result["chunk"] = chunk
    return result


def get_corrupted_score_part_one(inputs):
    score = 0
    scores_part_two = []
    for line in inputs:
        result = check_line_for_closed_bracets(line)
        if result["corrupted"]:
            score = score + SYMBOLS_SCORE.get(result["corrupted_symbol"])
        if result["incomplete"]:
            scores_part_two.append(get_score_for_incomplete_chunk(result["chunk"]))
    print(f"Part one {score=}")

    #Part two
    scores_part_two.sort()
    middle_score = scores_part_two[int((len(scores_part_two) - 1) / 2)]
    print(f"Part two {middle_score=}")

if __name__ == "__main__":
    filename = get_filename(argv)
    inputs = read_input(filename)
    # print(inputs)
    get_corrupted_score_part_one(inputs)
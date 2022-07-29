from pathlib import Path
from pprint import pprint

def is_subset(_set, _subset):
    result = False
    if set(_subset).issubset(set(_set)):
        result = True
    return result


def determine_digit(display, stage="first", samples = {}):
    digit = -1
    if stage == "first" or stage == "second":
        if len(display) == 2:
            digit = 1
        elif len(display) == 4:
            digit = 4
        elif len(display) == 3:
            digit = 7
        elif len(display) == 7:
            digit = 8
    if stage == "second":
        if len(display) == 6:
            if is_subset(display, samples.get(4)):
                digit = 9
            elif is_subset(display, samples.get(7)):
                digit = 0
            else:
                digit = 6
        if len(display) == 5:
            if is_subset(display, samples.get(7)):
                digit = 3
            elif is_subset(display + samples.get(4), samples.get(8)):
                digit = 2
            else:
                digit = 5

    return digit


def read_input(filename="input.txt", part="output"):
    lines = Path(filename).read_text().splitlines()

    result = []
    if part == "output":
        for line in lines:
            result.append(line.split("|")[1].split(" "))
    if part == "all":
        for line in lines:
            inputs = line.split("|")[0].strip().split(" ")
            outputs = line.split("|")[1].strip().split(" ")
            result.append(
                {"inputs": inputs, "outputs": outputs}
            )
    return result

def get_part_one_digits(inputs):
    digits = {}
    for line in inputs:
        for display in line:
            digit = determine_digit(display)
            digits.update({digit: digits.get(digit, 0) + 1})
    result = 0
    for i in [1, 4, 7, 8]:
        result = result + digits.get(i, 0)
    print(f"Part one result: {result}")

def get_part_two_digits(input_puzzle):
    sum = 0
    for line in input_puzzle:
        samples = {}
        number = ""
        for screen in line.get("inputs"):
            samples.update({determine_digit(screen): screen})

        outputs = line.get("outputs")
        for output in outputs:
            number = number + str(determine_digit(output, "second", samples))
        # print(f"{outputs}: {number}")
        sum = sum + int(number)
    print(f"Part two result: {sum}")


if __name__ == "__main__":
    # part one
    get_part_one_digits(read_input())

    #part two
    get_part_two_digits(read_input(filename="input.txt", part="all"))
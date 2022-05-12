from pathlib import Path
from pprint import pprint
import curses
from time import sleep

DAYS_TO_FINISH = 256

def read_input(filename="input.txt"):
    return Path(filename).read_text().split(",")

def fill_fishnet(fishes, fish_net):
    for fish in fishes:
        count = fish_net.get(fish, 0) + 1
        fish_net.update({fish: count})

def spawn_fishes(fish_net):
    new_fishes = fish_net.get("0", 0)
    for i in range(1, 9):
        fish_net.update({f"{i-1}": fish_net.get(f"{i}", 0)})
    fish_net.update({"8": new_fishes})
    fish_net.update({"6": fish_net.get("6", 0) + new_fishes})

def get_total_fishes(fish_net):
    total = 0
    for count in fish_net.values():
        total += count
    return total


def get_markers(count):
    result = ""
    if count > 255:
        result = "....256 more"
    else:
        result = "*" * count
    return result

def print_fishnet(iteration, fish_net, screen):
    screen.addstr(0, 0, f"Iteration: {iteration}")
    for i in range(0, 9):
        count = fish_net.get(f"{i}", 0)
        screen.addstr(i+1, 0, f"{i}:\t{get_markers(count)}")
    screen.refresh()



if __name__ == "__main__":
    screen = curses.initscr()
    fish_net = {}
    fishes_list = read_input("input.txt")
    fill_fishnet(fishes_list, fish_net)
    print(f"Initial state: {fishes_list}")
    sleep(3)
    for i in range(1, DAYS_TO_FINISH + 1):
        spawn_fishes(fish_net)
        total = get_total_fishes(fish_net)
        print_fishnet(i, fish_net, screen)
        sleep(0.2)
        screen.clear()
        print(f"After {i} day (total {total})")
        pprint(fish_net)
    screen.clear()
    curses.endwin()

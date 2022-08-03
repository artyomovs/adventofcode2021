from pathlib import Path
from sys import argv
import graphviz


def read_input(filename="input.txt"):
    return Path(filename).read_text().splitlines()

def get_filename(args):
    if "example" in args:
        return "input_example.txt"
    else:
        return "input.txt"


def vizualize(inputs):
    u = graphviz.Graph('unix', format="png", filename='caves_graph.gv', node_attr={'color': 'lightblue2', 'style': 'filled'})
    for line in inputs:
        a = line.split("-")[0]
        b = line.split("-")[1]
        u.edge(a, b)
    u.render()


if __name__ == "__main__":
    filename = get_filename(argv)
    inputs = read_input(filename)
    vizualize(inputs)


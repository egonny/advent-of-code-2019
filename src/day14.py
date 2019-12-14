import math

INPUT = "input/14.in"

def parse_element(output):
    split = output.split(" ")
    return (int(split[0]), split[1])

def parse_input(input):
    split = input.split(", ")
    return [parse_element(x) for x in split]

def read_input():
    result = {}
    with open(INPUT) as f:
        for line in f:
            [input, output] = line.rstrip().split(" => ")
            parsed_output = parse_element(output)
            parsed_input = parse_input(input)
            result[parsed_output[1]] = (parsed_output[0], parsed_input)

    return result

def find_cost(init_elem, init_amount, elem_map):
    state = {init_elem: init_amount}
    while [x for x in state.items() if x[0] != "ORE" and x[1] > 0]:
        (elem, amount) = next((x for x in state.items() if x[0] != "ORE" and x[1] > 0))
        (amount_per, requirements) = elem_map[elem]
        for (new_elem_amount, new_elem) in requirements:
            current_amount = state.get(new_elem, 0)
            new_amount = current_amount + math.ceil(amount / amount_per) * new_elem_amount
            state[new_elem] = new_amount
        state[elem] = amount - math.ceil(amount / amount_per) * amount_per

    return state["ORE"]

elem_map = read_input()
cost = find_cost("FUEL", 1, elem_map)
print(f"Part 1: {cost}")
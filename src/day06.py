from anytree import Node, RenderTree

INPUT = "input/06.in"

def read_input(input):
    with open(input) as f:
        return [x.rstrip().split(')') for x in f]

def construct_tree(orbits):
    com = Node("COM")
    planets = {"COM": com}
    for orbit in orbits:
        if not orbit[0] in planets:
            planets[orbit[0]] = Node(orbit[0])
        if not orbit[1] in planets:
            planets[orbit[1]] = Node(orbit[1])
        planets[orbit[1]].parent = planets[orbit[0]]

    return (com, planets)

def solve_1(planets, com):
    total_orbits = 0
    for planet in planets.values():
        node = planet
        while not node == com:
            node = node.parent
            total_orbits += 1
    
    return total_orbits


input = read_input(INPUT)
(com, planets) = construct_tree(input)

# PART 1
print(f"Part 1: {solve_1(planets, com)}")


# PART 2
def get_all_parents(node):
    result = []
    while node.parent:
        result.append(node.parent)
        node = node.parent

    return result

def get_closest_connecting_node(node1, node2):
    node1_parents = get_all_parents(node1)
    node2_parents = get_all_parents(node2)

    for elem1 in node1_parents:
        for elem2 in node2_parents:
            if elem1 == elem2:
                return elem1

def get_distance_between(parent_node, child_node):
    distance = 0
    node = child_node
    while not node == parent_node:
        node = node.parent
        distance += 1
    
    return distance

def solve_2(planets, com):
    you = planets["YOU"]
    santa = planets["SAN"]
    connection = get_closest_connecting_node(you, santa)

    return get_distance_between(connection, you) + get_distance_between(connection, santa) - 2


print(f"Part 2: {solve_2(planets, com)}")
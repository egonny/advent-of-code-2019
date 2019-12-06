INPUT = "input/03.in"

def read_input():
    with open(INPUT) as f:
        return [line.split(",") for line in f]

def directions_to_coords(line):
    points = set()
    distances = dict()
    current_pos = (0, 0)
    current_dist = 0
    for dir in line:
        orientation = dir[0]
        amount = int(dir[1:])
        
        if orientation == "U":
            for i in range(amount):
                coord = (current_pos[0], current_pos[1] - i - 1)
                if not coord in distances:
                    distances[coord] = current_dist + i + 1
                points.add(coord)
            current_pos = (current_pos[0], current_pos[1] - amount)
        elif orientation == "R":
            for i in range(amount):
                coord = (current_pos[0] + i + 1, current_pos[1])
                if not coord in distances:
                    distances[coord] = current_dist + i + 1
                points.add(coord)
            current_pos = (current_pos[0] + amount, current_pos[1])
        elif orientation == "D":
            for i in range(amount):
                coord = (current_pos[0], current_pos[1] + i + 1)
                if not coord in distances:
                    distances[coord] = current_dist + i + 1
                points.add(coord)
            current_pos = (current_pos[0], current_pos[1] + amount)
        elif orientation == "L":
            for i in range(amount):
                coord = (current_pos[0] - i - 1, current_pos[1])
                if not coord in distances:
                    distances[coord] = current_dist + i + 1
                points.add(coord)
            current_pos = (current_pos[0] - amount, current_pos[1])
        
        current_dist += amount
    return (points, distances)

lines = read_input()
(first_coords, first_distances) = directions_to_coords(lines[0])
(second_coords, second_distances) = directions_to_coords(lines[1])
intersect = first_coords.intersection(second_coords)

# PART 1
min_intersect = min(intersect, key = lambda coord: abs(coord[0]) + abs(coord[1]))
print(f"Manhattan distance of closest intersection: {abs(min_intersect[0]) + abs(min_intersect[1])}")

# PART 2
min_intersect = min(intersect, key = lambda coord: first_distances[coord] + second_distances[coord])
print(f"Fewest combined steps for an intersection: {first_distances[min_intersect] + second_distances[min_intersect]}")
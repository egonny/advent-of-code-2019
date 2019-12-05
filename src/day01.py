import math

INPUT = "input/01.in"

def read_input():
    with open(INPUT) as f:
        content = f.readlines()
        return list(map(lambda x: int(x), content))

def calc_fuel(mass):
    return math.floor(mass / 3) - 2

# PART 1
input = read_input()
total_fuel = sum(map(lambda x: calc_fuel(x), input))
print(f"Total fuel requirements: {total_fuel}")

# PART 2
def calc_fuel_repeated(mass):
    total = 0
    fuel = calc_fuel(mass)
    while fuel > 0:
        total += fuel
        fuel = calc_fuel(fuel)
    return total

total_fuel_repeated = sum(map(lambda x: calc_fuel_repeated(x), input))
print(f"Total fuel repeated requirements: {total_fuel_repeated}")
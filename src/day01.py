import math

INPUT = "input/01.in"

def read_input():
    with open(INPUT) as f:
        return [int(x) for x in f]

def calc_fuel(mass):
    return math.floor(mass / 3) - 2

# PART 1
input = read_input()
total_fuel = sum([calc_fuel(x) for x in input])
print(f"Total fuel requirements: {total_fuel}")

# PART 2
def calc_fuel_repeated(mass):
    total = 0
    fuel = calc_fuel(mass)
    while fuel > 0:
        total += fuel
        fuel = calc_fuel(fuel)
    return total

total_fuel_repeated = sum([calc_fuel_repeated(x) for x in input])
print(f"Total fuel repeated requirements: {total_fuel_repeated}")
from collections import Counter

INPUT = "307237-769058"

def create_range(input):
    split = input.split("-")

    return (int(split[0]), int(split[1]))

def meets_criteria(number):
    str_num = str(number)
    if not len(str_num) == 6:
        return False
    has_pair = False
    for i in range(0, 5):
        pair = str_num[i:i+2]
        if int(pair[0]) > int(pair[1]):
            return False
        if int(pair[0]) == int(pair[1]):
            has_pair = True
    return has_pair

input_range = create_range(INPUT)

# Part 1
answers = [x for x in range(input_range[0], input_range[1]) if meets_criteria(x)]
print(f"Part 1: there are {len(answers)} answers")

# Part 2
def meets_criteria_2(number):
    str_num = str(number)
    if not len(str_num) == 6:
        return False

    for i in range(0, 5):
        pair = str_num[i:i+2]
        if int(pair[0]) > int(pair[1]):
            return False
    
    return any([x for x in Counter(str_num).values() if x == 2])

answers = [x for x in range(input_range[0], input_range[1]) if meets_criteria_2(x)]
print(f"Part 2: there are {len(answers)} answers")
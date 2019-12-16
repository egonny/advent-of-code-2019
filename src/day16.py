INPUT = "input/16.in"


def read_input():
    with open(INPUT) as f:
        return [int(x) for x in f.readline().rstrip()]


def calc_num(phase, pos):
    pattern = [0] * (pos + 1) + [1] * (pos + 1) + \
        [0] * (pos + 1) + [-1] * (pos + 1)
    result = 0
    for i in range(len(phase)):
        result += phase[i] * pattern[(i + 1) % len(pattern)]

    return abs(result) % 10


def calc_next_phase(phase):
    result = []
    for i in range(len(phase)):
        result.append(calc_num(phase, i))

    return result


def calc_phase(init_phase, n):
    phase = init_phase
    for _ in range(n):
        phase = calc_next_phase(phase)

    return phase


# PART 1
init_phase = read_input()
phase_100 = calc_phase(init_phase, 100)
print("".join(str(x) for x in phase_100)[0:8])

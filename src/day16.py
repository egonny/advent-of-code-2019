INPUT = "input/16.in"


def read_input():
    with open(INPUT) as f:
        return [int(x) for x in f.readline().rstrip()]


def sign_pos(idx, pos):
    return 1 if (idx + 1) % (4 * (pos + 1)) <= 2 * (pos + 1) else -1


def calc_num(phase, pos):
    if pos >= len(phase) / 2:
        return sum(phase[pos:])

    filtered = [x * sign_pos(idx, pos)
                for (idx, x) in enumerate(phase) if (idx + 1) % (2 * (pos + 1)) >= (pos + 1)]
    result = sum(filtered)

    return abs(result) % 10


def calc_phase_fast(phase, pos):
    result = []
    inter = 0
    for i in range(len(phase) - 1, pos - 1, -1):
        inter += phase[i]
        result.append(abs(inter) % 10)
    result.reverse()
    return result


def calc_next_phase(phase, min_pos=0):
    if min_pos >= len(phase) / 2:
        return [0] * min_pos + calc_phase_fast(phase, min_pos)
    result = [0] * min_pos
    for i in range(min_pos, len(phase)):
        result.append(calc_num(phase, i))
    return result


def calc_phase(init_phase, n, min_pos=0):
    phase = init_phase
    for i in range(n):
        print(i)
        phase = calc_next_phase(phase, min_pos=min_pos)
        print(phase[min_pos:min_pos+8])

    return phase


# PART 1
init_phase = read_input()
# phase_100 = calc_phase(init_phase, 100)
# print("".join(str(x) for x in phase_100)[0:8])

# PART 2
long_phase = read_input() * 10000
skip_bytes = sum(x * 10 ** (6 - idx)
                 for (idx, x) in enumerate(long_phase[0:7]))
phase_100 = calc_phase(long_phase, 100, min_pos=skip_bytes)
# print(phase_100[skip_bytes:])
print("".join(str(x) for x in phase_100)[skip_bytes:skip_bytes+8])

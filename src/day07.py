from io import StringIO
from itertools import permutations
import sys

INPUT = "input/07.in"

def read_input():
    with open(INPUT) as f:
        return [int(item) for line in f for item in line.split(",")]

def get_intcode_value(intcode, pos, immediate):
    val = intcode[pos]
    if immediate:
        return val
    return intcode[val]

class Evaluator:
    instruction_pointer = 0
    __stopped = False

    def __handle_addition(self, modes):
        modes += [False] * (2 - len(modes))
        in1 = get_intcode_value(self.intcode, self.instruction_pointer, modes[0])
        in2 = get_intcode_value(self.intcode, self.instruction_pointer + 1, modes[1])
        pos_out = self.intcode[self.instruction_pointer + 2]
        self.intcode[pos_out] = in1 + in2
        self.instruction_pointer += 3

    def __handle_multiplication(self, modes):
        modes += [False] * (2 - len(modes))
        in1 = get_intcode_value(self.intcode, self.instruction_pointer, modes[0])
        in2 = get_intcode_value(self.intcode, self.instruction_pointer + 1, modes[1])
        pos_out = self.intcode[self.instruction_pointer + 2]
        self.intcode[pos_out] = in1 * in2
        self.instruction_pointer += 3

    def __handle_halt(self, modes):
        self.__stopped = True
        self.instruction_pointer += 1

    def __handle_input(self, modes):
        pos_out = self.intcode[self.instruction_pointer]
        self.intcode[pos_out] = int(self.input.readline().replace("\x00", ""))
        self.instruction_pointer += 1

    def __handle_output(self, modes):
        modes += [False] * (1 - len(modes))
        self.output.write(f"{get_intcode_value(self.intcode, self.instruction_pointer, modes[0])}\n")
        self.instruction_pointer += 1
    
    def __handle_jit(self, modes):
        modes += [False] * (2 - len(modes))
        in1 = get_intcode_value(self.intcode, self.instruction_pointer, modes[0])
        in2 = get_intcode_value(self.intcode, self.instruction_pointer + 1, modes[1])
        if in1 != 0:
            self.instruction_pointer = in2
        else:
            self.instruction_pointer += 2

    def __handle_jif(self, modes):
        modes += [False] * (2 - len(modes))
        in1 = get_intcode_value(self.intcode, self.instruction_pointer, modes[0])
        in2 = get_intcode_value(self.intcode, self.instruction_pointer + 1, modes[1])
        if in1 == 0:
            self.instruction_pointer = in2
        else:
            self.instruction_pointer += 2
    
    def __handle_lt(self, modes):
        modes += [False] * (2 - len(modes))
        in1 = get_intcode_value(self.intcode, self.instruction_pointer, modes[0])
        in2 = get_intcode_value(self.intcode, self.instruction_pointer + 1, modes[1])
        pos_out = self.intcode[self.instruction_pointer + 2]
        self.intcode[pos_out] = 1 if in1 < in2 else 0

        self.instruction_pointer += 3

    def __handle_eq(self, modes):
        modes += [False] * (2 - len(modes))
        in1 = get_intcode_value(self.intcode, self.instruction_pointer, modes[0])
        in2 = get_intcode_value(self.intcode, self.instruction_pointer + 1, modes[1])
        pos_out = self.intcode[self.instruction_pointer + 2]
        self.intcode[pos_out] = 1 if in1 == in2 else 0
        
        self.instruction_pointer += 3

    __handlers = {
        1: __handle_addition,
        2: __handle_multiplication,
        3: __handle_input,
        4: __handle_output,
        5: __handle_jit,
        6: __handle_jif,
        7: __handle_lt,
        8: __handle_eq,
        99: __handle_halt
    }

    def __init__(self, intcode, input=sys.stdin, output=sys.stdout):
        self.intcode = intcode
        self.input = input
        self.output = output

    def is_stopped(self):
        return self.__stopped

    def evaluate(self):
        if self.is_stopped():
            return

        instruction = str(self.intcode[self.instruction_pointer])
        self.instruction_pointer += 1
        opcode = int(instruction[-2:])
        self.__handlers[opcode](self, [x == "1" for x in instruction[-3::-1]])

class Amplifier:
    def __init__(self, intcode, phase, input):
        self.input = StringIO(f"{phase}\n{input}")
        self.output = StringIO()
        self.evaluator = Evaluator(intcode, input=self.input, output=self.output)
    
    def get_output(self):
        while not self.evaluator.is_stopped():
            self.evaluator.evaluate()
        
        return int(self.output.getvalue())

# PART 1
intcode = read_input()
max = (0, None)
for combination in permutations(range(5)):
    input = 0
    for phase in combination:
        amp = Amplifier(intcode.copy(), phase, input)
        input = amp.get_output()
    if max[0] < input:
        max = (input, combination)
print(f"Part 1: {max[0]}")

# PART 2
class Amplifier2:
    def __init__(self, intcode, phase):
        self.input = StringIO()
        self.input.write(f"{phase}\n")
        self.output = StringIO()
        self.evaluator = Evaluator(intcode, input=self.input, output=self.output)
    
    def get_output(self, input):
        self.input.write(f"{input}\n")
        self.input.seek(0)
        self.output.truncate(0)
        while not (self.output.getvalue() or self.is_stopped()):
            self.evaluator.evaluate()
        
        if self.is_stopped():
            return None
        self.output.seek(0)
        self.input.truncate(0)
        result = int(self.output.readline().replace("\x00", ""))
        return result
    
    def is_stopped(self):
        return self.evaluator.is_stopped()

max = (0, None)
for combination in permutations(range(5, 10)):
    amps = [Amplifier2(intcode.copy(), phase) for phase in combination]
    input = 0
    stopped = False
    i = 0
    while not stopped:
        amp = amps[i % 5]
        output = amp.get_output(input)
        if output == None:
            stopped = True
        else:
            input = output
        i += 1

    if max[0] < input:
        max = (input, combination)
print(f"Part 2: {max[0]}")
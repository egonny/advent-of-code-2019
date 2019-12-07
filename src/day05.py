INPUT = "input/05.in"

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
        self.intcode[pos_out] = int(input("Enter value: "))
        self.instruction_pointer += 1

    def __handle_output(self, modes):
        modes += [False] * (1 - len(modes))
        print(get_intcode_value(self.intcode, self.instruction_pointer, modes[0]))
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

    def __init__(self, intcode):
        self.intcode = intcode

    def is_stopped(self):
        return self.__stopped

    def evaluate(self):
        if self.is_stopped():
            return

        instruction = str(self.intcode[self.instruction_pointer])
        self.instruction_pointer += 1
        opcode = int(instruction[-2:])
        self.__handlers[opcode](self, [x == "1" for x in instruction[-3::-1]])

# PART 1+2
intcode = read_input()
evaluator = Evaluator(intcode)
while not evaluator.is_stopped():
    evaluator.evaluate()
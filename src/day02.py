INPUT = "input/02.in"

def read_input():
    with open(INPUT) as f:
        return [int(item) for line in f for item in line.split(",")]

class Evaluator:
    instruction_pointer = 0
    __stopped = False

    def __handle_addition(self):
        pos_in1 = self.intcode[self.instruction_pointer]
        pos_in2 = self.intcode[self.instruction_pointer + 1]
        pos_out = self.intcode[self.instruction_pointer + 2]
        self.intcode[pos_out] = self.intcode[pos_in1] + self.intcode[pos_in2]
        self.instruction_pointer += 3

    def __handle_multiplication(self):
        pos_in1 = self.intcode[self.instruction_pointer]
        pos_in2 = self.intcode[self.instruction_pointer + 1]
        pos_out = self.intcode[self.instruction_pointer + 2]
        self.intcode[pos_out] = self.intcode[pos_in1] * self.intcode[pos_in2]
        self.instruction_pointer += 3

    def __handle_halt(self):
        self.__stopped = True
        self.instruction_pointer += 1

    __handlers = {
        1: __handle_addition,
        2: __handle_multiplication,
        99: __handle_halt
    }

    def __init__(self, intcode):
        self.intcode = intcode

    def is_stopped(self):
        return self.__stopped

    def evaluate(self):
        if self.is_stopped():
            return

        opcode = self.intcode[self.instruction_pointer]
        self.instruction_pointer += 1
        try:
            self.__handlers[opcode](self)
        except:
            self.__stopped = True

# PART 1
input = read_input()
input[1] = 12
input[2] = 2
evaluator = Evaluator(input)
while not evaluator.is_stopped():
    evaluator.evaluate()
print(f"Value at pos 0: {evaluator.intcode[0]}")

# PART 2
def run_input(input):
    evaluator = Evaluator(input)
    while not evaluator.is_stopped():
        evaluator.evaluate()
    return evaluator.intcode[0]

def find_noun_verb(goal):
    orig_input = read_input()
    for noun in range(256):
        for verb in range(256):
            input = orig_input.copy()
            input[1] = noun
            input[2] = verb

            output = run_input(input)
            if output == goal:
                return (noun, verb)

(noun, verb) = find_noun_verb(19690720)
print(f"100 * noun + verb = {100 * noun + verb}")
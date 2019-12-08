WIDTH = 25
HEIGHT = 6

INPUT = "input/08.in"

def read_input():
    with open(INPUT) as f:
        line = f.readline().rstrip()
        length = WIDTH * HEIGHT
        return [line[i:i+length] for i in range(0, len(line), length)]

layers = read_input()

# PART 1
layer = min(layers, key=lambda x: x.count("0"))
product = layer.count("1") * layer.count("2")
print(f"Part 1: {product}")

# PART 2
image = [[None] * WIDTH for x in range(HEIGHT)]

for layer in layers:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            pixel = layer[y * WIDTH + x]
            if image[y][x] == None and pixel != "2":
                image[y][x] = pixel

print("Part 2")
for row in image:
    print("".join(map(lambda x: " " if x == "0" else "\u2588", row)))
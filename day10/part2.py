with open("data.txt", mode="r") as f:
    commands = [command.split(" ") for command in f.read().splitlines()]

WIDTH = 40

signal = [1]
for command in commands:
    if len(command) == 1:
        signal.append(signal[-1])
    else:
        signal.append(signal[-1])
        signal.append(signal[-1] + int(command[1]))

for line in range((len(signal) - 1) // WIDTH):
    drawing = ""
    for position in range(WIDTH):
        cycle = position + line * WIDTH
        if abs(position - signal[cycle]) <= 1:
            drawing += "##"
        else:
            drawing += ".."
    print(drawing)

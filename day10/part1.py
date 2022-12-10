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

total = [signal[19 + num * WIDTH] * (20 + num * WIDTH) for num in range(6)]

print(total)
print(sum(total))

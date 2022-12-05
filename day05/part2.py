from re import findall

with open("data.txt", mode="r") as f:
    stacks, moves = f.read().split("\n\n")

moves = [[int(num) for num in findall("[0-9]+", move)] for move in moves.split("\n")]
num_of_stacks = int(findall("[0-9]+", stacks.split("\n")[-1])[-1])
stacks = [
    [stack[col * 4 + 1] for col in range(num_of_stacks)]
    for stack in stacks.split("\n")[:-1]
]
queues = [[item for item in row if item != " "] for row in zip(*reversed(stacks))]

for move in moves:
    queues[move[2] - 1].extend(queues[move[1] - 1][-move[0]:])
    queues[move[1] - 1] = queues[move[1] - 1][:-move[0]]

answer = "".join([queue[-1] for queue in queues])

print(answer)

with open("data.txt", mode="r") as f:
    data = f.read()

sorted_calories = sorted([sum([int(y) for y in x.split("\n")]) for x in data.split("\n\n")])
max_calories = sorted_calories[-1]
max3_calories = sum(sorted_calories[-3:])

print(f"Max calories: {max_calories}")
print(f"Max 3 calories: {max3_calories}")

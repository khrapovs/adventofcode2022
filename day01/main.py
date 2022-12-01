from operator import itemgetter

with open("data.txt", mode="r") as f:
    data = f.read()

calories_by_elf = [sum([int(y) for y in x.split("\n")]) for x in data.split("\n\n")]
elfs_number, max_calories = max(enumerate(calories_by_elf), key=itemgetter(1))

print(f"Calories for each elf: {calories_by_elf}")
print(f"Elf's number: {elfs_number}, calories: {max_calories}")

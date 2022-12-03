from string import ascii_lowercase, ascii_uppercase

with open("data.txt", mode="r") as f:
    rucksacks = [rucksack for rucksack in f.read().split("\n")]

compartments = []
for rucksack in rucksacks:
    number_of_items = len(rucksack) // 2
    compartments.append((rucksack[:number_of_items], rucksack[number_of_items:]))

values_lo = {letter: value + 1 for value, letter in enumerate(ascii_lowercase)}
values_up = {letter: value + 27 for value, letter in enumerate(ascii_uppercase)}
values = {**values_lo, **values_up}

scores = [
    values[list(set(compartment[0]).intersection(set(compartment[1])))[0]]
    for compartment in compartments
]

print(sum(scores))

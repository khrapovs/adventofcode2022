from string import ascii_lowercase, ascii_uppercase

with open("data.txt", mode="r") as f:
    rucksacks = [rucksack for rucksack in f.read().split("\n")]

groups = [
    rucksacks[group_id * 3 : (group_id + 1) * 3]
    for group_id in range(len(rucksacks) // 3)
]

values_lo = {letter: value + 1 for value, letter in enumerate(ascii_lowercase)}
values_up = {letter: value + 27 for value, letter in enumerate(ascii_uppercase)}
values = {**values_lo, **values_up}

scores = [
    values[
        list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
    ]
    for group in groups
]

print(sum(scores))

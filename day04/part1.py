def expand_range(sections: str) -> set:
    first, second = sections.split("-")
    return set(range(int(first), int(second) + 1))


def one_is_subset(pair: tuple[set, set]) -> bool:
    return pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])


with open("data.txt", mode="r") as f:
    pairs = [pair.split(",") for pair in f.read().split("\n")]

sections = [(expand_range(pair[0]), expand_range(pair[1])) for pair in pairs]
subsets = [one_is_subset(section) for section in sections]

print(sum(subsets))

with open("data.txt", mode="r") as f:
    encrypted_plays = [tuple(turn.split(" ")) for turn in f.read().split("\n")]

# A - Rock
# B - Paper
# C - Scissors
values = {"A": 1, "B": 2, "C": 3}
wins = {"A": "B", "B": "C", "C": "A"}
draws = {x: y for x, y in zip(values.keys(), values.keys())}
losses = {y: x for x, y in wins.items()}
my_choice_values = {"X": (0, losses), "Y": (3, draws), "Z": (6, wins)}


def compute_score(play: tuple) -> int:
    opponents_choice = play[0]  # A B C
    my_choice = play[1]  # X Y Z
    recommended_plays = my_choice_values[my_choice][1]
    return my_choice_values[my_choice][0] + values[recommended_plays[opponents_choice]]


total_score = sum([compute_score(play) for play in encrypted_plays])

print(total_score)

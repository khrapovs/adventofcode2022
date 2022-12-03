with open("data.txt", mode="r") as f:
    plays = [tuple(turn.split(" ")) for turn in f.read().split("\n")]

# A, X - Rock
# B, Y - Paper
# C, Z - Scissors
opponents_choices = ["A", "B", "C"]
my_choice_values = {"X": 1, "Y": 2, "Z": 3}
wins = {("A", "Y"), ("B", "Z"), ("C", "X")}
draws = {(x, y) for x, y in zip(opponents_choices, my_choice_values.keys())}


def compute_score(play: tuple) -> int:
    score = 6 if play in wins else 3 if play in draws else 0
    return score + my_choice_values[play[-1]]


total_score = sum([compute_score(play) for play in plays])

print(total_score)

TABLE_T = list[list[int]]
COORDINATES_T = list[list[tuple[int, int]]]
SCORE_T = dict[tuple[int, int], int]

with open("data.txt", mode="r") as f:
    raw_forest = [[int(tree) for tree in row] for row in f.read().splitlines()]


forest_coordinates = [
    [(row, col) for col in range(len(raw_forest[0]))] for row in range(len(raw_forest))
]
tree_score = {
    (row, col): 1 for col in range(len(raw_forest[0])) for row in range(len(raw_forest))
}


def compute_scores(forest: TABLE_T, coordinates: COORDINATES_T, score: SCORE_T) -> SCORE_T:
    for row, row_coordinates in zip(forest, coordinates):
        for num in range(len(row) - 1):
            temp_score = 1
            for num_neighbor in range(num + 1, len(row) - 1):
                temp_score += 1
                if row[num_neighbor + 1] >= row[num]:
                    break
            score[row_coordinates[num]] *= temp_score
    return score


def rotate(table: TABLE_T | COORDINATES_T) -> TABLE_T | COORDINATES_T:
    return [list(row) for row in zip(*reversed(table))]


for _ in range(4):
    raw_forest = rotate(table=raw_forest)
    forest_coordinates = rotate(table=forest_coordinates)
    tree_score = compute_scores(
        forest=raw_forest, coordinates=forest_coordinates, score=tree_score
    )

answer = max(tree_score.values())

print(answer)

TABLE_T = list[list[int]]
COORDINATES_T = list[list[tuple[int, int]]]

with open("data.txt", mode="r") as f:
    raw_forest = [[int(tree) for tree in row] for row in f.read().splitlines()]


forest_coordinates = [[(row, col) for col in range(len(raw_forest[0]))] for row in range(len(raw_forest))]
visible_trees = set()


def cleanup(forest: TABLE_T, coordinates: COORDINATES_T, visible: set) -> set:
    for row, row_coordinates in zip(forest, coordinates):
        visible = visible.union({row_coordinates[0]})
        max_height = row[0]
        for num in range(len(row) - 1):
            if row[num + 1] > max(row[num], max_height):
                visible = visible.union({row_coordinates[num + 1]})
                max_height = row[num + 1]
            else:
                continue
    return visible


def rotate(table: TABLE_T | COORDINATES_T) -> TABLE_T | COORDINATES_T:
    return [list(row) for row in zip(*reversed(table))]


for _ in range(4):
    raw_forest = rotate(table=raw_forest)
    forest_coordinates = rotate(table=forest_coordinates)
    visible_trees = cleanup(
        forest=raw_forest, coordinates=forest_coordinates, visible=visible_trees
    )

answer = len(visible_trees)

print(answer)

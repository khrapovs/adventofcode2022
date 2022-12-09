from __future__ import annotations

with open("data.txt", mode="r") as f:
    moves = [move.split(" ") for move in f.read().splitlines()]

moves = [(move[0], int(move[1])) for move in moves]


class Knot:
    def __init__(self) -> None:
        self.location: tuple[int, int] = (0, 0)  # (row, col)
        self.visited = {self.location}

    def move(self, direction: str) -> None:
        match direction:
            case "R":
                self.location = (self.location[0], self.location[1] + 1)
            case "L":
                self.location = (self.location[0], self.location[1] - 1)
            case "U":
                self.location = (self.location[0] + 1, self.location[1])
            case "D":
                self.location = (self.location[0] - 1, self.location[1])

    def multi_move(self, steps: tuple[str, str]) -> None:
        for step in steps:
            self.move(direction=step)
        self.visited = self.visited.union({self.location})

    def direction(self, other: Knot) -> tuple[str, str]:
        vertical_distance = other.location[0] - self.location[0]
        horizontal_distance = other.location[1] - self.location[1]
        if vertical_distance > 0:
            vertical = "U"
        elif vertical_distance < 0:
            vertical = "D"
        else:
            vertical = "S"
        if horizontal_distance > 0:
            horizontal = "R"
        elif horizontal_distance < 0:
            horizontal = "L"
        else:
            horizontal = "S"
        return vertical, horizontal

    def is_touching(self, other: Knot) -> bool:
        return all(self._distance(axis=axis, other=other) <= 1 for axis in [0, 1])

    def _distance(self, axis: int, other: Knot) -> int:
        return abs(self.location[axis] - other.location[axis])


head = Knot()
tail = Knot()

for move in moves:
    for _ in range(move[1]):
        head.move(direction=move[0])
        if not head.is_touching(other=tail):
            tail.multi_move(steps=tail.direction(other=head))

answer = len(tail.visited)

print(answer)

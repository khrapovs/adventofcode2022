import operator
from functools import reduce
from math import lcm
from re import findall
from typing import Callable

with open("data.txt", mode="r") as f:
    monkey_data = f.read().splitlines()


class Monkey:
    def __init__(
        self,
        starting_items: list[int],
        operation: Callable,
        divisor: int,
        next_monkey: dict[bool, int],
    ) -> None:
        self.starting_items = starting_items
        self.operation = operation
        self.divisor = divisor
        self.next_monkey = next_monkey
        self.total_inspections = 0

    def play(self, lcm_value: int) -> list[tuple[int, int]]:
        processed = list()
        while len(self.starting_items) > 0:
            new_item = self.operation(self.starting_items.pop(0)) % lcm_value
            divisible = new_item % self.divisor == 0
            processed.append((self.next_monkey[divisible], new_item))
            self.total_inspections += 1
        return processed


def operation_fun(fun: Callable, right: int = None) -> Callable:
    return lambda left: fun(left, left) if right is None else fun(left, right)


def convert_to_bool(value: str) -> bool:
    return True if value == "true" else False


def extract_true_or_false(value: str) -> str:
    return value.split(":")[0].split(" ")[-1]


def extract_monkey_name(value: str) -> int:
    return int(value.split(" ")[-1])


def get_next_monkey_names(data: list[str], line_no: int) -> dict[bool, int]:
    return {
        convert_to_bool(
            extract_true_or_false(data[line_no + num])
        ): extract_monkey_name(data[line_no + num])
        for num in [3, 4]
    }


def get_divisor(data: list[str], line_no: int) -> int:
    return int(data[line_no + 2].split(" ")[-1])


def get_monkey_operation(data: list[str], line_no: int) -> Callable:
    description = data[line_no + 1].split("old ")[-1].split(" ")
    right_is_old = description[1] == "old"
    match description[0]:
        case "+":
            my_operator = operator.add
        case "*":
            my_operator = operator.mul
        case _:
            my_operator = operator.add
    return operation_fun(
        fun=my_operator, right=None if right_is_old else int(description[1])
    )


def get_starting_items(data: list[str], line_no: int) -> list[int]:
    return [int(value) for value in findall("\d+", data[line_no])]


monkeys = [
    Monkey(
        starting_items=get_starting_items(data=monkey_data, line_no=num_line),
        operation=get_monkey_operation(data=monkey_data, line_no=num_line),
        divisor=get_divisor(data=monkey_data, line_no=num_line),
        next_monkey=get_next_monkey_names(data=monkey_data, line_no=num_line),
    )
    for num_line in range(1, len(monkey_data), 7)
]

multiplier = lcm(*[monkey.divisor for monkey in monkeys])

for i in range(10000):
    for monkey in monkeys:
        for monkey_num, item in monkey.play(lcm_value=multiplier):
            monkeys[monkey_num].starting_items.append(item)

total_inspections = sorted([monkey.total_inspections for monkey in monkeys])[-2:]

print(reduce(operator.mul, total_inspections))

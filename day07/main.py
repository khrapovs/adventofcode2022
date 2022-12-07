from re import match

with open("data.txt", mode="r") as f:
    terminal = f.read().split("\n")

path = []
contents: dict[tuple, int] = dict()

for line in terminal:
    match_cd_in_command = match("^\$\scd\s([\w\/]+).*", line)
    match_cd_out_command = match("^\$\scd\s\.\..*", line)
    match_ls_file = match("^(\d+)\s([\w\W]+).*", line)
    if match_cd_in_command:
        path.append(match_cd_in_command.group(1))
        if tuple(path) not in contents.keys():
            contents[tuple(path)] = 0
    elif match_cd_out_command:
        path.pop(-1)
    elif match_ls_file:
        current_path = []
        for folder in path:
            current_path.append(folder)
            contents[tuple(current_path)] += int(match_ls_file.group(1))


answer = sum(value for name, value in contents.items() if value < 1e5)

print(answer)

needed_space = 3e7 - (7e7 - contents[("/",)])

print(min(value for name, value in contents.items() if value >= needed_space))
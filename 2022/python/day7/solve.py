from collections import defaultdict
import itertools

# input
with open("2022/python/day7/input.txt") as f:
    lines = f.readlines()

dict = defaultdict(int)
path = []  # 現在位置のパスを記録する

for line in lines:
    command = line.strip().split(" ")
    match command:
        case "$", "cd", "/": path = ["/"]
        case "$", "ls": continue
        case "dir", _: continue
        case "$", "cd", "..": path.pop()
        case "$", "cd", x: path.append(x + "/")
        case size, _: 
            # 親、親の親...のディレクトリまでサイズを足す
            for dir in itertools.accumulate(path):
                dict[dir] += int(size)

# part1
ans1 = 0
for value in dict.values():
    if value <= 10000:
        ans1 += value
print(ans1)

# part2
needed_size = 30000000 - (70000000 - dict["/"])  # 消す必要があるサイズ

# 全ディレクトリを見てneeded_size
for size in sorted(dict.values()):
    if size > needed_size:
        break

print(size)
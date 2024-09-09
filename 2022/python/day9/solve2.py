SIZE = 1000  # is_visitedの大きさ
is_visited = [[False] * SIZE for _ in range(SIZE)]  # 訪れた場所
all_now = [{"x": SIZE//2, "y": SIZE//2} for _ in range(10)]  # 初期位置をグリッドの中央にする

def move_target(prev_now: dict, target_now: dict):
    vector = {"x": prev_now["x"] - target_now["x"], "y": prev_now["y"] - target_now["y"]}
    move_vector = {
        "x": 0 if vector["x"] == 0 else vector["x"] // abs(vector["x"]), 
        "y": 0 if vector["y"] == 0 else vector["y"] // abs(vector["y"]) 
    }
    if abs(vector["x"]) == 2 or abs(vector["y"]) == 2:
        target_now["x"] += move_vector["x"]
        target_now["y"] += move_vector["y"]
    
    if (target_now == all_now[9]):
        is_visited[target_now["y"]][target_now["x"]] = True

def move_part2(command):
    command = command.strip().split(" ")
    match command:
        case "U", num: 
            for _ in range(int(num)):
                all_now[0]["y"] += 1  # 下へ
                for i in range(1, 10):
                    move_target(all_now[i-1], all_now[i])
        case "D", num:
            for _ in range(int(num)):
                all_now[0]["y"] -= 1  # 上へ
                for i in range(1, 10):
                    move_target(all_now[i-1], all_now[i])
        case "R", num:
            for _ in range(int(num)):
                all_now[0]["x"] += 1  # 左へ
                for i in range(1, 10):
                    move_target(all_now[i-1], all_now[i])
        case "L", num: 
            for _ in range(int(num)):
                all_now[0]["x"] -= 1  # 右へ
                for i in range(1, 10):
                    move_target(all_now[i-1], all_now[i])

# デバッグ用
def view_grid():
    grid = [["."] * SIZE for _ in range(SIZE)]
    for i in range(10):
        if (i == 0):
            grid[all_now[i]["y"]][all_now[i]["x"]] = "H"
        else:
            grid[all_now[i]["y"]][all_now[i]["x"]] = str(i)
    for line in grid:
        print(*line)
    print("\n")

with open("2022/python/day9/input.txt") as f:
    lines = f.readlines()

for line in lines:
    move_part2(line)
    # print(f"--- {line.rstrip()} ---")
    # view_grid()

count_true = sum(row.count(True) for row in is_visited)
print(f"part2: {count_true}")
SIZE = 1000  # is_visitedの大きさ
is_visited = [[False] * SIZE for _ in range(SIZE)]  # 訪れた場所

h_now = {"x": 0, "y": 0}
t_now = {"x": 0, "y": 0}

def move_part1(command):
    command = command.strip().split(" ")
    match command:
        case "U", num: 
            for _ in range(int(num)):
                h_now["y"] += 1  # 下へ
                move_target(h_now, t_now)
        case "D", num:
            for _ in range(int(num)):
                h_now["y"] -= 1  # 上へ
                move_target(h_now, t_now)
        case "R", num:
            for _ in range(int(num)):
                h_now["x"] += 1  # 左へ
                move_target(h_now, t_now)
        case "L", num: 
            for _ in range(int(num)):
                h_now["x"] -= 1  # 右へ
                move_target(h_now, t_now)

def move_target(prev_now: dict, target_now: dict):
    vector = {"x": prev_now["x"] - target_now["x"], "y": prev_now["y"] - target_now["y"]}
    move_vector = {
        "x": 0 if vector["x"] == 0 else vector["x"] // abs(vector["x"]), 
        "y": 0 if vector["y"] == 0 else vector["y"] // abs(vector["y"]) 
    }
    if abs(vector["x"]) == 2 or abs(vector["y"]) == 2:
        target_now["x"] += move_vector["x"]
        target_now["y"] += move_vector["y"]
    
    is_visited[target_now["y"]][target_now["x"]] = True

with open("2022/python/day9/input.txt") as f:
    lines = f.readlines()

for line in lines:
    move_part1(line)
count_true = sum(row.count(True) for row in is_visited)
print(f"part1: {count_true}")
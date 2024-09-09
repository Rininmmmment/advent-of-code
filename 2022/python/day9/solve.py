SIZE = 1000  # is_visitedの大きさ
is_visited = [[False] * SIZE for _ in range(SIZE)]  # 訪れた場所

h_now = {"x": 0, "y": 0}
t_now = {"x": 0, "y": 0}

def move_h(command):
    command = command.strip().split(" ")
    match command:
        case "U", num: 
            for _ in range(int(num)):
                h_now["y"] += 1  # 下へ
                move_t()
        case "D", num:
            for _ in range(int(num)):
                h_now["y"] -= 1  # 上へ
                move_t()
        case "R", num:
            for _ in range(int(num)):
                h_now["x"] += 1  # 左へ
                move_t()
        case "L", num: 
            for _ in range(int(num)):
                h_now["x"] -= 1  # 右へ
                move_t()

def move_t():
    th_vector = {"x": h_now["x"] - t_now["x"], "y": h_now["y"] - t_now["y"]}
    t_move_vector = {
        "x": 0 if th_vector["x"] == 0 else th_vector["x"] // abs(th_vector["x"]), 
        "y": 0 if th_vector["y"] == 0 else th_vector["y"] // abs(th_vector["y"]) 
    }
    if abs(th_vector["x"]) == 2 or abs(th_vector["y"]) == 2:
        t_now["x"] += t_move_vector["x"]
        t_now["y"] += t_move_vector["y"]
    
    is_visited[t_now["y"]][t_now["x"]] = True

# input
with open("2022/python/day9/input.txt") as f:
    lines = f.readlines()

for line in lines:
    move_h(line)
count_true = sum(row.count(True) for row in is_visited)
print(count_true)
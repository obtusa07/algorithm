import sys
sys.setrecursionlimit(10000)

def solution(maps):
    answer = []
    foods = 0
    visited = [
        [False for _ in range(len(maps[0]))]
        for _ in range(len(maps))
    ]

    def in_range(x, y):
        return 0 <= x < len(maps) and 0 <= y < len(maps[0])

    def can_go(x, y):
        if not in_range(x, y):
            return False
        if maps[x][y] == "X":
            return False
        return True

    def dfs(x, y):
        if not can_go(x, y) or visited[x][y]:
            return
        visited[x][y] = True
        nonlocal foods
        foods += int(maps[x][y])
        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            dfs(nx, ny)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j]:
                dfs(i, j)
                if foods != 0:
                    answer.append(foods)
                    foods = 0

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)
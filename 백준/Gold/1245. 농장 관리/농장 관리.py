import sys
sys.setrecursionlimit(1000)
n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    return True

dxs, dys = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
cnt = 0
is_top = True
def dfs(x, y):
    global is_top
    value = grid[x][y]
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny):
            if value < grid[nx][ny]:
                is_top = False
            if not visited[nx][ny] and value == grid[nx][ny]:
                dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if grid[i][j] > 0 and not visited[i][j]:
            dfs(i, j)
            if is_top:
                cnt += 1
            is_top = True

print(cnt)
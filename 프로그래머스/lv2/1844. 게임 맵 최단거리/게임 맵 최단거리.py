# bfs 문제
from collections import deque

def solution(maps):
    answer = 0
    q = deque()
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    return answer
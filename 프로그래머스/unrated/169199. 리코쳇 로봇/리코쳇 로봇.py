import collections

def solution (board):
    q = collections.deque()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                q.append((i, j, 0))
    visited = set()

    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        x, y, cnt = q.popleft()
        if (x, y) in visited:
            continue
        if board[x][y] == 'G':
            return cnt
        visited.add((x, y))
        for dx, dy in zip(dxs, dys):
            nx, ny = x, y
            while True:
                tx, ty = nx + dx, ny + dy
                if 0 <= tx < len(board) and 0 <= ty < len(board[0]) and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                    continue
                q.append((nx, ny, cnt + 1))
                break
    return -1
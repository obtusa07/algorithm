def solution(board):
    answer = 0
    visited = [
        [False for _ in range(len(board))]
        for _ in range(len(board))
    ]
    
    def in_range(x, y):
        return 0 <= x < len(board[0]) and 0 <= y < len(board)

    def can_go(x, y):
        if not in_range(x, y):
            return False
        if visited[x][y]:
            return False
        return True
    
    def dfs(x, y):                        
        dxs, dys = [-1, 1, 0 , 0, 1, 1, -1, -1], [0, 0, -1, 1, -1, 1, 1, -1]
        for dx, dy in zip(dxs, dys):
            nx = dx + x
            ny = y + dy
            if can_go(nx, ny) and board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                board[nx][ny] = 2
                if board[nx][ny] == 1:
                    dfs(nx, ny)
                
        
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] == 1:
                dfs(i, j)
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer += 1
    return answer
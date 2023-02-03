def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(num):
        visited[num] = True
        for i in range(n):
            if computers[num][i] and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
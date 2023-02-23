def solution(x, y, n):
    answer = 0
    dp = [1e9 for _ in range(y+1)]
    dp[x] = 0
        
    for i in range(x + 1, y + 1):
        if i//3 >= x and i % 3 == 0 and dp[i//3] != 1e9:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i//2 >= x and i % 2 == 0 and dp[i//2] != 1e9:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i-n >= x and dp[i-n] != 1e9:
            dp[i] = min(dp[i], dp[i - n]+1)
            
    answer = dp[y]
    if answer == 1e9:
        answer = -1
    return answer
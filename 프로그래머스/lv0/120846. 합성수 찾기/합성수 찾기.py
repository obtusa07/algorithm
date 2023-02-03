def solution(n):
    answer = 0
    for num in range(1, n+1):
        i = 1
        cnt = 0
        while i <= num:
            if num % i == 0:
                cnt += 1
            if cnt >= 3:
                answer += 1
                break
            i += 1
        
    return answer
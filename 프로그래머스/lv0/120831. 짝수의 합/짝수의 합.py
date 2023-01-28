def solution(n):
    answer = 0
    while n:
        if n % 2 != 1:
            answer += n
        n -= 1
    return answer
def solution(n, k):
    free_drink = n // 10
    answer = n*12000
    if k - free_drink > 0:
        answer += (k-free_drink)*2000
    return answer
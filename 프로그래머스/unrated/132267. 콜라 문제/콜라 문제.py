def solution(a, b, n):
    answer = 0
    
    while n >= a:
        original_n = n
        answer += (n // a) * b
        n -= (n // a) * a
        n += (original_n // a) * b
    return answer
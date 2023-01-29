def solution(n):
    answer = []
    i = 1
    while i <= n:
        if i % 2 == 1:
            answer.append(i)
        i += 1
    return answer
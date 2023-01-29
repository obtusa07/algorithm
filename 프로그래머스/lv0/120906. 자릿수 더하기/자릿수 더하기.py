def solution(n):
    answer = 0
    n_list = list(str(n))
    while n_list:
        answer += int(n_list.pop())
    return answer
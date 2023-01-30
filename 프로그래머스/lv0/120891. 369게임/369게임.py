def solution(order):
    answer = 0
    for s in str(order):
        if int(s) == 3 or int(s) == 6 or int(s) == 9:
            answer += 1
    return answer
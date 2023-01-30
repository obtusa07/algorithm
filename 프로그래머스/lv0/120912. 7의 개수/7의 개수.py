def solution(array):
    answer = 0
    for elem in array:
        for s in list(str(elem)):
            if s == '7':
                answer += 1
    return answer
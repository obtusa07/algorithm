import itertools

def solution(number):
    answer = 0
    numbers = list(itertools.combinations(number, 3))
    for group in numbers:
        if sum(group) == 0:
            answer += 1
    return answer
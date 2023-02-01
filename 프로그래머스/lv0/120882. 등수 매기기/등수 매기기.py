def solution(score):
    answer = []
    result = []
    for group in score:
        answer.append((group[0] + group[1])/2)
    memo = sorted(answer, reverse = True)
    for num in answer:
        result.append(memo.index(num) + 1)
    return result
def solution(sides):
    answer = set()
    for num in range(max(sides), sum(sides)):
        answer.add(num)
    for num in range(1, max(sides)+1):
        if min(sides) + num > max(sides):
            answer.add(num)
    return len(answer)
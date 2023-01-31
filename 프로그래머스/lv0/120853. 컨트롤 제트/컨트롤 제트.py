def solution(s):
    answer = []
    for elem in list(map(str, s.split())):
        if elem != "Z":
            answer.append(int(elem))
        else:
            answer.pop()
    return sum(answer)
def solution(numlist, n):
    answer = []
    temp = []
    for num in numlist:
        temp.append((abs(n - num), num))
    temp.sort(key= lambda x :(x[0], -x[1]))
    for tp in temp:
        answer.append(tp[1])
    return answer
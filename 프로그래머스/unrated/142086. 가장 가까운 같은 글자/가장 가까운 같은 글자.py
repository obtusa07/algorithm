import collections

def solution(s):
    answer = []
    dict = collections.defaultdict(int)
    for i, v in enumerate(s):
        if v not in dict:
            answer.append(-1)
            dict[v] = i
        else:
            answer.append(i - dict[v])
            dict[v] = i
    return answer
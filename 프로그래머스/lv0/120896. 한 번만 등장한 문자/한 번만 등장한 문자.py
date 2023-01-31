import collections

def solution(s):
    answer = []
    dict = collections.defaultdict(int)
    for c in s:
        dict[c] += 1
    
    for key in list(dict.keys()):
        if dict[key] == 1:
            answer.append(key)
    if len(answer) == 0:
        return ''
    else:
        return ''.join(sorted(answer))
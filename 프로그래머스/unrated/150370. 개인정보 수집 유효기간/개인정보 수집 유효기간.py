import collections

def solution(today, terms, privacies):
    answer = []
    dict = collections.defaultdict(int)
    today_day = ((int(today[:4]) - 2000)* 28*12) + int(today[5:7])*28 + int(today[-2:])
    for term in terms:
        array = term.split()
        dict[array[0]] = int(array[1])*28
    
    for i, v in enumerate(privacies):
        privacy = v
        day = ((int(privacy[:4]) - 2000)* 28*12) + int(privacy[5:7])*28 + int(privacy[8:10])
        type = privacy[-1]
        if dict[type] <= today_day - day:
            answer.append(i+1)
            
    return answer
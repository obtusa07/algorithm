import collections

def solution(name, yearning, photo):
    answer = []
    dict = collections.defaultdict(int)
    
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    for name_list in photo:
        temp = 0
        for name in name_list:
            temp += dict[name]
        answer.append(temp)
    
    return answer
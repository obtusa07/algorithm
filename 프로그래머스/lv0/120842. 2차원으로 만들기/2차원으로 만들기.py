def solution(num_list, n):
    answer = []
    while num_list:
        temp = []
        for _ in range(n):
            temp.append(num_list.pop(0))
        answer.append(temp)
    
    return answer
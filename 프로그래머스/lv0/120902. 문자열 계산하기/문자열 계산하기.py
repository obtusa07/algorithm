def solution(my_string):
    answer = 0
    array = list(map(str, my_string.split()))
    for i in range(len(array)):
        if i == 0:
            answer = int(array[i])
        if array[i] == "+": 
            answer += int(array[i+1])
        if array[i] == "-":
            answer -= int(array[i+1])            
    return answer
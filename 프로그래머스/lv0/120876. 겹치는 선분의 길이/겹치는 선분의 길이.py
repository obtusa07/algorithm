def solution(lines):
    answer = 0
    array = [0 for _ in range(200)]

    for line in lines:
        for i in range(line[0]+100, line[1]+100):
            if array[i] == 1:
                array[i] = 2
                answer += 1
            else:
                array[i] = 1
    return answer
def solution(s):
    answer = 0
    x = '-1'
    x_num = 0
    not_x_num = 0
    for i in range(len(s)):
        if x == '-1':
            x = s[i]
            x_num += 1
            continue
        if s[i] == x:
            x_num += 1
        else:
            not_x_num += 1
        if x_num == not_x_num:
            x_num = 0
            not_x_num=0
            x = '-1'
            answer += 1
    if x != '-1':
        answer += 1
    return answer
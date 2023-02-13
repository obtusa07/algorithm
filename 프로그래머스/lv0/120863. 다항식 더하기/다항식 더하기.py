def solution(polynomial):
    answer = ''
    polynomial = list(map(str, polynomial.split()))
    x_cnt = 0
    cnt = 0
    for elem in polynomial:
        if elem == '+':
            continue
        if elem == 'x':
            x_cnt += 1
            continue
        if elem[-1] == 'x':
            x_cnt += int(elem[:-1])
        else:
            cnt += int(elem)
    
    if x_cnt == 0:
        if cnt == 0:
            answer = "0"
        else:
            answer = f"{cnt}"
    else:
        if x_cnt == 1 and cnt == 0:
            answer = f"x"
        elif x_cnt == 1 and cnt != 0:
            answer = f"x + {cnt}"
        elif x_cnt != 1 and cnt == 0:
            answer = f"{x_cnt}x"
        elif x_cnt != 1 and cnt != 0:
            answer = f"{x_cnt}x + {cnt}"
    return answer
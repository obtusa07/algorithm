def solution(keymap, targets):
    answer = []
    for target in targets:
        target_num = 0
        for c in target:
            temp = 101
            check = True
            for key in keymap:
                if c in key:
                    check = False
                    temp = min(temp , key.index(c))
            if check:
                break
            else:
                target_num += temp+1
        if check:
            answer.append(-1)
        else:
            answer.append(target_num)
    return answer
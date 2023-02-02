def solution(common):
    answer = common[:3]
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] +common[2] - common[1]
    if common[2] // common[1] == common[1] // common[0]:
        return common[-1] * (common[2] // common[1])              
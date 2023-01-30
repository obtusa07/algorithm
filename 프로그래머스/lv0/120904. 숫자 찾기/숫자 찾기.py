def solution(num, k):
    num_list = list(str(num))
    if str(k) not in num_list:
        return -1
    return num_list.index(str(k)) + 1
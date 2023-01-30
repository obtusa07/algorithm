def solution(array):
    memo = [0]*1001
    for elem in array:
        memo[elem] += 1
        
    if memo.count(max(memo)) > 1:
        return -1
    return memo.index(max(memo))
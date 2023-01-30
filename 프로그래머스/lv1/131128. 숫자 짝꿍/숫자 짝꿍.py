def solution(X, Y):
    answer = ''
    for i in range(0, 10):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    
    if answer == '':
        return '-1'
    if answer.count("0") == len(answer):
        return '0'
    return answer[::-1]
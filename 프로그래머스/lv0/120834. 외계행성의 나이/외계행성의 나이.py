def solution(age):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in str(age):
        answer += alpha[int(i)]
    return answer
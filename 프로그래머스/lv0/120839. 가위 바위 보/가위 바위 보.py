def solution(rsp):
    answer = ''
    for game in rsp:
        if game == "2":
            answer += '0'
        if game == "0":
            answer += '5'
        if game == "5":
            answer += "2"
    return answer
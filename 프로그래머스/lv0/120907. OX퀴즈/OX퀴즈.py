def solution(quiz):
    answer = []
    
    for ask in quiz:
        ask_list = list(map(str, ask.split()))
        if ask_list[1] == '+':
            if int(ask_list[0]) + int(ask_list[2]) == int(ask_list[-1]):
                answer.append("O")
            else:
                answer.append("X")
        elif ask_list[1] == '-':
            if int(ask_list[0]) - int(ask_list[2]) == int(ask_list[-1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer
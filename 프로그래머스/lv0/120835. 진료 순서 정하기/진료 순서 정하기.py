def solution(emergency):
    sorted_list = sorted(emergency, reverse = True)
    answer = []
    for i, v in enumerate(emergency):
        answer.append(sorted_list.index(v)+1)
    return answer
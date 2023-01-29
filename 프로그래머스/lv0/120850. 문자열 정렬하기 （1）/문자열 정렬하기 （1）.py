def solution(my_string):
    answer = []
    for elem in my_string:
        if elem.isdigit():
            answer.append(int(elem))
    return sorted(answer)
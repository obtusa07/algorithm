import re

def solution(my_string):
    answer = 0
    my_string = my_string.lower()
    my_string = re.sub('[^0-9]', '', my_string)
    for elem in my_string:
        answer += int(elem)
    return answer
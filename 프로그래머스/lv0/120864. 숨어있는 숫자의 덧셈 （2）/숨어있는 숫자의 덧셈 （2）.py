import re
def solution(my_string):
    answer = 0
    my_string = my_string.lower()
    my_string = re.sub('[a-z]', "a", my_string)
    array = list(map(str, my_string.split("a")))
    for elem in array:
        if elem != "":
            answer += int(elem)
    return answer
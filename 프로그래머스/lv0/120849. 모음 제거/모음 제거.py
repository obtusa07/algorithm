import re

def solution(my_string):
    my_string = re.sub('a', '', my_string)
    my_string = re.sub('e', '', my_string)
    my_string = re.sub('i', '', my_string)
    my_string = re.sub('o', '', my_string)
    my_string = re.sub('u', '', my_string)
    return my_string
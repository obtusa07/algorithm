def solution(my_string, letter):
    my_string = list(my_string)
    while letter in my_string:
        del my_string[my_string.index(letter)]
    return ''.join(my_string)
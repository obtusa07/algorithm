def solution(my_string):
    result = []
    for elem in my_string:
        if elem.islower():
            result.append(elem.upper())
        else:
            result.append(elem.lower())
    return ''.join(result)
def solution(array, n):
    temp_array = []
    array = sorted(array)
    for i in array:
        temp_array.append(abs(i - n))
    return array[temp_array.index(min(temp_array))]
    
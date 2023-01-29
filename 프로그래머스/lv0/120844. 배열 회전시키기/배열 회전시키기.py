def solution(numbers, direction):
    if direction == 'right':
        temp = numbers.pop()
        numbers.insert(0, temp)
    else:
        temp = numbers[0]
        numbers.pop(0)
        numbers.append(temp)
    return numbers
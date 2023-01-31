def solution(numbers):
    numbers = sorted(numbers)
    
    if numbers[-1] * numbers[-2] > numbers[0] * numbers[1]:
        return numbers[-1] * numbers[-2]
    else:
        return numbers[0] * numbers[1]
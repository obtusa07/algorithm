import itertools, math

def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    result = 0
    def isPrime(num):
        if num < 2:
            return False
        
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
        return True
    
    for i in range(1, len(numbers)+1):
        answer.extend(list(itertools.permutations(nums, i)))
        
    new_num = [int(("").join(p)) for p in answer]
    for n in set(new_num):
        if isPrime(n):
            result += 1
            
    return result
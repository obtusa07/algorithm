import math

def solution(n):
    answer = []
    array = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    prime_list = [i for i in range(2, n+1) if array[i]]
    
    for num in prime_list:
        if n % num == 0:
            answer.append(num)
    
    return answer
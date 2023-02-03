import math

def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number+1):
        i = 1
        cnt = 0
        for i in range(1, int(num**(1/2))+1):
            if num % i == 0:
                cnt += 1
                if i != num // i:
                    cnt += 1
                    
        if cnt <= limit:
            answer += cnt
        else:
            answer += power
    return answer
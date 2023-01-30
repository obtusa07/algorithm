def solution(n):
    answer = 1
    def factorial(num):
        if num == 1:
            return 1
        return num * factorial(num - 1)
    
    while factorial(answer) <= n:
        answer += 1
        
    return answer - 1
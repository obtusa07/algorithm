def solution(balls, share):
    answer = 0
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)
    
    answer = factorial(balls) / (factorial(balls-share) * factorial(share))
    return answer
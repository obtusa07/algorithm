import collections

def solution(A, B):
    answer = 0
    stack = collections.deque(A)    
    for _ in range(len(B)):
        if list(stack) == list(B):
            return answer
        stack.appendleft(stack.pop())
        answer += 1    
        
    return -1
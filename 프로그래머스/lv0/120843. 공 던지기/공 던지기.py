import collections

def solution(numbers, k):
    stack = collections.deque(numbers)
    
    while k > 1:
        k -= 1
        stack.append(stack.popleft())
        stack.append(stack.popleft())
    
    return stack.popleft()
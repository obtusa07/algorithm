def solution(number, k):
    stack = []
    for num in number:
        # k이 아직 0 이 아니거나 stack이 안 비어져 있거나, 스택 마지막수가 num보다 작으면
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(number)-k])
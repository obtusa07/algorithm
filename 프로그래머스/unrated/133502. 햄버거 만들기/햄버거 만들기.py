def solution(ingredient):
    # 1, 2, 3, 1 -> 햄버거 하나
    burger = 0
    stack = []
    for num in ingredient:
        stack.append(num)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            burger += 1
    return burger
n = int(input())
stack = []
result = []

for _ in range(n):
    problem = input()
    is_false = True
    for c in problem:
        if c == "(":
            stack.append("(")
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_false = False
                break
    # 스택이 비었으면 성공

    if len(stack) == 0 and is_false:
        result.append("YES")
    else:
        result.append("NO")
    stack = []

for answer in result:
    print(answer)
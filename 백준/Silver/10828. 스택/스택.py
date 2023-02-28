n = int(input())
stack = []
array = []
for _ in range(n):
    order = list(input().split())

    if order[0] == 'push':
        stack.append(order[1])
    if order[0] == "top":
        if len(stack) == 0:
            array.append(-1)
        else:
            array.append(stack[-1])
    if order[0] == "size":
        array.append(len(stack))
    if order[0] == "empty":
        if len(stack):
            array.append(0)
        else:
            array.append(1)
    if order[0] == "pop":
        if len(stack) == 0:
            array.append(-1)
        else:
            array.append(stack[-1])
            stack.pop()

for elem in array:
    print(elem)
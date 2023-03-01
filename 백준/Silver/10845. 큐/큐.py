import collections
n = int(input())
q = collections.deque()
array = []

for _ in range(n):
    order = list(input().split())
    if order[0] == 'push':
        q.append(order[1])
    if order[0] == "back":
        if len(q) == 0:
            array.append(-1)
        else:
            array.append(q[-1])
    if order[0] == "front":
        if len(q) == 0:
            array.append(-1)
        else:
            array.append(q[0])
    if order[0] == "size":
        array.append(len(q))
    if order[0] == "empty":
        if len(q):
            array.append(0)
        else:
            array.append(1)
    if order[0] == "pop":
        if len(q) == 0:
            array.append(-1)
        else:
            array.append(q.popleft())

for elem in array:
    print(elem)
from collections import deque
q = deque()
n = int(input())
result = []
for _ in range(n):
    order = list(map(str, input().split()))
    if order[0] == "push_front":
        q.appendleft(order[1])
    if order[0] == "push_back":
        q.append(order[1])
    if order[0] == "pop_front":
        if not q:
            result.append(-1)
        else:
            t = q.popleft()
            result.append(t)
    if order[0] == "pop_back":
        if not q:
            result.append(-1)
        else:
            t = q.pop()
            result.append(t)
    if order[0] == "size":
        result.append(len(q))
    if order[0] == "empty":
        if len(q):
            result.append(0)
        else:
            result.append(1)
    if order[0] == "front":
        if not q:
            result.append(-1)
        else:
            result.append(q[0])
    if order[0] == "back":
        if not q:
            result.append(-1)
        else:
            result.append(q[-1])

for i in result:
    print(i)
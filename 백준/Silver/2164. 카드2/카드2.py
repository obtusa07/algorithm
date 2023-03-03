from _collections import deque

n = int(input())
q = deque()

for i in range(1, n+1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    if len(q) != 1:
        t = q.popleft()
        q.append(t)

print(q[0])

from _collections import deque
n, k = map(int, input().split())
result = []
q = deque()

for i in range(1, n+1):
    q.append(i)

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<", end="")
for i in range(len(result)-1):
    print(result[i], end=", ")
print(f"{result[-1]}>")
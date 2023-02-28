import math

m = int(input())
n = int(input())
result = []
for i in range(m, n+1):
    if int(math.sqrt(i)) == math.sqrt(i):
        result.append(i)

if len(result):
    print(sum(result))
    print(result[0])
else:
    print(-1)
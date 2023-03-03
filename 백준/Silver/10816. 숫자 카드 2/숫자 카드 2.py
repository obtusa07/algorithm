from collections import Counter

n = int(input())
narr = list(map(int, input().split()))

m = int(input())
marr = list(map(int, input().split()))

result = []
counter = Counter(narr)

for num in marr:
    result.append(counter[num])

for n in result:
    print(n, end=" ")
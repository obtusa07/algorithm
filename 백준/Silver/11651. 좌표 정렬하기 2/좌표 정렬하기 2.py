import sys
si = sys.stdin.readline
n = int(si())
arr = []
for _ in range(n):
    location = list(map(int, input().split()))
    arr.append(location)

arr.sort(key=lambda x: (x[1], x[0]))

for location in arr:
    print(str(location[0]) + " " + str(location[1]))

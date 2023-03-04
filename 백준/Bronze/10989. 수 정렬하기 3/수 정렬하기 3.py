import sys
si = sys.stdin.readline
n = int(si())
arr = [0] * 10001

for _ in range(n):
    i = int(si())
    arr[i] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)

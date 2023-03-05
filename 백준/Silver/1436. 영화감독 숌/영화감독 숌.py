import sys
si = sys.stdin.readline
n = int(si())
i = 0
while n != 0:
    if "666" in str(i):
        n -= 1
    i += 1

print(i-1)
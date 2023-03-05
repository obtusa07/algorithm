import  sys

si = sys.stdin.readline
k = int(si())
stack = []

for _ in range(k):
    num = int(si())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
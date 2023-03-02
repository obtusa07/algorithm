n = int(input())
arr = []
result = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


for guy in arr:
    cnt = 0
    for versus in arr:
        if versus[0] > guy[0] and versus[1] > guy[1]:
            cnt += 1
    result.append(cnt + 1)

for num in result:
    print(num, end=" ")
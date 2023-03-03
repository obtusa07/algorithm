n = int(input())

arr = []

for i in range(1, n+1):
    user = list(map(str, input().split()))
    user.append(i)
    arr.append(user)

arr.sort(key=lambda x: int(x[0]))
for user in arr:
    print(f"{user[0]} {user[1]}")

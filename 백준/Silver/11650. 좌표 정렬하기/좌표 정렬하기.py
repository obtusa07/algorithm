n = int(input())
arr = []

for _ in range(n):
    location = list(map(int, input().split()))
    arr.append(location)

arr.sort(key=lambda x: (x[0], x[1]))

for location in arr:
    print(f"{location[0]} {location[1]}")
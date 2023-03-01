n = int(input())
arr = []

for _ in range(n):
    word = input()
    if (len(word), word) not in arr:
        arr.append((len(word), word))

arr.sort(key=lambda x: (x[0], x[1]))

for i in arr:
    print(i[1])
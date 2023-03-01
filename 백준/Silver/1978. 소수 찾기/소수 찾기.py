n = int(input())
array = list(map(int, input().split()))
prime = [True] * 1001
cnt = 0
prime[0] = False
prime[1] = False

for i in range(2, 1001):
    j = 2
    while i*j <= 1000:
        prime[i*j] = False
        j += 1


for elem in array:
    if prime[elem]:
        cnt += 1

print(cnt)
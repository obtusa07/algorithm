
nums = list(map(int, input().split()))
temp = 0
for num in nums:
    temp += num ** 2

print(temp % 10)
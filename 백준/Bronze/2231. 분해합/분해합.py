n = int(input())
trigger = True
for i in range(n):
    check = 0
    list_i = list(str(i))
    for elem in list_i:
        check += int(elem)
    if i + check == n:
        print(i)
        trigger = False
        break
if trigger:
    print(0)
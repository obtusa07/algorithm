import sys
si = sys.stdin.readline

n = int(si())
n_arr = list(map(int, si().split()))
m = int(si())
m_arr = list(map(int, si().split()))

n_arr.sort()
for num in m_arr:
    lt, rt = 0, n - 1
    isExist = False

    while lt <= rt:
        mid = (lt + rt) // 2
        if num == n_arr[mid]:
            isExist = True
            break
        elif num > n_arr[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    if isExist:
        print(1)
    else:
        print(0)

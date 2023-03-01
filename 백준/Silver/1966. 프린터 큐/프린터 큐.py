import collections

t = int(input())

for _ in range(t):
    cnt = 0
    n, i = map(int, input().split())
    q = collections.deque(list(map(int, input().split())))

    while q:
        max_q = max(q)
        t = q.popleft()
        if t != max_q:
            q.append(t)
        else:
            cnt += 1
            if i == 0:
                print(cnt)
                break
        i -= 1
        if i == -1:
            i = len(q)-1
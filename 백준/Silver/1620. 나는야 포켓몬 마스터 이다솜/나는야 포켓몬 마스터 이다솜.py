import collections
dict = collections.OrderedDict()
n, m = map(int, input().split())

for i in range(1, n+1):
    dict[i] = input()

reverse_dict = {v:k for k, v in dict.items()}
ask = []
for _ in range(m):
    q = input()
    ask.append(q)

for q in ask:
    if q.isdigit():
        print(dict[int(q)])
    else:
        print(reverse_dict[q])
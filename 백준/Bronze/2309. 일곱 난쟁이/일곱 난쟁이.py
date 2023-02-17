import itertools

array = [int(input()) for _ in range(9)]

combis = itertools.combinations(array, 7)

for combi in combis:
    if sum(combi) == 100:
        for num in sorted(combi):
            print(num)
        break
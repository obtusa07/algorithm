import sys
from math import factorial
si = sys.stdin.readline
n, k = map(int, si().split())

def calc(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

print(calc(n, k))
